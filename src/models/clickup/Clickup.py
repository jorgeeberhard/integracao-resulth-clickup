import requests

class Clickup:
    def __init__(self):
        self.list_id = "901306061918"
        self.authorization_token = "pk_44292168_6C9TVCULO8ZGN27OOVQ8H6IRRHZZ0X93"
        self.url_task = f'https://api.clickup.com/api/v2/list/{self.list_id}/task'
        self.default_assignee = 44292168
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": self.authorization_token,
        }

    def create_task(self, task_object):
        
        if type(task_object) is not dict:
            raise TypeError("Type needs to be a Dictionary")

        response = requests.post(self.url_task, headers=self.headers, json=task_object)

        return response
    
    def update_task(self, task_object):
        
        if type(task_object) is not dict:
            raise TypeError("Type needs to be a Dictionary")
        
        task_id = task_object.get("task_id")
        
        if not task_id is None:
            raise ValueError("The task_id cant be None")
        
        response = requests.post(self.url_task, headers=self.headers, json=task_object)
        return response
    
    def create_comment(self, task_id, comment_text):

        url = f'https://api.clickup.com/api/v2/task/{task_id}/comment'

        params = {
            "comment_text": comment_text,
            "assignee": self.default_assignee,
            "notify_all": False
        }

        response = requests.post(url, headers=self.headers, json=params)
        return response
    
    def udpate_comment(self, comment_id, comment_text):
        
        url = f'https://api.clickup.com/api/v2/comment/{comment_id}'

        params = {
            "comment_text": comment_text,
            "assignee": self.default_assignee,
            "notify_all": False
        }

        response = requests.put(url, headers=self.headers, json=params)
        return response
