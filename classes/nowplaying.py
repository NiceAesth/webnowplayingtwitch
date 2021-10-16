import asyncio, websockets, logging
from asyncio.tasks import current_task

class WebsocketServer:

    def __init__(self) -> None:
        self.version = "0.5.0.0"
        self.player_type = ""
        self.current_track_data = dict()

    def get_current_data(self) -> str:
        """Returns the current track data as a humanly-readable string."""
        try:
            return f"{self.current_track_data['artist']} - {self.current_track_data['title']} ({self.current_track_data['player']})"
        except KeyError:
            return "Nothing."

    def data_handler(self, data) -> None:
        """Handles the data received from the extension."""
        data_list = data.split(':')
        if data_list[0] == "PLAYER":
            self.current_track_data['player'] = data_list[1]
        elif data_list[0] == "STATE":
            self.current_track_data['state'] = data_list[1]        
        elif data_list[0] == "TITLE":
            self.current_track_data['title'] = data_list[1]
        elif data_list[0] == "ARTIST":
            self.current_track_data['artist'] = data_list[1]
        elif data_list[0] == "ALBUM":
            self.current_track_data['album'] = data_list[1]
        elif data_list[0] == "COVER":
            self.current_track_data['cover_url'] = ''.join(data_list[1:])
        elif data_list[0] == "DURATION":
            self.current_track_data['duration'] = ':'.join(data_list[1:])
        elif data_list[0] == "POSITION":
            self.current_track_data['position'] = ':'.join(data_list[1:])
        elif data_list[0] == "VOLUME":
            self.current_track_data['volume'] = data_list[1]
        elif data_list[0] == "RATING":
            self.current_track_data['rating'] = data_list[1]
        elif data_list[0] == "REPEAT":
            self.current_track_data['repeat'] = data_list[1]
        elif data_list[0] == "SHUFFLE":
            self.current_track_data['shuffle'] = data_list[1]

    async def conn_handler(self, websocket, path) -> None:
        """Handles connections from the WebNowPlayingCompanion extension."""
        await websocket.send(f"VERSION:{self.version}")
        logging.info("Received connection from browser.")
        while True:
            data = await websocket.recv()
            self.data_handler(data)

    async def main(self) -> None:
        """Main server loop."""
        async with websockets.serve(self.conn_handler, "localhost", 8974):
            await asyncio.Future()  # run forever