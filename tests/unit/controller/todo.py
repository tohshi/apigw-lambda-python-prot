from src.controller.todo import TodoController, TodoService


class MockTodoService(TodoService):
    def __init__(self):
        pass

    def list_todos(self):
        return {"data": [{"id": 1, "title": "hello"}, {"id": 2, "title": "world"}]}

    def get_todo_by_user_id(self, user_id: str):
        return {"id": 1, "title": "hello"}


service = MockTodoService()
controller = TodoController(service)


def test_list_todo():
    response = controller.list_todos()

    assert response == {
        "data": [{"id": 1, "title": "hello"}, {"id": 2, "title": "world"}]
    }
