from db.model import models as M
from sqlalchemy.orm import Session
from db.schemas.schemas import StudentBase
from db.services.base_Service import BaseSerVice

class CourseServiceManager:
    def display_all_course_details(db: Session):
        q=db.query(M.CourseManager)
        try:
            return q.all()
        except Exception as e:
            return None

    def display_course_details_by_course_name(db: Session,course_name):
        q = db.query(M.CourseManager).filter_by(course_name=course_name).first()
        try:
            return q
        except Exception as e:
            return None

    def display_course_details_by_course_code(db: Session,course_code):
        q = db.query(M.CourseManager).filter_by(course_code=course_code).first()
        try:
            return q
        except Exception as e:
            return None


    def insert_course_details(db:Session,course_code,course_name,course_fees,course_number_of_student):
        try:
            course=M.CourseManager(course_code=course_code,course_name=course_name,course_fees=course_fees,course_number_of_student=course_number_of_student)
            db.add(course)
            db.commit()
            q = db.query(M.CourseManager)
            return q
        except Exception as e:
            return None


    def update_course_fees_by_course_code(db:Session,course_code,course_fees):#by name email get updated
        try:
            course=db.query(M.CourseManager).filter_by(course_code=course_code).first()
            if course:
                course.course_fees=course_fees
                db.commit()
                q = db.query(M.CourseManager)
                return q
            else:
                return {"message":"course code not found"}
        except Exception as e:
            return e

    def update_course_name_by_course_code(db:Session,course_code,course_name):#by name email get updated
        try:
            course=db.query(M.CourseManager).filter_by(course_code=course_code).first()
            if course:
                course.course_name=course_name
                db.commit()
                db.refresh(course)
                q = db.query(M.CourseManager)
                return q
            else:
                return {"message":"course code not found"}
        except Exception as e:
            return e

    def update_number_of_student_by_course_code(db: Session, course_number_of_student, course_code):
        try:
            # Get the course by course_code
            course = db.query(M.CourseManager).filter_by(course_code=course_code).first()
            if course:
                course.course_number_of_student = course_number_of_student
                db.commit()
                db.refresh(course)
                q = db.query(M.CourseManager)# refresh object with latest data from DB
                return q.all()
            else:
                return{"message":"course code not found"}

        except Exception:
            db.rollback()
            raise

    def delete_course_details_by_code(db: Session, course_code):
        try:
            course = db.query(M.CourseManager).filter_by(course_code=course_code).first()
            if course:
                db.delete(course)
                db.commit()
                q = db.query(M.CourseManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None

    def delete_course_details_by_course_name(db: Session, course_name):
        try:
            course = db.query(M.CourseManager).filter_by(course_name=course_name).first()
            if course:
                db.delete(course)
                db.commit()
                q = db.query(M.CourseManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None

    def get_courses_with_fees_greater_than(db: Session, minimum_fee: int):
        try:
            courses = db.query(M.CourseManager).filter(M.CourseManager.course_fees >= minimum_fee).all()
            if courses:
                return courses
            else:
                return []
        except Exception as e:
            return []

    def get_courses_with_fees_less_than(db: Session, minimum_fee: int):
        try:
            courses = db.query(M.CourseManager).filter(M.CourseManager.course_fees <= minimum_fee).all()
            if courses:
                return courses
            else:
                return []
        except Exception as e:
            return []







