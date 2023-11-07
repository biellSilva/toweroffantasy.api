
from uvicorn import run # type: ignore

from api import app

if __name__ == '__main__':
    run(app=app, 
        access_log=False, 
        host='0.0.0.0',
        port=8080,
        # reload=True,      # dev function
        # reload_delay=5,   # dev function
        # workers=1         # dev function
        )