# import db.model.models
# import db
#
# def drop_all():
#     db.base_engine.echo=True
#     db.Base.metadata.drop_all(bind=db.base_engine)
#
# if __name__=='__main__':
#     drop_all()

import db.model.models
import db

def drop_fees_table():
    db.base_engine.echo = True
    db.model.models.Academic.__table__.drop(bind=db.base_engine, checkfirst=True)

if __name__ == '__main__':
    drop_fees_table()
