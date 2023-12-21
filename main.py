
from uvicorn import run # type: ignore

from api import app

__import__ = [
    app
]

DEBUG = False

if __name__ == '__main__':
    if DEBUG:
        run(app='main:app', 
            reload=True, 
            workers=1)
    else:
        run(app=app,
            host='0.0.0.0',
            port=8080, 
            access_log=False, 
            timeout_keep_alive=60)