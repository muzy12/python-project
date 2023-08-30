from LectureCDmodel import CD
def print_info(CD):
    print(f"CD No:{CD.CD_No}, Title:{CD.title},SUBJECT:{CD.subject},rental_price_per_day:{CD.rental_price},number_of_copies:{CD.copies}")

class CDFunction:
    def __init__(self) :
        self.list_of_CD = []
        self.initial_data()
    
    def initial_data(self):
        cd1 = CD(CD_No ="01",title = "Basics of Western Music", subject ="Music",rental_price = 1.5,copies =11)
        cd2 = CD(CD_No ="02", title ="Japanese Language",  subject =" Foreign Language",rental_price = 30.00,copies = 40)
        cd3 = CD(CD_No ="03",title = "Sets and functions", subject ="Math", rental_price =10.00,copies = 0 )
        self.list_of_CD.append(cd1)
        self.list_of_CD.append(cd2)
        self.list_of_CD.append(cd3)

 

    def addfunc(self):
        __cdNo = int(input("Enter CD No of the CD:"))
        __title = input("Enter title of the CD:").strip()
        __subject = input("Enter subject of the CD:")
        __rental_price = float(input("Enter rental price per day of the CD:"))
        __copies = int(input("Enter number of copies of the CD:"))
        CD_New = CD(CD_No =__cdNo,title = __title, subject =__subject,rental_price = __rental_price,copies = __copies)
        self.list_of_CD.append(CD_New)
        
        print("CD  added successfully")
        
    def removefunc(self):
        removeCD = int(input("Enter the CD No of the CD you want to remove:"))
        matched= list(CDs for CDs in self.list_of_CD if CDs.CD_No == removeCD)
        for CDs in matched:
            self.list_of_CD.remove(CDs)
        print("CD removed successfully")
        




    def available(self):
        matched = list (CDs for CDs in self.list_of_CD if CDs.copies > 0)
        for CDs in matched:
            print_info(CD = CDs)
        
        
                
            

    def unavailable(self):
        matched = list(CDs for CDs in self.list_of_CD if CDs.copies == 0)
        for CDs in matched:
            print_info(CD = CDs)
        


    def show_all(self):
        for CDs in self.list_of_CD:
            print_info(CD = CDs)
           
        

    def lend(self):
        removeCD = int(input("Enter the CD number: "))
        __copies = int(input("enter lend copies:"))
        matched= list(CDs for CDs in self.list_of_CD if CDs.CD_No == removeCD)
        for CDs in matched:
            CDs.copies -= __copies
        print("CD lent")

    def update_again(self):
        removeCD = int(input("Enter the CD number: "))
        __copies = int(input("enter received copies:"))
        matched= list(CDs for CDs in self.list_of_CD if CDs.CD_No == removeCD)
        for CDs in matched:
            CDs.copies += __copies
        print(f"CD Received with {__copies} copies")