from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from db.schemas.schemas import DeleteAcademic,DeleteAcademic2
from app.logger import setup_logging
import logging
from db.services.Academic_Services import AcademicServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()



@router.delete("/delete_academic_record_by_academic_year")
def delete_student_record_name(student:DeleteAcademic,db:Session=Depends(get_db)):
    logger.info("Request Received to delete academics records")
    records=AcademicServiceManager.delete_academic_details_records_by_academic_year_(db,student.academic_year)
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
        raise HTTPException(status_code=500, detail="Error in deleting Student Academic Record")



@router.delete("/delete_academic_record_by_academic_id")
def delete_student_record_name(student:DeleteAcademic2,db:Session=Depends(get_db)):
    logger.info("Request Received to delete academic record")
    records=AcademicServiceManager.delete_academic_details_records_by_academic_id(db,student.academic_id)
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
        raise HTTPException(status_code=500, detail="Error in deleting Student Academic Record")