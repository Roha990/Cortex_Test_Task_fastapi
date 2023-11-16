from app.database.database import SessionLocal, Employee
import re


def add_employee(last_name, first_name, middle_name, position_id, hire_date):
    if re.search(r'[0-9\s\W]', last_name):
        return False
    if re.search(r'[0-9\s\W]', first_name):
        return False
    if re.search(r'[0-9\s\W]', middle_name):
        return False
    db = SessionLocal()
    new_employee = Employee(last_name=last_name, first_name=first_name, middle_name=middle_name, position_id=position_id, hire_date=hire_date)
    db.add(new_employee)
    db.commit()
    db.close()
    return True


def get_employees():
    db = SessionLocal()
    query = db.query(Employee)
    db.close()
    return db.query(Employee)


def get_employee(employee_id):
    db = SessionLocal()
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    db.close()
    if employee is None:
        return False
    return employee


def delete_employee_db(id):
    db = SessionLocal()
    employee = db.query(Employee).filter(Employee.id == id).first()
    db.delete(employee)
    db.commit()
    db.close()
    return True


def update_employee(id, last_name, first_name, middle_name, position_id, hire_date):
    if re.search(r'[0-9\s\W]', last_name):
        return False
    if re.search(r'[0-9\s\W]', first_name):
        return False
    if re.search(r'[0-9\s\W]', middle_name):
        return False
    db = SessionLocal()
    employee = db.query(Employee).filter(Employee.id == id).first()
    employee.last_name = last_name
    employee.first_name = first_name
    employee.middle_name = middle_name
    employee.position_id = position_id
    employee.hire_date = hire_date
    db.commit()
    db.close()
    return True
