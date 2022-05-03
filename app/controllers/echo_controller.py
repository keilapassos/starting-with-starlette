from starlette.responses import PlainTextResponse


def echo(request):
    return PlainTextResponse("Echo page")