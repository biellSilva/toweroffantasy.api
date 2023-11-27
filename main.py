
from uvicorn import run # type: ignore

from api import app

__import__ = [
    app
]

DEBUG = True

if __name__ == '__main__':
    if DEBUG:
        run(app=app)
    else:
        run(app='main:app', host='0.0.0.0', port=8080, workers=1)