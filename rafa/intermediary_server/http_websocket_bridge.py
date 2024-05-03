import logging
import os
from aiohttp import web, ClientSession, ClientTimeout
from dotenv import load_dotenv

# Load and setup environment variables from .env file
load_dotenv()
IS_DOCKER = os.environ.get("IS_DOCKER")
WEBSOCKET_SERVER = os.environ.get("DOCKER_WEBSOCKET_SERVER") if IS_DOCKER else os.environ.get("LOCAL_WEBSOCKET_SERVER")
INTERMEDIATE_SERVER_PORT = os.environ.get("DOCKER_INTERMEDIATE_PORT") if IS_DOCKER else os.environ.get("LOCAL_INTERMEDIATE_PORT")

async def handle_query(request):
    data = await request.json()

    timeout = ClientTimeout(total=300)
    async with ClientSession(timeout=timeout) as session:
        try:
            async with session.ws_connect(WEBSOCKET_SERVER) as ws:
                await ws.send_json(data)
                msg = await ws.receive()
                return web.json_response({'response': msg.data})
        except Exception as e:
            logging.error(f"WebSocket connection error: {e}")
            return web.json_response({'error': 'WebSocket connection error'})

app = web.Application()
app.add_routes([web.post('/query', handle_query)])

web.run_app(app, port=int(INTERMEDIATE_SERVER_PORT))
