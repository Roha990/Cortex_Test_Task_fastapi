from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates

from app.config import get_datebase
from app.crud.positions import add_position, get_positions, delete_position_db, update_position, get_position
from app.models.models import Position

router = APIRouter()
datebase = get_datebase()
templates = Jinja2Templates(directory="templates")


@router.get("/get", response_class=HTMLResponse, name='get_positions')
async def return_positions(request: Request):
    positions = get_positions()
    context = {"request": request, "positions": positions}
    return templates.TemplateResponse("positions/get_positions.html", context)


@router.get("/add_form", response_class=HTMLResponse, name='get_form_add_position')
async def return_form_add_position(request: Request):
    return templates.TemplateResponse("positions/add_position.html", {"request": request})


@router.post("/add_form", name='post_form_add_position')
async def post_form_data(request: Request, position_name=Form()):
    if add_position(position_name):
        return RedirectResponse('/position/get', status_code=303)
    else:
        return RedirectResponse('../error', status_code=303)


@router.get("/edit_form/{position_id}", response_class=HTMLResponse, name='get_form_edit_position')
async def return_form_edit_position(request: Request, position_id: int):
    position = get_position(position_id)
    return templates.TemplateResponse("positions/edit_position.html",
                                      {"request": request, 'position': position})


@router.put("/update/{position_id}", name='put_form_edit_position')
async def put_form_edit_position(request: Request, position_id: int, position_name: str = Form(...), ):
    position = get_position(position_id)
    if update_position(position_id, position_name):
        return RedirectResponse('/position/get', status_code=303)
    else:
        return RedirectResponse('../../error', status_code=303)


@router.delete("/delete/{position_id}", name='delete_position')
async def delete_position(position_id: int):
    delete_position_db(position_id)
    return {'message': 'ok'}


