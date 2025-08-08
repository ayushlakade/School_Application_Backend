from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from app.logger import setup_logging
import logging
from db.services.Course_Service import CourseServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.get("/get_all_course_details")
def get_all_students(db:Session=Depends(get_db)):
    logger.info("Request Received to get all course info")
    course_info=CourseServiceManager.display_all_course_details(db)
    return_list=[]

    for course in course_info:
        course_data = {}
        course_data['course_id']=course.course_id
        course_data['course_code']=course.course_code
        course_data['course_name']=course.course_name
        course_data['course_fees'] = course.course_fees
        course_data['course_number_of_student'] = course.course_number_of_student
        return_list.append(course_data)


    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_course_details_by_name/{course_name}")
def get_students_by_id(course_name:str,db:Session=Depends(get_db)):
    logger.info("Request Received to get course details by name : {0}".format(course_name))
    course_info=CourseServiceManager.display_course_details_by_course_name(db,course_name)

    return_list = []
    # for course in course_info:

    course_data = {}
    course_data['course_id'] = course_info.course_id
    course_data['course_code'] = course_info.course_code
    course_data['course_name'] = course_info.course_name
    course_data['course_fees'] = course_info.course_fees
    course_data['course_number_of_student'] = course_info.course_number_of_student
    return_list.append(course_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_course_details_by_course_code/{course_code}")
def get_courses_by_fees(course_code:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get course details by course code : {0}".format(course_code))
    course_info=CourseServiceManager.display_course_details_by_course_code(db,course_code)

    return_list = []
    # for course in course_info:
    course_data = {}
    course_data['course_id'] = course_info.course_id
    course_data['course_code'] = course_info.course_code
    course_data['course_name'] = course_info.course_name
    course_data['course_fees'] = course_info.course_fees
    course_data['course_number_of_student'] = course_info.course_number_of_student
    return_list.append(course_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_courses_greater_than_fees/{minimum_fee}")
def get_courses_by_minimum_fee(minimum_fee: int, db: Session = Depends(get_db)):
    logger.info("Request Received to get course sort by course_fees : {0}".format(minimum_fee))
    course_info = CourseServiceManager.get_courses_with_fees_greater_than(db, minimum_fee)
    return_list = []
    for course in course_info:
        course_data = {}
        course_data['course_id'] = course.course_id
        course_data['course_code'] = course.course_code
        course_data['course_name'] = course.course_name
        course_data['course_fees'] = course.course_fees
        course_data['course_number_of_student'] = course.course_number_of_student
        return_list.append(course_data)

    return JSONResponse(
        status_code=200,
        content={"message": return_list}
    )


@router.get("/get_courses_less_than_fees/{minimum_fee}")
def get_courses_by_minimum_fee(minimum_fee: int, db: Session = Depends(get_db)):
    logger.info("Request Received to get course sort by course_fees : {0}".format(minimum_fee))
    course_info = CourseServiceManager.get_courses_with_fees_less_than(db, minimum_fee)
    return_list = []
    for course in course_info:
        course_data = {}
        course_data['course_id'] = course.course_id
        course_data['course_code'] = course.course_code
        course_data['course_name'] = course.course_name
        course_data['course_fees'] = course.course_fees
        course_data['course_number_of_student'] = course.course_number_of_student
        return_list.append(course_data)

    return JSONResponse(
        status_code=200,
        content={"message": return_list}
    )