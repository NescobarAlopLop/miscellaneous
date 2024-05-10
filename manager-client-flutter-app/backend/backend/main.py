from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()

# This will keep track of all active WebSocket connections
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
async def send_message(message: str):
    # This endpoint receives messages from the master app and broadcasts them to all connected clients
    for connection in connections:
        await connection.send_text(message)
    return {"message": "Message sent to all clients", "data": message}


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
