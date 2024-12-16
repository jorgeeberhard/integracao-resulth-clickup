import requests

class Resulth:
    def __init__(self):
        self.host = "localhost"
        self.port = 5000
        self.url = "http://" +self.host + ":" + str(self.port)

    def get_os(self, os_id):
        try:
            url = f'{self.url}/os'

            params = {
                "id": os_id
            }

            print(url)

            response = requests.get(url, params)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return e
        
        