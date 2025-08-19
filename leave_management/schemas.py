from pydantic import BaseModel
from datetime import date

# ---------------- Employee Schemas ----------------
class EmployeeBase(BaseModel):
    name: str
    email: str

class EmployeeCreate(EmployeeBase):
    pass

class Employee(EmployeeBase):
    id: int

    class Config:
        from_attributes = True


# ---------------- Leave Schemas ----------------
class LeaveBase(BaseModel):
    start_date: date
    end_date: date
    reason: str

class LeaveCreate(LeaveBase):
    pass

class Leave(LeaveBase):
    id: int
    employee_id: int

    class Config:
        from_attributes = True
