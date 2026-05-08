from fastapi import Depends, FastAPI, HTTPException, File, UploadFile, BackgroundTasks, WebSocket

from fastapi_p.models import Item

app = FastAPI()


@app.get("/")
def root():
    return {"hello": "world"}


@app.post("/items/")
def create_items(item: Item):
    return item


@app.put("/items/{id}")
def update_item(id: int):
    return {"id": id}


@app.get("/async")
async def async_func():
    return {"message": "async response"}


def common():
    return {"user": "admin"}


@app.get("/secure")
def secure(data=Depends(common)):
    return data


@app.get("/get_error")
def error():
    raise HTTPException(status_code=404, detail="Not Found")


@app.post("/upload")
def file_upload(file: UploadFile = File(...)):
    return {"filename": file.filename}


@app.middleware("http")
async def middleware(request, call_next):
    response = await call_next(request)
    return response


def task():
    print("Running...")


@app.get("/")
def background_task(bg: BackgroundTasks):
    bg.add_task(task)
    return {"message": "task started"}


@app.websocket("/ws")
async def websocket(ws: WebSocket):
    await ws.accept()
    await ws.send_text("Hello")
