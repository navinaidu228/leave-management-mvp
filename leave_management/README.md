# Mini Leave Management System (MVP)

## Setup
1. Clone or unzip the project
2. Create virtual environment
   python -m venv .venv
   source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
3. Install dependencies
   pip install -r requirements.txt
4. Run
   uvicorn app.main:app --reload
5. Open Swagger UI at http://127.0.0.1:8000/docs
6. Use the Mini Leave Management System (MVP) 
## API Endpoints
- POST /employees → Add employee
- GET /employees/{id}/leave-balance → Fetch balance
- POST /employees/{id}/apply-leave → Apply leave
- POST /leaves/{id}/approve?approve=true/false → Approve or reject

## Edge Cases
- Leave before joining date
- End date before start date
- Overlapping leave
- Applying more days than available
- Employee not found
- Approval when insufficient balance

## Improvements
- Authentication (HR/Admin vs Employee roles)
- Email notifications
- Carry-forward leave
- Reporting dashboard
- Deployment on Render/Heroku
- FastAPI + SQLAlchemy + SQLite

## How to run locally
```bash
uvicorn leave_management.main:app --reload
