#EmpSelect.py<----File name and Module Name
import pickle
def singleempdet():
    try:
        with open("projectemp.data","rb") as fp:
            try:
                empno=int(input("Enter Emp Number to view Deatils:"))
                res=False
                while(True):
                    try:
                        record=pickle.load(fp)
                        if(empno==record[0]):
                            rec=record
                            res=True
                            break
                    except EOFError:
                        break
                if(res):
                    print("-" * 50)
                    print("\tSingle Employee Deatils")
                    print("-"*50)
                    print("\tEmployee Number={}".format(rec[0]))
                    print("\tEmployee Name={}".format(rec[1]))
                    print("\tEmployee Salary={}".format(rec[2]))
                    print("-" * 50)
                else:
                    print("\tEmployee Number {} Does not Exist".format(empno))
            except ValueError:
                print("\tInvalid Employee Number:")
    except FileNotFoundError:
        print("File Does not Exist")

def allempdet():
    with open("projectemp.data","rb") as fp:
        print("-"*50)
        print("\tEmpNO\tEmpName\t\tEmpSal")
        print("-" * 50)
        while(True):
            try:
                record=pickle.load(fp)
                for val in record:
                    print("\t{}".format(val),end="\t")
                print()
            except EOFError:
                print("-" * 50)
                break

