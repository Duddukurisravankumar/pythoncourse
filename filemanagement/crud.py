from pathlib import Path
import os
def readfilemanagement():
    path =Path('')
    iteam = list(path.rglob('*'))
    for i ,iteam in enumerate(iteam):
        print(f"{i+1} : {iteam}")

def createfile():
    try:
        readfilemanagement()
        name = input("enter your file name:-")
        p = Path(name)
        if p.exists() and p.is_file():
            print(f"{p} already existed")
        else:
            with open(p,'w') as fs:
                data = input("enter your data: ")
                fs.write(data)
                print("creating is completed")
            
    except Exception as err:
        print(f"an error occured {err}")
        
        
def readfile():
    readfilemanagement()
    name = input("selsect your file name ")
    p = Path(name)
    if p.exists and p.is_file():
        with open(p,'r') as fs:
            data = fs.read()
            print(data)
        print("reading is completed")
        
        
def update():
    try:
        readfilemanagement()
        select = input("enter the requeried filename ")
        p = Path(select)
        if p.exists and p.is_file():
            print("enter 1 for the adding data ")
            print(":enter 2 for the changing the name of file ")
            print("enter 3 for the overwriting the file ")
            choice = int(input("enter your choice "))
            if choice == 1:
                with open(p,'a') as fs:
                    data = fs.write(input("enter data to add "))
                    print(data)
                    print("updating is completed")
            if choice == 2:
                data = Path((input("enter the name you want to change ")))
                p.rename(data)
                print(" task completed")
            if choice == 3:
                with open(p,'w') as fs:
                    data = input("enter the data that need to change ")
                    fs.write(data)
                    print("overwriting completed")
    except Exception as err:
        print(f"{err }occured")
        
        
def daleting():
    readfilemanagement()
    choice = input("enter file you want to delet ")
    de = Path(choice)
    if de.exists and de.is_file():
        os.remove(de)
        print("delection is completed")
    else:
        print("enter the existed file name")
               

print("enter the 1 for creating a file")
print("enter the 2 for reading a file")
print("enter the 3 for updating a file")
print("enter the 4 for deleting a file")
check = int(input ("enter your choice "))
if check == 1:
    createfile()
if check == 2:
    readfile()
if check == 3:
    update()
if check == 4:
    daleting()