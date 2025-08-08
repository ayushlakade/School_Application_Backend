import  logging

class BaseSerVice(object):
    def __init__(self,session):
        self.session=session
        self.logger=logging.getLogger('tornado.application')