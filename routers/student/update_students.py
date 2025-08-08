from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import StudentBase
from app.logger import setup_logging
import logging
from db.services.Student_Service import StudentServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()



@router.patch("/update_student_email_id_by_name")
def patch_update_student_record(student:StudentBase,db:Session=Depends(get_db)):
    logger.info("Request Received to update student email id")
    records=StudentServiceManager.update_student_email_by_name(db,student.student_name,student.student_email)
    if records:
        return_list = []
        for student in records:
            student_data = {}
            student_data['student_id'] = student.student_id
            student_data['student_name'] = student.student_name
            student_data['student_email'] = student.student_email
            return_list.append(student_data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500,detail="Error in updating Student Gmail")

@router.patch("/update_student_name_by_email_id")
def patch_update_student_name(student: StudentBase, db: Session = Depends(get_db)):
    try:
        updated_student = StudentServiceManager.update_student_name(db, student.student_email, student.student_name)
        if not updated_student:
            raise HTTPException(status_code=404, detail="Student not found")
        return {
            "student_id": updated_student.student_id,
            "student_name": updated_student.student_name,
            "student_email": updated_student.student_email,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating student name: {e}")
