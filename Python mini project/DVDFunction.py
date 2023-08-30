from EduDVDmodel import DVD
def print_info(DVD):
    print(f"DVD No:{DVD.DVD_No}, Title:{DVD.title},SUBJECT:{DVD.subject},rental_price_per_day:{DVD.rental_price},number_of_copies:{DVD.copies}")

class DVDFunction:
    def __init__(self) :
        self.list_of_DVD = []
        self.initial_data()
    
    def initial_data(self):
        dvd1 = DVD(DVD_No ="01",title = "Birth of the Solar System", subject ="Astronomy",rental_price = 2.50,copies = 10)
        dvd2 = DVD(DVD_No ="02", title ="Pythagoras Theorem",  subject ="Math",rental_price = 1.00,copies = 50)
        dvd3 = DVD(DVD_No ="03",title = "Data structures", subject ="Technology", rental_price =5.50,copies = 0)
        self.list_of_DVD.append(dvd1)
        self.list_of_DVD.append(dvd2)
        self.list_of_DVD.append(dvd3)

 

    def addfunc(self):
        __dvdNo = int(input("Enter DVD No of the DVD:"))
        __title = input("Enter title of the DVD:").strip()
        __subject = input("Enter subject of the DVD:")
        __rental_price = float(input("Enter rental price per day of the DVD:"))
        __copies = int(input("Enter number of copies of the DVD:"))
        DVD_New = DVD(DVD_No =__dvdNo,title = __title, subject =__subject,rental_price = __rental_price,copies = __copies)
        self.list_of_DVD.append(DVD_New)
        
        print("DVD  added successfully")
        
    def removefunc(self):
        removeDVD = int(input("Enter the DVD No of the DVD you want to remove:"))
        matched= list(DVDs for DVDs in self.list_of_DVD if DVDs.DVD_No == removeDVD)
        for DVDs in matched:
            self.list_of_DVD.remove(DVDs)
        print("DVD removed successfully")
        




    def available(self):
        matched = list (DVDs for DVDs in self.list_of_DVD if DVDs.copies > 0)
        for DVDs in matched:
            print_info(DVD = DVDs)
        
        
                
            

    def unavailable(self):
        matched = list(DVDs for DVDs in self.list_of_DVD if DVDs.copies == 0)
        for DVDs in matched:
            print_info(DVD = DVDs)
        


    def show_all(self):
        for DVDs in self.list_of_DVD:
            print_info(DVD = DVDs)
           
        

    def lend(self):
        removeDVD = int(input("Enter the DVD number: "))
        __copies = int(input("enter lend copies:"))
        matched= list(DVDs for DVDs in self.list_of_DVD if DVDs.DVD_No == removeDVD)
        for DVDs in matched:
            DVDs.copies -= __copies
        print("DVD lent")

    def update_again(self):
        removeDVD = int(input("Enter the DVD number: "))
        __copies = int(input("enter received copies:"))
        matched= list(DVDs for DVDs in self.list_of_DVD if DVDs.DVD_No == removeDVD)
        for DVDs in matched:
            DVDs.copies += __copies
        print(f"DVD Received with {__copies} copies")