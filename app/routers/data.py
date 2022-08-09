from fastapi.responses import FileResponse
from fastapi import APIRouter
from fastapi import File, UploadFile
from fastapi.responses import HTMLResponse

import random
import os
from starlette.responses import StreamingResponse
from datetime import datetime
from typing import List


router = APIRouter()


def iter_file(path: str):
    with open(path, mode="rb") as file_like:
        yield from file_like


@router.get("/static-data/streaming-response/{filename}")
async def get_streaming_response(filename: str) -> StreamingResponse:
    return StreamingResponse(
        iter_file("../p1_data/static_data/" + filename)
    )


@router.get("/static-data/file-response/{filename}")
async def get_file_response(filename: str) -> FileResponse:
    return FileResponse(
        path="../p1_data/static_data/" + filename
    )

@router.post(path="/uploadImages")
async def extract_data_from_images(images: List[UploadFile] = File(...)):
    return f"Name: {images[0].filename}, now: {datetime.now()}"


# @router.get("/records/{record_filename}")
# async def get_record_by_file(record_filename: str):
#     return FileResponse(
#         # TODO: Implement clean_filename. Its still a placeholder function
#         "./data/records/" + clean_filename(record_filename)
#     )


# @router.get("/dummies-records/{record_filename}")
# async def get_dummies_record_by_random(record_filename: str):
#     """ Return a random audio file ("mp3", "wav") in short_audio_samples folder.
#     Don't care about record_filename """
#     listdir = os.listdir("./data/short_audio_samples/")
#     listfiles = [item for item in listdir if item.split(".")[-1] in ["mp3", "wav"]]
#     random_file = random.choice(listfiles)
#     # print(listfiles)
#     return FileResponse(
#         "./data/short_audio_samples/" + random_file
#     )


# @router.get("/record-or-dummy/{record_filename}")
# async def get_record_by_filename_or_random_dummy(record_filename: str):
#     """ Return filename, or a random audio file ("mp3", "wav") in short_audio_samples folder. """
#     if os.path.isfile("./data/records/" + record_filename):
#         return FileResponse("./data/records/" + record_filename)

#     """ No file found. Return random file """
#     listdir = os.listdir("./data/short_audio_samples/")
#     listfiles = [item for item in listdir if item.split(".")[-1] in ["mp3", "wav"]]
#     random_file = random.choice(listfiles)
#     # print(listfiles)
#     return FileResponse("./data/short_audio_samples/" + random_file)