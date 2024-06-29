from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayHttpResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from .router.todo import router as TodoRouter

logger = Logger()
app = APIGatewayHttpResolver()
app.include_router(TodoRouter)


@app.get("/todos")
def get_todos():
    return {"todos": {"a"}}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
