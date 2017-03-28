from wtforms.validators import ValidationError

class Unique(object):

    def __init__(self,  message=u'Name is missing "_TN"'):
        self.tname = tname
 

    def __call__(self, tname):
        if '_TN' not in tname:
            check = False

        if not check:
            raise ValidationError(self.message)


