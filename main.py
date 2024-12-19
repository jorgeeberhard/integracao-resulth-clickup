import requests, json
from src.models.resulth import Resulth
from src.models.clickup import Clickup
from src.models.database import DataBase
import json

from src.controller.TaskManager import TaskManager

clickup = Clickup()
resulth = Resulth()

task = {
            "name": "task manager",
            "description": "Descrição de teste",
            "tags": ["GANESA"]
        }

task_manager = TaskManager()
task_manager.add_task("Clickup", "create_task", [task])
task_manager.add_task("Clickup", "create_comment", ["86a5z4nzn", "comentario de teste task manager"])
task_manager.process_tasks()

# serialized_params = json.dumps(task)
# print(serialized_params)
# deserialized_params = json.loads(*serialized_params)
# print(deserialized_params)