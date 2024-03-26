from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/docs", tags=["Docs"])


@router.get("/scalar")
async def get_docs():
    return HTMLResponse(content=open("src/main/app/routes/docs/index.html", "r").read())
