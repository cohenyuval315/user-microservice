import click
import uvicorn

from lib.common.loggers import logger
from server.app import create_app




@click.group()
def cli():
    """CLI for managing the FastAPI application."""
    pass

@cli.command()
@click.option("--host", default="127.0.0.1", help="Host to run the server.")
@click.option("--port", default=8000, help="Port to run the server.")
def runserver(host, port):
    """Run the FastAPI application."""
    click.echo(f"Starting server on http://{host}:{port}")
    uvicorn.run(app, host=host, port=port)

@cli.command()
def hello():
    """A simple hello command."""
    click.echo("Hello from the CLI!")

if __name__ == "__main__":
    cli()