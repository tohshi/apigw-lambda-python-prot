from aws_lambda_powertools.event_handler.api_gateway import Router
from controller.todo import TodoController
from service.todo import TodoService


router = Router()

service = TodoService()
controller = TodoController(service)


@router.get("/todos")
def list_todos():
    return controller.list_todos()


@router.get("/todos/<todo_id>")
def get_todo_by_id(todo_id: str):
    return controller.get_todo_by_user_id(todo_id)
