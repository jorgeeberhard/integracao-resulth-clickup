from src.models.clickup import Clickup
from src.models.database import DataBase
from operator import itemgetter
import json, time, threading, logging

logging.basicConfig(level=logging.INFO)

class TaskManager:
    def __init__(self):
        self.database = DataBase()
        self.__create_table()

    def __create_table(self):
        query = {
            "sql": """
                    CREATE TABLE IF NOT EXISTS queue_tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        class_name TEXT NOT NULL,
                        method_name TEXT NOT NULL,
                        params TEXT NOT NULL,
                        status TEXT DEFAULT 'pending',
                        created_at TIMESTAMP DEFAULT (DATETIME('now'))
                    );
                """
        }
        self.database.query(query)

    def add_task(self, class_name, method_name, params):

        if not isinstance(params, list):
            raise TypeError("Params must be a List")

        sql = {
            "sql": "INSERT INTO queue_tasks (class_name, method_name, params) VALUES (?, ?, ?)",
            "params": [class_name, method_name, json.dumps(params)]
        }


        self.database.query(sql)
        logging.info(f'Task added: {class_name}.{method_name}({params})')

    def process_tasks(self):
        while True:

            sql = {
                "sql": "SELECT * FROM queue_tasks WHERE status = 'pending' ORDER BY id LIMIT 1"
            }
            

            response = self.database.query(sql)
            if not len(response) > 0:
                logging.info("No task in the queue. Waiting...")
                time.sleep(5)
                continue
            
            task_id, class_name, method_name, params, status, created_at = itemgetter("id", "class_name", "method_name", "params", "status","created_at")(response[0])

            try:
                logging.info(f'Processing task {task_id}: {class_name}.{method_name}({params})')

                # Instanciate the class and starts the method
                class_instance = globals()[class_name]()
                class_method = getattr(class_instance, method_name)
                deserialized_params = json.loads(params)
                class_method(*deserialized_params)

                # Mark the task as completed
                query = {
                    "sql": "UPDATE queue_tasks SET status = 'completed' WHERE id = ?",
                    "params": [task_id]
                }
                self.database.query(query)
                logging.info(f'Task {task_id} completed.\n')
            except Exception as e:
                logging.error(f'Error processing task {task_id}: {e}')

                # Mark the task as failed
                query = {
                    "sql": "UPDATE queue_tasks SET status = 'failed' WHERE id = ?",
                    "params": [task_id]
                }
                self.database.query(query)

    def start(self):

        # Create process_tasks thread
        process_task_thread = threading.Thread(target=self.process_tasks)

        # Start process_tasks thread
        process_task_thread.start()
        return process_task_thread