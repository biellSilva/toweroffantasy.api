
from uvicorn import run # type: ignore

from api import app

DEBUG = False

if __name__ == '__main__':
    if DEBUG:
        run(app='main:app', access_log=True, log_level='debug', 
            reload=True, reload_delay=15, workers=1)
    else:
        run(app=app, host='0.0.0.0', port=8080, access_log=False)