from uuid import uuid4
import http.client
from urllib import parse
import json


class WebSocketManager:
    connection_pool = {}

    def __init__(self):
        pass

    def add_connection(self,connection):
        uuid = uuid4()
        self.connection_pool[uuid] = {
            "connection": connection,
            "user_details": get_user_details(connection.headers.get('user-agent'))
        }
        return uuid

    async def broadcast_message(self, connection_id, message):
        for id, connection in self.connection_pool.items():
            if id == connection_id:continue
            await connection["connection"].send_json({
                "id": f"{connection_id} - {self.connection_pool[connection_id]['user_details']['os_family']}",
                "message": str(message)
            })
    
    def remove_connection(self, connection_id):
        self.connection_pool.pop(connection_id, None)


def get_user_details(user_agent):
    try:
        conn = http.client.HTTPSConnection('api.apicagent.com')
        conn.request(
            'GET',
            f'/?ua={parse.quote(user_agent)}',
        )
        response = conn.getresponse()
        return json.loads(response.read().decode('utf-8'))
    except:
        return {}