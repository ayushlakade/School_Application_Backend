from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from db.schemas.schemas import UpdateCourse, UpdateCourse2, UpdateCourse3

from app.logger import setup_logging
import logging
from db.services.Course_Service import CourseServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()



@router.patch("/update_course_fees_by_course_code")
def patch_update_course_fees(course:UpdateCourse,db:Session=Depends(get_db)):
    logger.info("Request Received to update course fees")
    records=CourseServiceManager.update_course_fees_by_course_code(db,course.course_code,course.course_fees)

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
        raise HTTPException(status_code=500,detail="Error in updating Student Gmail")



@router.patch("/update_course_name_by_course_code")
def patch_update_course_name(course:UpdateCourse2,db:Session=Depends(get_db)):
    logger.info("Request Received to update course name")
    records=CourseServiceManager.update_course_name_by_course_code(db,course.course_code,course.course_name)
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
        raise HTTPException(status_code=500,detail="Error in updating  course name")




@router.patch("/update_number_of_student_in_course_by_course_code ")
def patch_update_course_names(course:UpdateCourse3,db:Session=Depends(get_db)):
    logger.info("Request Received to update course name")
    records=CourseServiceManager.update_number_of_student_by_course_code(db,course.course_number_of_student,course.course_code)
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
        raise HTTPException(status_code=500,detail="Error in updating  course name")
