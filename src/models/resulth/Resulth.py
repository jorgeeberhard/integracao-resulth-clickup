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

            response = requests.get(url, params)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return e
        
    def get_ocorrencia(self, os_id):
        try:
            url = f'{self.url}/ocorrencia'

            params = {
                "id": os_id
            }

            response = requests.get(url, params)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return e
        
    def get_log(self, log_id):
        try:
            url = f'{self.url}/log'

            params = {
                "id": log_id
            }

            response = requests.get(url, params)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return e    
        

    def get_causa(self, os_id):
        try:
            url = f'{self.url}/causa'

            params = {
                "id": os_id
            }

            response = requests.get(url, params)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return e
        
    def get_defeito(self, os_id):
        try:
            url = f'{self.url}/defeito'

            params = {
                "id": os_id
            }

            response = requests.get(url, params)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return e
        
    def get_equipamento(self, os_id):
        try:
            url = f'{self.url}/equipamento'

            params = {
                "id": os_id
            }

            response = requests.get(url, params)
            return response
        except Exception as e:
            print(f'Error: {e}')
            return e