#EmpSearch.py<----File Name and Module Name
import pickle
def empsearch():
    try:
        with open("projectemp.data","rb") as fp:
            try:
                empno=int(input("Enter Emp Number to Search:"))
                res=False
                while(True):
                    try:
                        record=pickle.load(fp)
                        if(empno==record[0]):
                            res=True
                            break
                    except EOFError:
                        break
                if(res):
                    print("\tEmployee Number {} Exist--valid emp".format(empno))
                else:
                    print("\tEmployee Number {} Does not Exist--Invalid emp".format(empno))
            except ValueError:
                print("\tInvalid Employee Number:")
    except FileNotFoundError:
        print("File Does not Exist")