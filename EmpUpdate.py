#EmpUpdate.py<-----File Name and Module name
import  pickle
def empupdate():
    emprecords=list()
    try:
        with open("projectemp.data","rb") as fp:
            while(True):
                try:
                    record=pickle.load(fp)
                    emprecords.append(record)
                except EOFError:
                    break
        #Update Code
        res=False
        empno = int(input("Enter Emp Number for Updating Name and Salary:"))
        for recno in range(len(emprecords)):
            if(emprecords[recno][0]==empno):
                rno=recno
                res=True
                break
        if(res):
            empname=input("Enter Employee New Name for Update:")
            empsal=float(input("Enter Employee New Salary for Update:"))
            emprecords[rno][1]=empname
            emprecords[rno][2]=empsal
            with open("projectemp.data","wb") as fp:
                for record in emprecords:
                    pickle.dump(record,fp)
            print("\tEmp Record {} Updated--verify".format(empno))
        else:
            print("\tEmployee Number {} Does Not Exist--Not Possible to Update".format(empno))
    except FileNotFoundError:
        print("File Does not Exist")
