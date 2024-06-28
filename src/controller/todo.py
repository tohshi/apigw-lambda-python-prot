from abc import ABC, abstractmethod


class TodoService(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def list_todos(self) -> dict:
        pass

    @abstractmethod
    def get_todo_by_user_id(self, user_id: str) -> dict:
        pass


class TodoController:
    def __init__(self, user_service: TodoService):
        self.service = user_service

    def list_todos(self):
        return self.service.list_todos()

    def get_todo_by_user_id(self, user_id: str):
        return self.service.get_todo_by_user_id(user_id)
