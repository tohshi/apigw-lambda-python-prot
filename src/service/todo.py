from controller.todo import TodoService as ITodoService


class TodoService(ITodoService):
    def __init__(self):
        pass

    def list_todos(self):
        return {}

    def get_todo_by_user_id(self, user_id: str):
        return {}
