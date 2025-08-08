from fastapi import APIRouter,HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app.logger import setup_logging
import logging
from db.services.Academic_Services import AcademicServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()

@router.get("/get_all_academic_details")
def get_all_academic_record(db:Session=Depends(get_db)):
    logger.info("Request Received to get all student academic details")
    academic_info=AcademicServiceManager.display_all_academic_details(db)
    return_list=[]

    for student in academic_info:
        academic_data = {}
        academic_data['academic_id']=student.academic_id
        academic_data['student_id']=student.student_id
        academic_data['course_id']=student.course_id
        academic_data['academic_year'] = student.academic_year
        academic_data['grade'] = student.grade
        academic_data['remarks'] = student.remarks
        academic_data['enrollment_date'] = student.enrollment_date

        return_list.append(academic_data)


    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_academic_detail_by_academic_id/{academic_id}")
def get_students_by_id(academic_id:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get student detail by academic id : {0}".format(academic_id))
    academic=AcademicServiceManager.display_academic_details_by_academic_id(db,academic_id)

    return_list = []

    academic_data = {}
    academic_data['academic_id'] = academic.academic_id
    academic_data['student_id'] = academic.student_id
    academic_data['course_id'] = academic.course_id
    academic_data['academic_year'] = academic.academic_year
    academic_data['grade'] = academic.grade
    academic_data['remarks'] = academic.remarks
    academic_data['enrollment_date'] = academic.enrollment_date

    return_list.append(academic_data)

    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_academic_detail_by_students_id/{student_id}")
def get_students_by_id(student_id:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get student by id : {0}".format(student_id))
    academic=AcademicServiceManager.display_academic_details_by_student_id(db,student_id)


    return_list = []
    academic_data = {}
    academic_data['academic_id'] = academic.academic_id
    academic_data['student_id'] = academic.student_id
    academic_data['course_id'] = academic.course_id
    academic_data['academic_year'] = academic.academic_year
    academic_data['grade'] = academic.grade
    academic_data['remarks'] = academic.remarks
    academic_data['enrollment_date'] = academic.enrollment_date

    return_list.append(academic_data)


    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )

@router.get("/get_academic_detail_by_course_id/{course_id}")
def get_students_by_id(course_id:int,db:Session=Depends(get_db)):
    logger.info("Request Received to get student by id : {0}".format(course_id))
    academic=AcademicServiceManager.display_academic_details_by_course_id(db,course_id)


    return_list = []
    academic_data = {}
    academic_data['academic_id'] = academic.academic_id
    academic_data['student_id'] = academic.student_id
    academic_data['course_id'] = academic.course_id
    academic_data['academic_year'] = academic.academic_year
    academic_data['grade'] = academic.grade
    academic_data['remarks'] = academic.remarks
    academic_data['enrollment_date'] = academic.enrollment_date

    return_list.append(academic_data)


    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )


@router.get("/get_academic_detail_by_academic_year/{academic_year}")
def get_students_by_id(academic_year:str,db:Session=Depends(get_db)):
    logger.info("Request Received to get student by id : {0}".format(academic_year))
    academic=AcademicServiceManager.display_academic_details_by_academic_year(db,academic_year)


    return_list = []
    academic_data = {}
    academic_data['academic_id'] = academic.academic_id
    academic_data['student_id'] = academic.student_id
    academic_data['course_id'] = academic.course_id
    academic_data['academic_year'] = academic.academic_year
    academic_data['grade'] = academic.grade
    academic_data['remarks'] = academic.remarks
    academic_data['enrollment_date'] = academic.enrollment_date

    return_list.append(academic_data)


    return JSONResponse(
        status_code=200,
        content={"message":return_list}
    )
