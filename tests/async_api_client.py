import httpx
import json
from typing import Optional, Dict, Any, Union, Callable, Mapping, List, Tuple


class AsyncApiClient:
    def __init__(
        self,
        base_url: str,
        default_headers: Optional[Dict[str, str]] = None,
        default_timeout: int = 10000,
        auth: Optional[httpx.Auth] = None,
        verify: Union[bool, str] = True,
        cert: Optional[Union[str, Tuple[str, str]]] = None,
        http1: bool = True,
        http2: bool = False,
        proxies: Optional[Union[str, httpx.Proxy]] = None,
        follow_redirects: bool = False,
        limits: Optional[httpx.Limits] = None,
        event_hooks: Optional[Mapping[str, List[Callable]]] = None,
        trust_env: bool = True,
        transport: Optional[httpx.AsyncBaseTransport] = None,
        app: Optional[Callable[..., Any]] = None,
        proxy: Optional[str] = None,
        mounts: Optional[Mapping[str, Optional[httpx.AsyncBaseTransport]]] = None,
        cookies: Optional[Dict[str, str]] = None,
        default_encoding: Union[str, Callable[[bytes], str]] = "utf-8",
        max_redirects: int = 20,
        params: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the async API client with various advanced options.

        :param base_url: Base URL for the API.
        :param default_headers: Optional dictionary for default headers.
        :param default_timeout: Default timeout for requests in milliseconds.
        :param auth: Authentication (e.g., BasicAuth or custom Auth class).
        :param verify: SSL certificate verification (bool or path to a cert file).
        :param cert: Client-side certificates (single file or a tuple of cert and key).
        :param http1: Enable or disable HTTP/1.1.
        :param http2: Enable or disable HTTP/2.
        :param proxies: HTTP or HTTPS proxy URL.
        :param follow_redirects: Enable or disable automatic redirection.
        :param limits: Set limits on the number of connections.
        :param event_hooks: Event hooks for lifecycle events (request, response, etc.).
        :param trust_env: Whether to trust environment variables like HTTP_PROXY.
        :param transport: A custom transport instance.
        :param app: Optional ASGI app.
        :param proxy: Optional proxy URL.
        :param mounts: Optional mapping of transports for specific prefixes.
        :param cookies: Optional cookies to include in the requests.
        :param default_encoding: Default encoding for decoding responses.
        :param max_redirects: Maximum number of redirects.
        :param params: Default query parameters for requests.
        """
        self.base_url = base_url
        self.default_headers = default_headers or {}
        self.default_timeout = default_timeout / 1000  # Convert to seconds for `httpx`

        # Initialize the AsyncClient with all the additional parameters
        self.session = httpx.AsyncClient(
            base_url=base_url,
            headers=self.default_headers,
            auth=auth,
            verify=verify,
            cert=cert,
            http1=http1,
            http2=http2,
            proxies=proxies,
            follow_redirects=follow_redirects,
            limits=limits,
            event_hooks=event_hooks,
            trust_env=trust_env,
            timeout=httpx.Timeout(self.default_timeout),
            transport=transport,
            app=app,
            proxy=proxy,
            mounts=mounts,
            cookies=cookies,
            default_encoding=default_encoding,
            max_redirects=max_redirects,
            params=params,
        )

    async def __aenter__(self):
        """Enter the asynchronous context manager."""
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the asynchronous context manager and close the session."""
        await self.close()
        
    async def close(self) -> None:
        """ Close the async session when done. """
        await self.session.aclose()

    async def reset_session(self) -> None:
        """ Reset the session, clearing all cookies and state. """
        await self.close()  # Close the current session
        self.session = httpx.AsyncClient()  # Create a new session with default settings

    async def _build_headers(self, headers: Optional[Dict[str, str]], access_token: Optional[str] = None) -> Dict[str, str]:
        """ Merge default headers with additional headers and add JWT if provided. """
        final_headers = {**self.default_headers, **(headers or {})}
        if access_token:
            final_headers['Authorization'] = f"Bearer {access_token}"
        return final_headers

    def _build_url(self, path: str, query_params: Optional[Dict[str, Any]] = None) -> str:
        """
        Build the complete URL by combining base_url, path, and optional query parameters.
        
        :param path: The API endpoint path.
        :param query_params: Optional query parameters.
        :return: Complete URL as a string.
        """
        # Combine default params with the method-specific query params
        full_params = {}
        if self.session.params:
            full_params.update(self.session.params)
        if query_params:
            full_params.update(query_params)
            
        # If we have query parameters, append them to the URL
        if full_params:
            query_string = '&'.join(f"{k}={v}" for k, v in full_params.items())
            return f"{self.base_url}{path}?{query_string}"
        return f"{self.base_url}{path}"

    def _build_body(self, body: Optional[Union[Dict[str, Any], str]]) -> Optional[Union[str, Dict[str, Any]]]:
        """ Return body in the appropriate format, handling JSON and FormData. """
        if body and isinstance(body, dict):  # Assume JSON if it's a dictionary
            return json.dumps(body)
        return body

    async def _request(
        self,
        path: str,
        method: str,
        body: Optional[Union[Dict[str, Any], str]] = None,
        headers: Optional[Dict[str, str]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        access_token: Optional[str] = None,
        timeout: Optional[int] = None,
        files: Optional[Dict[str, Any]] = None
    ) -> Optional[httpx.Response]:
        """
        Generic async request function for all scenarios.

        :param path: The API endpoint path.
        :param method: HTTP method (GET, POST, PUT, DELETE).
        :param body: Request body (can be a dictionary for JSON or string for form data).
        :param headers: Optional headers for the request.
        :param query_params: Optional query parameters for the request.
        :param access_token: Optional JWT access token for Authorization header.
        :param timeout: Optional timeout to override default timeout.
        :param files: Optional files to upload (used for file upload endpoints).
        :return: Response object if successful, None otherwise.
        """
        request_headers = await self._build_headers(headers, access_token)
        url = self._build_url(path, query_params)
        request_body = self._build_body(body)
        effective_timeout = timeout / 1000 if timeout else self.default_timeout

        try:
            response = await self.session.request(
                method=method.upper(),
                url=url,
                headers=request_headers,
                content=request_body,  # Use content for async body
                files=files,
                timeout=effective_timeout
            )
            response.raise_for_status()
            return response
        except httpx.TimeoutException:
            print("Request timed out.")
        except httpx.RequestError as e:
            print(f"Error occurred: {e}")
        return None

    async def get(
        self,
        path: str,
        headers: Optional[Dict[str, str]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        access_token: Optional[str] = None,
        timeout: Optional[int] = None
    ) -> Optional[httpx.Response]:
        """ GET request wrapper. """
        return await self._request(path, "GET", headers=headers, query_params=query_params, access_token=access_token, timeout=timeout)

    async def post(
        self,
        path: str,
        body: Optional[Union[Dict[str, Any], str]] = None,
        headers: Optional[Dict[str, str]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        access_token: Optional[str] = None,
        timeout: Optional[int] = None,
        files: Optional[Dict[str, Any]] = None
    ) -> Optional[httpx.Response]:
        """ POST request wrapper. """
        return await self._request(path, "POST", body=body, headers=headers, query_params=query_params, access_token=access_token, timeout=timeout, files=files)

    async def put(
        self,
        path: str,
        body: Optional[Union[Dict[str, Any], str]] = None,
        headers: Optional[Dict[str, str]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        access_token: Optional[str] = None,
        timeout: Optional[int] = None
    ) -> Optional[httpx.Response]:
        """ PUT request wrapper. """
        return await self._request(path, "PUT", body=body, headers=headers, query_params=query_params, access_token=access_token, timeout=timeout)

    async def delete(
        self,
        path: str,
        headers: Optional[Dict[str, str]] = None,
        query_params: Optional[Dict[str, Any]] = None,
        access_token: Optional[str] = None,
        timeout: Optional[int] = None
    ) -> Optional[httpx.Response]:
        """ DELETE request wrapper. """
        return await self._request(path, "DELETE", headers=headers, query_params=query_params, access_token=access_token, timeout=timeout)

    async def get_cookies(self) -> Dict[str, str]:
        """ Get cookies currently stored in the session. """
        return self.session.cookies.jar.get_dict()

    async def set_cookies(self, cookies: Dict[str, str]) -> None:
        """ Manually set cookies for the session. """
        for name, value in cookies.items():
            self.session.cookies.set(name, value)

    async def clear_cookies(self) -> None:
        """ Clear all cookies from the session. """
        self.session.cookies.clear()
    