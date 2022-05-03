from starlette.responses import JSONResponse


def home(request):
    return JSONResponse({"msg": "welcome to home page"})