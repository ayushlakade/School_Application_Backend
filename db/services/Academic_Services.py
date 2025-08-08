from db.model import models as M
from sqlalchemy.orm import Session


class AcademicServiceManager:
    def display_all_academic_details(db: Session):
        q=db.query(M.AcademicManager)
        try:
            return q.all()
        except Exception as e:
            return None

    def display_academic_details_by_academic_id(db: Session,academic_id):
        q = db.query(M.AcademicManager).filter_by(academic_id=academic_id).first()
        try:
            return q
        except Exception as e:
            return None

    def display_academic_details_by_student_id(db: Session,student_id):
        q = db.query(M.AcademicManager).filter_by(student_id=student_id).first()
        try:
            return q
        except Exception as e:
            return None

    def display_academic_details_by_course_id(db: Session,course_id):
        q = db.query(M.AcademicManager).filter_by(course_id=course_id).first()
        try:
            return q
        except Exception as e:
            return None

    def display_academic_details_by_academic_year(db: Session,academic_year):
        q = db.query(M.AcademicManager).filter_by(academic_year=academic_year).first()
        try:
            return q
        except Exception as e:
            return None

    def insert_academics_details(db:Session,academic_id,student_id,course_id,academic_year,grade,remarks,enrollment_date):
        try:
            academic=M.AcademicManager(academic_id=academic_id,student_id=student_id,course_id=course_id,academic_year=academic_year,grade=grade,remarks=remarks,enrollment_date=enrollment_date)
            db.add(academic)
            db.commit()
            q = db.query(M.AcademicManager)
            return q
        except Exception as e:
            return None

    def update_academic_record_by_academic_id(db: Session, academic_id,student_id,course_id,academic_year,grade,remarks,enrollment_date):
        try:
            academic_record = db.query(M.AcademicManager).filter_by(academic_id=academic_id).first()
            if academic_record:
                academic_record.student_id=student_id
                academic_record.course_id=course_id
                academic_record.academic_year=academic_year
                academic_record.grade=grade
                academic_record.remarks=remarks
                academic_record.enrollment_date=enrollment_date

                db.commit()
                q = db.query(M.AcademicManager)
                return q.all()

        except Exception:
            db.rollback()
            raise


    def delete_academic_details_records_by_academic_year_(db:Session, academic_year : str):
        try:
            records= db.query(M.AcademicManager).filter(M.AcademicManager.academic_year == academic_year).all()
            if not records:
                return None

            for record in records:
                db.delete(record)

            db.commit()
            return db.query(M.AcademicManager).all()

        except Exception as e:
            db.rollback()
            raise e

    def delete_academic_details_records_by_academic_id(db:Session, academic_id):
        try:
            academic_record=db.query(M.AcademicManager).filter_by(academic_id = academic_id).first()
            if academic_record:
                db.delete(academic_record)
                db.commit()
                q = db.query(M.AcademicManager)
                return q.all()
            else:
                return None
        except Exception as e:
            return None


