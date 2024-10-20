import sys
import os
import json
from dotenv import load_dotenv
from pathlib import Path

env = os.environ.get("ENVIRONMENT","development")

dotenv_path = Path(f'../../environments/.env.{env}')
load_dotenv(dotenv_path=dotenv_path)


sys.path.append(os.getenv('SERVICE_ROOT', '/'))

current_dir = os.path.dirname(os.path.abspath(__file__))
server_directory = os.path.join(current_dir)
version = f"{sys.version_info.major}.{sys.version_info.minor}"
sys.path.insert(0,server_directory)
sys.path.append("./src")
sys.path.append("../server/src")
sys.path.append(".")

# if os.getenv("RUN_IN_DOCKER", False):
#     # sys.path.insert(0, "/src/server")
#     pass
# else:
#    pass
    


from lib.common.loggers import logger
from app.application import create_app


if os.getenv("ENVIRONMENT", None) == "development" and os.getenv("DEBUG_ON_INIT",False) == True:
    import debugpy
    logger.info("Waiting for debugger to attach...")
    debugpy.wait_for_client() 

logger.info("Creating FastAPI application...")
logger.info(f"""\n    
    {
        json.dumps(
            {
                "python version:":version,
                "current dir":current_dir,
                "env": json.dumps(dict(os.environ.items())),
            },
            indent=2
        )
    }
""")


if __name__ == "__main__":
    app = create_app()

