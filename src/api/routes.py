from fastapi import APIRouter, UploadFile, File, HTTPException
from dtklp_wrapper import ImageEngine, Lib

from src.storage import Storage
from src.config import Config
from src.api.schemas import RecognizedPlatesList
from src.lockers import lock_rw_storage


router = APIRouter()


@router.post(
    "/recognize/",
    response_model=RecognizedPlatesList
)
async def recognize_plate(
        image: UploadFile = File(...),
):
    img_bytes = bytearray(await image.read())
    lib = Lib(Config.DTKLP_LIB_PATH, Config.DTKLP_BUFFER_SIZE)
    engine = ImageEngine(lib)
    with engine:
        if not engine.is_licensed() and not engine.activate(Config.DTKLP_KEY):
            raise HTTPException(503, "DTKLPR Engine is't licensed")
        result = engine.process(img_bytes)
        
        find_list = []
        with lock_rw_storage.r_locked():
            for plate in result["plates"]:
                item = Storage.getItem(plate["text"])
                if item:
                    find_list.append(item)
        response = RecognizedPlatesList(len(find_list), find_list)

    return response