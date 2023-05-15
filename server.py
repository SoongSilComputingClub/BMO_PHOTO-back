# import Part
from typing import Union
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

import os



# BackEnd Part
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/sourceimage/{image_id}")
async def get_image(request: Request, image_id: str):
    image_path = "images/"+image_id+".png"
    return FileResponse(image_path)

@app.get("/images/{image_id}", response_class=HTMLResponse)
async def get_image(request: Request, image_id: str):
    return templates.TemplateResponse("index.html", {"request": request, "image_id": image_id})
    
@app.post("/uploadfile")
async def create_upload_file(file: UploadFile=File(...)):
    os.chdir("./images")
    contents = await file.read()
    with open(file.filename, "wb") as fp:
    	fp.write(contents)
    print(file.filename)
    os.chdir("../")
    return {"filename": file.filename}
