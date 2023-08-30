from magazinemodel import Magazine
def print_info(magazine):
    print(f"Magazine No:{magazine.Magazine_No}, Title:{magazine.title},printing:{magazine.printing},SUBJECT:{magazine.subject},rental_price_per_day:{magazine.rental_price},number_of_copies:{magazine.copies}")

class MagazineFunction:
    def __init__(self) :
        self.list_of_magazine = []
        self.initial_data()
    
    def initial_data(self):
        Mag1 = Magazine(Magazine_No ="01",title = "History of Cricket",printing= "color", subject ="Sports",rental_price = 5.00,copies = 7)
        Mag2 = Magazine(Magazine_No ="02", title =" Evolution of the Computer", printing=" black&white", subject ="Technology",rental_price = 3.00,copies = 21)
        Mag3 = Magazine(Magazine_No ="03",title = "Women's Empower",printing= "color", subject ="Science", rental_price =10.00,copies = 0)
        self.list_of_magazine.append(Mag1)
        self.list_of_magazine.append(Mag2)
        self.list_of_magazine.append(Mag3)

 

    def addfunc(self):
        __megNo = int(input("Enter Magazine No of the Magazine:"))
        __title = input("Enter title of the Magazine:").strip()
        __printing = input("Enter printed method(color / Black&White) of the Magazine:")
        __subject = input("Enter subject of the Magazine:")
        __rental_price = float(input("Enter rental price per day of the Magazine:"))
        __copies = int(input("Enter number of copies of the Magazine:"))
        Magazine_New = Magazine(Magazine_No =__megNo,title = __title,printing= __printing, subject =__subject,rental_price = __rental_price,copies = __copies)
        self.list_of_magazine.append(Magazine_New)
        
        print("Magazine  added successfully")
        
    def removefunc(self):
        removeMeg = int(input("Enter the Magazine No of the Magazine you want to remove:"))
        matched= list(Magazines for Magazines in self.list_of_magazine if Magazines.Magazine_No == removeMeg)
        for Magazines in matched:
            self.list_of_magazine.remove(Magazines)
        print("Magazine removed successfully")
        




    def available(self):
        matched = list (Magazines for Magazines in self.list_of_magazine if Magazines.copies > 0)
        for Magazines in matched:
            print_info(magazine = Magazines)
        
        
                
            

    def unavailable(self):
        matched = list(Magazines for Magazines in self.list_of_magazine if Magazines.copies == 0)
        for Magazines in matched:
            print_info(magazine = Magazines)
        


    def show_all(self):
        for Magazines in self.list_of_magazine:
            print_info(magazine = Magazines)
           
        

    def lend(self):
        removeMag = int(input("Enter the Magazine number: "))
        __copies = int(input("enter lend copies:"))
        matched= list(Magazines for Magazines in self.list_of_magazine if Magazines.Magazine_No == removeMag)
        for Magazines in matched:
            Magazines.copies -= __copies
        print("Magazine lent")

    def update_again(self):
        removeMag = int(input("Enter the Magazine number: "))
        __copies = int(input("enter received copies:"))
        matched= list(Magazines for Magazines in self.list_of_magazine if Magazines.Magazine_No == removeMag)
        for Magazines in matched:
            Magazines.copies += __copies
        print(f"Magazine Received with {__copies} copies")