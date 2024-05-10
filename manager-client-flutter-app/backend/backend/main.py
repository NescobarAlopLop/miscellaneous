from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel


class Message(BaseModel):
    message: str


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connections: List[WebSocket] = []


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            for connection in connections:
                if connection != websocket:
                    await connection.send_text(f"Message: {data}")
    except WebSocketDisconnect:
        connections.remove(websocket)


@app.post("/send/")
async def send_message(message: Message):
    for connection in connections:
        await connection.send_text(message.message)
    return {"message": "Message sent to all clients", "data": message.message}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
