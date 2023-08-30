from BookFunction import BookFunction
from magazinefunction import MagazineFunction
from DVDFunction import DVDFunction
from LectureCDFunction import CDFunction

bookfunc = BookFunction()
megfunc = MagazineFunction()
DVDfunc = DVDFunction()
CDfunc = CDFunction()

def mainmenu():
    print("Main Menu")
    print("===========")
    print("1 - Books")
    print("2 - Magazine")
    print("3 - Educational DVD")
    print("4 - Lecture CD")
    print("5 - Quit")



def submenu1():
    choice = 1 
    selected_resource = "Book"
     
    while choice > 0:
        print("Please choose the operation you wish to perform")
        print(f"1-Add a {selected_resource}")
        print(f"2-Remove a {selected_resource}")
        print(f"3-Show Available {selected_resource}s")
        print(f"4-Show Unavailable {selected_resource}s")
        print(f"5 - Lend  {selected_resource}s")
        print(f"6 -Receive {selected_resource}s")
        print(f"7 - Display all the {selected_resource}s ")
        print(" 8- Back to Main menu")
        print("0 - Quit")

        try:
            choice = int(input("Please select your choice:"))
        
        except ValueError:
            print("Invalid input, Try again")
            
        if choice == 1:
            bookfunc.addfunc()    
        elif choice == 2:
            bookfunc.removefunc()
        elif choice == 3:
            bookfunc.available()
        elif choice == 4:
            bookfunc.unavailable()
        elif choice == 5:
            bookfunc.lend()
        elif choice == 6:
            bookfunc.update_again()
        elif choice == 7:
            CDfunc.show_all()
        elif choice == 8:
            mainmenu()
        else:
            print("Invalid input")
            

def submenu2():
    
    
    choice = 1 
    selected_resource = "Megazine"
     
    while choice > 0:
        print("Please choose the operation you wish to perform")
        print(f"1-Add a {selected_resource}")
        print(f"2-Remove a {selected_resource}")
        print(f"3-Show Available {selected_resource}s")
        print(f"4-Show Unavailable {selected_resource}s")
        print(f"5 - Lend  {selected_resource}s")
        print(f"6 -Receive {selected_resource}s")
        print(f"7 - Display all the  {selected_resource}s ")
        print(" 8- Back to Main menu")
        print("0 - Quit")

        try:
            choice = int(input("Please select your choice:"))
        
        except ValueError:
            print("Invalid input, Try again")
            
        if choice == 1:
            megfunc.addfunc()    
        elif choice == 2:
            megfunc.removefunc()
        elif choice == 3:
            megfunc.available()
        elif choice == 4:
            megfunc.unavailable()
        elif choice == 5:
            megfunc.lend()
        elif choice == 6:
            megfunc.update_again()
        elif choice == 7:
            CDfunc.show_all()
        elif choice == 8:
            mainmenu()
        else:
            print("Invalid input")
            
            
def submenu3():
    choice = 1 
    selected_resource = "Educational DVD"
     
    while choice > 0:
        print("Please choose the operation you wish to perform")
        print(f"1-Add a {selected_resource}")
        print(f"2-Remove a {selected_resource}")
        print(f"3-Show Available {selected_resource}s")
        print(f"4-Show Unavailable {selected_resource}s")
        print(f"5 - Lend  {selected_resource}s")
        print(f"6 -Receive {selected_resource}s")
        print(f"7 - Display all the  {selected_resource}s ")
        print(" 8- Back to Main menu")
        print("0 - Quit")

        try:
            choice = int(input("Please select your choice:"))
        
        except ValueError:
            print("Invalid input, Try again")
            
        if choice == 1:
            DVDfunc.addfunc()    
        elif choice == 2:
            DVDfunc.removefunc()
        elif choice == 3:
            DVDfunc.available()
        elif choice == 4:
            DVDfunc.unavailable()
        elif choice == 5:
            DVDfunc.lend()
        elif choice == 6:
            DVDfunc.update_again()
        elif choice == 7:
            CDfunc.show_all()
        elif choice == 8:
            mainmenu()
        else:
            print("Invalid input")
            

def submenu4():
    
    
    choice = 1 
    selected_resource = "Lecture CD"
     
    while choice > 0:
        print("Please choose the operation you wish to perform")
        print(f"1-Add a {selected_resource}")
        print(f"2-Remove a {selected_resource}")
        print(f"3-Show Available {selected_resource}s")
        print(f"4-Show Unavailable {selected_resource}s")
        print(f"5 - Lend  {selected_resource}s")
        print(f"6 -Receive {selected_resource}s")
        print(f"7 - Display all the  {selected_resource}s ")
        print(" 8- Back to Main menu")
        print("0 - Quit")

        try:
            choice = int(input("Please select your choice:"))
        
        except ValueError:
            print("Invalid input, Try again")
            
        if choice == 1:
            CDfunc.addfunc()    
        elif choice == 2:
            CDfunc.removefunc()
        elif choice == 3:
            CDfunc.available()
        elif choice == 4:
            CDfunc.unavailable()
        elif choice == 5:
            CDfunc.lend()
        elif choice == 6:
            CDfunc.update_again()
        elif choice == 7:
            CDfunc.show_all()
        elif choice == 8:
            mainmenu()
        
        else:
            print("Invalid input")
            
        
            
        


        
        
print(" Welcome to OUSL library system")
print("********************************") 
selected_resource = 1
while selected_resource > 0:
    mainmenu()
    
    try: 
        selected_resource = int(input("Please select your option:")) 
    except ValueError:
        print("Invalid selection") 
        mainmenu()  
    if  selected_resource == 1:
        submenu1()
        break
    elif selected_resource == 2:
        submenu2()
        break
    elif selected_resource == 3:
        submenu3()
        break
    
    elif selected_resource == 4:
        submenu4()
        break
    elif selected_resource == 5:
        quit()

