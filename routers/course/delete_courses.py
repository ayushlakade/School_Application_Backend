from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import DeleteCourse,DeleteCourse2
from app.logger import setup_logging
import logging

from db.services.Course_Service import CourseServiceManager
from db.services.Student_Service import StudentServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.delete("/delete_course_record_by_course_code")
def delete_course_record(course:DeleteCourse,db:Session=Depends(get_db)):
    logger.info("Request Received to update student record")
    records=CourseServiceManager.delete_course_details_by_code(db,course.course_code)
    if records:
        return_list = []
        for course in records:
            course_data = {}
            course_data['course_id'] = course.course_id
            course_data['course_code'] = course.course_code
            course_data['course_name'] = course.course_name
            course_data['course_fees'] = course.course_fees
            course_data['course_number_of_student'] = course.course_number_of_student

            return_list.append(course_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500, detail="Error in deleting course ")


@router.delete("/delete_course_record_by_name")
def delete_course_record_by_name(course:DeleteCourse2,db:Session=Depends(get_db)):
    logger.info("Request Received to update student record")
    records=CourseServiceManager.delete_course_details_by_course_name(db,course.course_name)
    if records:
        return_list = []
        for course in records:
            course_data = {}
            course_data['course_id'] = course.course_id
            course_data['course_code'] = course.course_code
            course_data['course_name'] = course.course_name
            course_data['course_fees'] = course.course_fees
            course_data['course_number_of_student'] = course.course_number_of_student

            return_list.append(course_data)

        return JSONResponse(
            status_code=201,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500, detail="Error in deleting course ")


