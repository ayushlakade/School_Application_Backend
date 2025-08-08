from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import AcademicBase
from app.logger import setup_logging
import logging
from db.services.Academic_Services import AcademicServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

#only 3 course id available

@router.post("/insert_student_academic_record")
def post_insert_student_record(student:AcademicBase,db:Session=Depends(get_db)):
    logger.info("Request Received to insert student academic record")
    records=AcademicServiceManager.insert_academics_details(db,student.academic_id,student.student_id,student.course_id,student.academic_year,student.grade,student.remarks,student.enrollment_date)
    if records:
        return_list = []
        for student in records:
            student_data = {}
            student_data['academic_id'] = student.academic_id
            student_data['student_id'] = student.student_id
            student_data['course_id'] = student.course_id
            student_data['academic_year'] = student.academic_year
            student_data['grade'] = student.grade
            student_data['remarks'] = student.remarks
            student_data['enrollment_date'] = student.enrollment_date

            return_list.append(student_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500,detail="Error in inserting Student Academic Record")