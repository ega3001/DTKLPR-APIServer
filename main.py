import uvicorn
from fastapi import FastAPI

from src.api.routes import router
from src.api.middleware import add_middlewares
from src.config import Config
from src.daemon import init_daemons
from src.app_logging import logger


app = FastAPI()
app.include_router(router)
add_middlewares(app)


if __name__ == '__main__':
    logger.info("Starting daemon...")
    init_daemons()
    logger.info("Starting server...")
    uvicorn.run(app, host=Config.SERVER_HOST, port=Config.SERVER_PORT)
