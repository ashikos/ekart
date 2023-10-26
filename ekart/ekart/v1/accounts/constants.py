from common.library import ChoiceAdapter


class UserTypes(ChoiceAdapter):
    """ gender type choices"""
    
    User = 101
    Staff = 102
    Admin = 103



class GenderTypes(ChoiceAdapter):
    """ gender type choices"""
    
    Male = 101
    Fenale = 102
    Others = 103