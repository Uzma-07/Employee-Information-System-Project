#EmpExcept.py<----File Name and Module Name
class InvalidNameError(Exception):pass
class SpaceError(BaseException):pass
class ZeroNameLengthError(Exception):pass
#---------------------------------------------------
def validation(name): # name=Guido Va2n Rossum
    if(len(name)==0):
        raise ZeroNameLengthError
    else:
        words=name.split() # words=['Guido','Van','Rossum']
        if(len(words)==0):
            raise SpaceError
        else:
            res=True
            for word in words:
                if(not word.isalpha()):
                    res=False
                    break
            if(res):
                return name
            else:
                raise InvalidNameError
#----------------------------------------------------------------------
import pickle
def checkforunique(eno):
    emprecord=[]
    with open("projectemp.data","rb") as fp:
        while(True):
            try:
                record=pickle.load(fp)
                emprecord.append(record)
            except EOFError:
                break
    res=True
    for record in emprecord:
        if(eno==record[0]):
            res=False
            break
    return res


