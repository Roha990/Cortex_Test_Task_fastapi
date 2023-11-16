from fastapi import APIRouter, Depends, Request, Form
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

from app.config import get_datebase
from app.crud.employees import get_employees, add_employee, get_employee, update_employee, delete_employee_db
from app.crud.positions import get_positions

router = APIRouter()
datebase = get_datebase()
templates = Jinja2Templates(directory="templates")


@router.get("/get", response_class=HTMLResponse, name='get_employees')
async def return_employees(request: Request):
    employees = get_employees()
    context = {"request": request, "employees": employees}
    return templates.TemplateResponse("employees/get_employees.html", context)


@router.get("/add_form", response_class=HTMLResponse, name='get_form_add_employee')
async def return_form_add_employee(request: Request):
    positions = get_positions()
    return templates.TemplateResponse("employees/add_employee.html", {"request": request, 'positions': positions})


@router.post("/add_form", name='post_form_add_position')
async def post_form_data(request: Request, last_name=Form(), first_name=Form(), middle_name=Form(), position_id=Form(),
                         hire_date=Form()):
    if add_employee(last_name, first_name, middle_name, position_id, hire_date):
        return RedirectResponse('/employee/get', status_code=303)
    else:
        return RedirectResponse('../error', status_code=303)


@router.get("/edit_form/{employee_id}", response_class=HTMLResponse, name='get_form_edit_employee')
async def return_form_edit_employee(request: Request, employee_id: int):
    employee = get_employee(employee_id)
    positions = get_positions()
    return templates.TemplateResponse("employees/edit_employee.html",
                                      {"request": request, 'employee': employee, 'positions': positions})


@router.put("/update/{employee_id}", name='put_form_edit_employee')
async def put_form_edit_employee(request: Request, employee_id: int, last_name=Form(), first_name=Form(),
                                 middle_name=Form(), position_id=Form(),
                                 hire_date=Form()):
    position = get_employee(employee_id)
    if update_employee(employee_id, last_name, first_name, middle_name, position_id, hire_date):
        return RedirectResponse('/employee/get', status_code=303)
    else:
        return RedirectResponse('../../error', status_code=303)


@router.delete("/delete/{employee_id}", name='delete_employee')
async def delete_employee(employee_id: int):
    delete_employee_db(employee_id)
    return {'message': 'ok'}
