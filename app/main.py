import uvicorn
from fastapi import FastAPI
from fastapi import Request
from starlette.templating import Jinja2Templates

from app.routers.employees import router as employees_router
from app.routers.positions import router as positions_router

app = FastAPI()
app.include_router(employees_router, prefix='/employee')
app.include_router(positions_router, prefix='/position')
templates = Jinja2Templates(directory="templates")


@app.get('/')
async def root():
    return {'message': 'Есть два путя /employee /position'}


@app.get('/error')
async def error(request: Request):
    return templates.TemplateResponse("error.html", {"request": request})


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1',
                port=8080, reload=True, workers=1)
