from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import DeleteStudentBase4,DeleteStudentBase
from app.logger import setup_logging
import logging
from db.services.Student_Service import StudentServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.delete("/delete_student_record_by_email_id")
def delete_update_student_record(student:DeleteStudentBase,db:Session=Depends(get_db)):
    logger.info("Request Received to update student record")
    records=StudentServiceManager.delete_student_details_by_email_id(db,student.student_email)
    if records:
        return_list = []
        for student in records:
            student_data = {}
            student_data['student_id'] = student.student_id
            student_data['student_name'] = student.student_name
            student_data['student_email'] = student.student_email
            return_list.append(student_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500,detail="Error in Deleting Student Record")


@router.delete("/delete_student_record_by_name")
def delete_student_record_by_name(student:DeleteStudentBase4,db:Session=Depends(get_db)):
    logger.info("Request Received to delete student record")
    record=StudentServiceManager.delete_student_details_by_name(db,student.student_name)
    if record:
        return_list = []
        for student in record:
            student_data = {}
            student_data['student_id'] = student.student_id
            student_data['student_name'] = student.student_name
            student_data['student_email'] = student.student_email
            return_list.append(student_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500,detail="Error in Deleting Student Record")


