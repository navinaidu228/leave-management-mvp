# leave_management/crud.py

from sqlalchemy.orm import Session
from leave_management import models, schemas
from datetime import date


def create_employee(db: Session, emp: schemas.EmployeeCreate):
    db_emp = models.Employee(
        name=emp.name,
        email=emp.email,
        department=emp.department,
        joining_date=emp.joining_date,
        leave_balance=12  # default leave balance
    )
    db.add(db_emp)
    db.commit()
    db.refresh(db_emp)
    return db_emp


def get_employee(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()


def apply_leave(db: Session, emp_id: int, leave: schemas.LeaveCreate):
    emp = get_employee(db, emp_id)
    if not emp:
        raise ValueError("Employee not found")

    leave_days = (leave.end_date - leave.start_date).days + 1
    if emp.leave_balance < leave_days:
        raise ValueError("Insufficient leave balance")

    db_leave = models.Leave(
        employee_id=emp_id,
        start_date=leave.start_date,
        end_date=leave.end_date,
        status="Pending"
    )
    db.add(db_leave)
    db.commit()
    db.refresh(db_leave)
    return db_leave


def approve_leave(db: Session, leave_id: int, approve: bool):
    leave = db.query(models.Leave).filter(models.Leave.id == leave_id).first()
    if not leave:
        raise ValueError("Leave not found")

    if leave.status != "Pending":
        raise ValueError("Leave already processed")

    if approve:
        leave.status = "Approved"
        emp = get_employee(db, leave.employee_id)
        leave_days = (leave.end_date - leave.start_date).days + 1
        emp.leave_balance -= leave_days
    else:
        leave.status = "Rejected"

    db.commit()
    db.refresh(leave)
    return leave
