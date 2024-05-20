import asyncio
from threading import Thread

from src.storage import Storage
from src.parse import parse_DAL
from src.config import Config
from src.app_logging import logger
from src.lockers import lock_rw_storage


def bind_loop(func, *args, **kwargs):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(func(*args, **kwargs))
    loop.close()


async def update_local_db():
    while True:
        logger.info("Start updating local DB...")
        plates = parse_DAL.get_license_plates()
        with lock_rw_storage.w_locked():
            Storage.clear()
            for plate in plates:
                Storage.setItem(plate, plate)
        logger.info("Local DB successfully updated")
        await asyncio.sleep(Config.PARSE_TIMEOUT)


def init_daemons():
    Thread(
        target = bind_loop, 
        daemon = True, 
        kwargs = {"func": update_local_db}
    ).start()
    