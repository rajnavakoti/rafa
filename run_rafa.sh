#!/bin/bash
poetry run python3 rafa/websocket/websocket_server.py &
poetry run python3 rafa/intermediary_server/http_websocket_bridge.py &
poetry run streamlit run rafa/streamlit_app/friday.py