#EmpAdd.py<-----File Name and Module Name
import pickle
from EmpExcept import InvalidNameError,SpaceError,ZeroNameLengthError,validation,checkforunique
def empadd():
    with open("projectemp.data","ab") as fp:
        while(True):
            try:
                # Accept Employee Data
                print("------------------------------------")
                empno=int(input("Enter Employee Number:"))
                empname=validation(input("Enter Employee Name:"))
                empsal =float(input("Enter Employee Salary:"))
                print("------------------------------------")
                #Create empty list and append all emp values
                emplist=[]
                emplist.append(empno)
                emplist.append(empname)
                emplist.append(empsal)
                #Save emplist data to the File by using dump()
                res=checkforunique(empno) # Function Call
                if(res): # if res contains True
                    pickle.dump(emplist,fp)
                    print("\tEmployee Record Saved in a File Successfully..")
                else:
                    print("\tEmployee Number {} already exist--try with Uniue Value".format(empno))
                ch=input("Do u want to Add another Employee Record(yes/no):")
                if(ch.lower()=="no"):
                    break
            except ValueError:
                print("\tDon't Enter Alnums,strs and symbols for empno and salary--try again")
            except InvalidNameError:
                print("\tInvalid Name-try agian")
            except SpaceError:
                print("\tDon't Enter Space for Ur Name--try again")
            except ZeroNameLengthError:
                print("\tU Must Enter Ur Name--try again:")
