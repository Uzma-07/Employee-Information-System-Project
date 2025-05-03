#EmpDelete.py<--File Name and Module Name
import pickle
def empdelete():
    emprecords=[]
    try:
        with open("projectemp.data","rb") as fp:
            while(True):
                try:
                    record=pickle.load(fp)
                    emprecords.append(record)
                except EOFError:
                    break
        #-----------------------------
        eno=int(input("Enter Emp Number to Delete:"))
        print(eno)
        res=False
        for recno in range(len(emprecords)):
            if(eno==emprecords[recno][0]):
                delrecno=recno
                res=True
                break
        if(res):
            emprecords.pop(delrecno)
            print("Employee  Record Delete --verify")
            with open("projectemp.data","wb") as fp:
                for record in emprecords:
                    pickle.dump(record,fp)
        else:
            print("Emp Number does not Exist")

    except FileNotFoundError:
        print("File Does Not Exist")
