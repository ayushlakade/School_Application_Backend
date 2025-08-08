from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import CourseBase
from app.logger import setup_logging
import logging
from db.services.Course_Service import CourseServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.post("/insert_course_record")
def post_insert_course_record(course:CourseBase,db:Session=Depends(get_db)):
    logger.info("Request Received to insert course record")
    records=CourseServiceManager.insert_course_details(db,course.course_code,course.course_name,course.course_fees,course.course_number_of_student)
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
        raise HTTPException(status_code=500,detail="Error in inserting course Record")