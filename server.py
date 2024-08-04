from fastapi import FastAPI, WebSocket
from fastapi.middleware import cors
from fastapi.responses import FileResponse
from utils import WebSocketManager


app = FastAPI()

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connection_manager = WebSocketManager()

@app.websocket("/")
async def websocket_endpoint(websocket : WebSocket):
    await websocket.accept()
    connection_id = connection_manager.add_connection(websocket)
    while True:
        try:
            data = await websocket.receive_text()
            await connection_manager.broadcast_message(connection_id, data)
        except:
            connection_manager.remove_connection(connection_id)
            break

@app.get("/")
async def root():
    return FileResponse("index.html")