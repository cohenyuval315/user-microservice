from fastapi import APIRouter


def register_version_endpoint(router:APIRouter):
    @router.get("/version", summary="Version info", response_description="Version details")
    async def version():
        return await get_version()


async def get_version():
    return {
        "version": "1.0.0",
        "commit": "abc123def",
        "build_date": "2024-08-25"
    }
