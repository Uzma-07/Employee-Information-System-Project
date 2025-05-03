#EmpMainProject.py<----Main Program
from EmpAdd import empadd
from EmpDelete import empdelete
from EmpMenu import menu
from EmpSearch import empsearch
from EmpUpdate import empupdate
from EmpSelect import singleempdet, allempdet

while(True) :
    menu ()
    try:
        ch=int(input("Enter UR Choice:"))
        match (ch) :
            case 1 :
                empadd()
            case 2 :
                empdelete()
            case 3 :
                empsearch()
            case 4 :
                empupdate()
            case 5 :
                singleempdet()
            case 6 :
                allempdet()
            case 7 :
                print("Thx for using Project")
                break
            case _:
                print("\t UR selection of operation is Wrong-try again")

    except ValueError:
        print("\tDon't alnums,strs and symbol for choice--try again")

