from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import StudentBase,StaffBase
from app.logger import setup_logging
import logging
from db.services.Staff_Services import StaffServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.post("/insert_staff_record")
def post_insert_staff_record(student:StaffBase,db:Session=Depends(get_db)):
    logger.info("Request Received to insert student record")
    records=StaffServiceManager.insert_staff_details(db,student.staff_name,student.staff_email,student.staff_designation,student.staff_salary,student.staff_mobile_no)
    if records:
        return_list = []
        for student in records:
            student_data = {}
            student_data['staff_id'] = student.staff_id
            student_data['staff_name'] = student.staff_name
            student_data['staff_email'] = student.staff_email
            student_data['staff_designation'] = student.staff_designation
            student_data['staff_salary'] = student.staff_salary
            student_data['staff_mobile_no'] = student.staff_mobile_no
            return_list.append(student_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500,detail="Error in inserting Student Record")



