# import Part
from typing import Union

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os


# BackEnd Part
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/images/{image_id}")
async def get_image(image_id: str):
    image_path = "images/"+image_id+".png"
    return FileResponse(image_path)
    
@app.post("/uploadfile")
async def create_upload_file(file: UploadFile=File(...)):
    os.chdir("./images")
    contents = await file.read()
    with open(file.filename, "wb") as fp:
    	fp.write(contents)
    print(file.filename)
    os.chdir("..")
    return {"filename": file.filename}
