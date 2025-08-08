from fastapi import APIRouter,HTTPException,Depends
from fastapi.params import Depends
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from db.schemas.schemas import  AcademicBase
from app.logger import setup_logging
import logging
from db.services.Academic_Services import AcademicServiceManager
from db import get_db
setup_logging()
logger=logging.getLogger(__name__)
router=APIRouter()



@router.patch("/update_academic_record_by_academic_id")
def update_balance(academic: AcademicBase, db: Session = Depends(get_db)):
    academic_record = AcademicServiceManager.update_academic_record_by_academic_id(db, academic.academic_id,academic.student_id,
                                                                              academic.course_id,academic.academic_year,
                                                                              academic.grade,academic.remarks,
                                                                              academic.enrollment_date)
    if academic_record:
        return_list = []
        for academic in academic_record:
            data = {}
            data['academic_id'] = academic.academic_id
            data['student_id'] = academic.student_id
            data['course_id'] = academic.course_id
            data['academic_year'] = academic.academic_year
            data['grade'] = academic.grade
            data['remarks'] = academic.remarks
            data['enrollment_date'] = academic.enrollment_date


            return_list.append(data)

        return JSONResponse(
            status_code=200,
            content={"message": return_list}
        )
    else:
        raise HTTPException(status_code=500, detail="Error in updating Academic record  by id")