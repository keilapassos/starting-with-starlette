from starlette.routing import Route
from app.controllers import home_controller, echo_controller


routes = [
    Route("/", endpoint=home_controller.home),
    Route("/echo", endpoint=echo_controller.echo)
]