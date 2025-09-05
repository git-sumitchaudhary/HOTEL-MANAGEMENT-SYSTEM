import mysql.connector
import random

def hotelfarecal():
    while True:
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Booking for Room")
        print("2. Show Customer Record")
        print("3. Search Customer Record")
        print("4. Delete Customer Record")
        print("5. Update Customer Record")
        print("6. Return to Main Menu")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        b = input("\nEnter your choice: ")

        if b == '1':
            z = 'y'
            while z.lower() == 'y':
                inputdata()
                z = input("\nDo you want to continue? (y/n): ")
            if z.lower() == 'n':
                hotelfarecal()
        elif b == '2':
            z = 'y'
            while z.lower() == 'y':
                display()
                z = input("\nDo you want to continue? (y/n): ")
            if z.lower() == 'n':
                hotelfarecal()
        elif b == '3':
            z = 'y'
            while z.lower() == 'y':
                search()
                z = input("\nDo you want to continue? (y/n): ")
            if z.lower() == 'n':
                hotelfarecal()
        elif b == '4':
            z = 'y'
            while z.lower() == 'y':
                delete()
                z = input("\nDo you want to continue? (y/n): ")
            if z.lower() == 'n':
                hotelfarecal()
        elif b == '5':
            z = 'y'
            while z.lower() == 'y':
                update()
                z = input("\nDo you want to continue? (y/n): ")
            if z.lower() == 'n':
                hotelfarecal()
        elif b == '6':
            break
        else:
            print("Invalid Input....")


def inputdata():
    r = 0
    l = 0
    p = 0
    s = 0

    db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()

    Ccode = input("\nEnter Customer Code: ")
    Cname = input("Enter Customer Name: ")
    Cadd = input("Enter Customer Address: ")
    Cindate = input("Enter Customer Check in Date: ")
    Coutdate = input("Enter Customer Check out Date: ")
    Cid_type = input("Enter your Identity card name: ")
    Cid_no = input("Enter your Identity number: ")
    Ccontact_no = input("Enter you Contact number: ")
    CNationality = input("Enter your nationality: ")
    print("\n")

    print("We have the following rooms for you:-")
    print("1. Duplex ---> Rs 6000 PN\\-")
    print("2. Cabana ---> Rs 5000 PN\\-")
    print("3. Lanai ---> Rs 4000 PN\\-")
    print("4. Suit ---> Rs 3000 PN\\-")
    print("5. Mini ---> RS 2000 PN\\-")
    print("6. Next")

    while True:
        try:
            x = int(input("\nEnter you choice: "))
            if x == 1:
                n = int(input("For How Many Nights Did You Stay: "))
                print("You have opted room Duplex")
                s = s + 6000 * n
                Room_no = random.randint(1, 501)
                print("Your Room Number is:", Room_no)
                break
            elif x == 2:
                n = int(input("For How Many Nights Did You Stay: "))
                print("You have opted room Cabana")
                s = s + 5000 * n
                Room_no = random.randint(501, 1001)
                print("Your Room Number is:", Room_no)
                break
            elif x == 3:
                n = int(input("For How Many Nights Did You Stay: "))
                print("You have opted room Lanai")
                s = s + 4000 * n
                Room_no = random.randint(1001, 1501)
                print("Your Room Number is:", Room_no)
                break
            elif x == 4:
                n = int(input("For How Many Nights Did You Stay: "))
                print("You have opted room Suit")
                s = s + 3000 * n
                Room_no = random.randint(1501, 2001)
                print("Your Room Number is:", Room_no)
                break
            elif x == 5:
                n = int(input("For How Many Nights Did You Stay: "))
                print("You have opted room Mini")
                s = s + 2000 * n
                Room_no = random.randint(2001, 2501)
                print("Your Room Number is:", Room_no)
                break
            elif x == 6:
                break
            else:
                print("Please choose a room")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("\nYour room rent is", s, 'RS')

    print("\n*****RESTAURANT MENU*****")
    print("1.water--->Rs20", "2.tea--->Rs10", "3.breakfast combo--->Rs90", "4.lunch --->Rs110", "5.dinner-->Rs150", "6.Next")
    while True:
        try:
            c = int(input("\nEnter your choice: "))
            if c == 1:
                d = int(input("Enter the quantity: "))
                r = r + 20 * d
            elif c == 2:
                d = int(input("Enter the quantity: "))
                r = r + 10 * d
            elif c == 3:
                d = int(input("Enter the quantity: "))
                r = r + 90 * d
            elif c == 4:
                d = int(input("Enter the quantity: "))
                r = r + 110 * d
            elif c == 5:
                d = int(input("Enter the quantity: "))
                r = r + 150 * d
            elif c == 6:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("\nTotal food Cost=Rs ", r)

    print("\n******LAUNDRY MENU*******")
    print("1.Shorts--->Rs3", "2.Trousers--->Rs4", "3.Shirt--->Rs5", "4.Jeans --->Rs6", "5.Girlsuit -->Rs8", "6.Next")
    while True:
        try:
            e = int(input("\nEnter your choice: "))
            if e == 1:
                f = int(input("Enter the quantity: "))
                l = l + 3 * f
            elif e == 2:
                f = int(input("Enter the quantity: "))
                l = l + 4 * f
            elif e == 3:
                f = int(input("Enter the quantity: "))
                l = l + 5 * f
            elif e == 4:
                f = int(input("Enter the quantity: "))
                l = l + 5 * f
            elif e == 5:
                f = int(input("Enter the quantity: "))
                l = l + 6 * f
            elif e == 6:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("\nTotal Laundary Cost=Rs", l)

    print("\n******GAME MENU*******")
    print("1.Table tennis--->Rs60", "2.Bowling--->Rs80", "3.Snooker--->Rs70", "4.Video games--->Rs90", "5.Pool--->Rs50", "6.Next")
    while True:
        try:
            g = int(input("\nEnter your choice: "))
            if g == 1:
                h = int(input("No. of hours: "))
                p = p + 60 * h
            elif g == 2:
                h = int(input("No. of hours: "))
                p = p + 80 * h
            elif g == 3:
                h = int(input("No. of hours: "))
                p = p + 70 * h
            elif g == 4:
                h = int(input("No. of hours: "))
                p = p + 90 * h
            elif g == 5:
                h = int(input("No. of hours: "))
                p = p + 50 * h
            elif g == 6:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("\nTotal Game Bill=Rs", p)

    SubTotal_bill = s + r + l + p
    Add_charges = 1800
    GrandTotal_bill = SubTotal_bill + Add_charges
    print("\nYou have to pay Rs", GrandTotal_bill)

    rec = ("INSERT INTO hoteldata VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    cotm = ("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

    data1 = (Ccode, Cid_type, Cid_no, Cname, Ccontact_no, Cadd, Cindate, Coutdate, CNationality)
    data2 = (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no, s, r, l, p, SubTotal_bill, Add_charges, GrandTotal_bill)

    mycursor.execute(cotm, data1)
    mycursor.execute(rec, data2)
    db.commit()
    mycursor.close()
    print("\nRecord Inserted...... ")
    db.close()


def display():
    print("\n")
    print("1. Display all records")
    print("2. Display through code number")
    d = input("\nEnter your choice: ")
    if d == '1':
        db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        qry = ("SELECT h.Ccode, h.Cname, h.Cadd, h.Cindate, h.Coutdate, h.Room_no, c.CNationality, c.Ccontact_no, c.Cid_type, c.Cid_no FROM hoteldata h, customer c WHERE h.Ccode = c.Ccode")
        mycursor.execute(qry)
        for (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no, CNationality, Ccontact_no, Cid_type, Cid_no) in mycursor:
            print("\n")
            print("Customer details...... ")
            print("Customer code:", Ccode)
            print("Customer name:", Cname)
            print("Customer Id type:", Cid_type)
            print("Customer Id Number:", Cid_no)
            print("Customer address:", Cadd)
            print("customer Nationality:", CNationality)
            print("Check in date:", Cindate)
            print("Check out date", Coutdate)
            print("Room number:", Room_no)
            print("Customer Contact number:", Ccontact_no)
            print("____________________")
        mycursor.close()
        print("\nIt's All record")
        db.close()
    elif d == '2':
        db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
        mycursor = db.cursor()
        Ccode = input("\nEnter code of customer: ")
        qry = ("SELECT h.Ccode, h.Cname, h.Cadd, h.Cindate, h.Coutdate, h.Room_no, c.CNationality, c.Ccontact_no, c.Cid_type, c.Cid_no FROM hoteldata h, customer c WHERE h.Ccode = c.Ccode AND h.Ccode = %s")
        rec_code = (Ccode,)
        mycursor.execute(qry, rec_code)
        rec_count = 0
        for (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no, CNationality, Ccontact_no, Cid_type, Cid_no) in mycursor:
            rec_count += 1
            print('\nRecord Found..... ')
            print("Customer details...... ")
            print("Customer code:", Ccode)
            print("Customer name:", Cname)
            print("Customer Id type:", Cid_type)
            print("Customer Id Number:", Cid_no)
            print("Customer address:", Cadd)
            print("customer Nationality:", CNationality)
            print("Check in date:", Cindate)
            print("Check out date", Coutdate)
            print("Room number:", Room_no)
            print("Customer Contact number:", Ccontact_no)
        if rec_count == 0:
            print("\nRecord not found!!")
        db.commit()
        mycursor.close()
        db.close()
    else:
        print("Invalid Input!!")


def search():
    db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    Ccode = input("\nEnter Customer Code to be Searched in Hotel: ")
    qry = ("SELECT * FROM hoteldata WHERE Ccode = %s")
    rec_srch = (Ccode,)
    mycursor.execute(qry, rec_srch)
    rec_count = 0
    for (Ccode, Cname, Cadd, Cindate, Coutdate, Room_no, Room_rent, Food_bill, Laudry_bill, Game_bill, SubTotal_bill, Add_charges, GrandTotal_bill) in mycursor:
        rec_count += 1
        print('\nRecord Found')
        print("Customer details .....")
        print("Customer code:", Ccode)
        print("Customer name:", Cname)
        print("Customer address:", Cadd)
        print("Check in date:", Cindate)
        print("Check out date", Coutdate)
        print("Room number:", Room_no)
        print("Room rent is:", Room_rent)
        print("Food bill is:", Food_bill)
        print("Laundary bill is:", Laudry_bill)
        print("Game bill is:", Game_bill)
        print("Sub total bill is:", SubTotal_bill)
        print("Additional Service Charges is:", Add_charges)
        print("Grand Total bill is:", GrandTotal_bill)
    if rec_count == 0:
        print("\nRecord not found!!")
    db.commit()
    mycursor.close()
    db.close()


def delete():
    db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    Ccode = input("\nEnter Customer Code to be delete from Hotel: ")
    qry = ("DELETE FROM hoteldata WHERE Ccode = %s")
    qry1 = ("DELETE FROM customer WHERE Ccode = %s")
    del_rec = (Ccode,)
    mycursor.execute(qry, del_rec)
    mycursor.execute(qry1, del_rec)
    db.commit()
    mycursor.close()
    print("\nRecord Deleted..... ")
    db.close()


def update():
    print("\nWhich Data Should be Updated ..... ")
    print("1. Customer Name")
    print("2. Customer Address")
    print("3. Customer out Date")
    print("4. Customer Room Number")
    print("5. Customer Contact number")
    try:
        c = int(input("\nSelect your Choice: "))

        if c == 1:
            db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
            mycursor = db.cursor()
            Ccode = input('\nEnter Code of Customer to be Updated: ')
            Cname = input("Enter Customer Name: ")
            q = ('UPDATE hoteldata SET Cname = %s WHERE Ccode = %s')
            data = (Cname, Ccode)
            mycursor.execute(q, data)
            q = ('UPDATE customer SET Cname = %s WHERE Ccode = %s')
            data = (Cname, Ccode)
            mycursor.execute(q, data)
            print('\nRecord Updated .... ')
            db.commit()
            mycursor.close()
            db.close()
        elif c == 2:
            db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
            mycursor = db.cursor()
            Ccode = int(input('\nEnter Code of Customer to be Updated: '))
            Cadd = input("Enter Customer Address: ")
            q = ('UPDATE hoteldata SET Cadd = %s WHERE Ccode = %s')
            data = (Cadd, Ccode)
            mycursor.execute(q, data)
            q = ('UPDATE customer SET Cadd = %s WHERE Ccode = %s')
            data = (Cadd, Ccode)
            mycursor.execute(q, data)
            print('\nRecord Updated .... ')
            db.commit()
            mycursor.close()
            db.close()
        elif c == 3:
            db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
            mycursor = db.cursor()
            Ccode = int(input('\nEnter Code of Customer to be Updated: '))
            Coutdate = input("Enter Customer out Date: ")
            q = ('UPDATE hoteldata SET Coutdate = %s WHERE Ccode = %s')
            data = (Coutdate, Ccode)
            mycursor.execute(q, data)
            q = ('UPDATE customer SET Coutdate = %s WHERE Ccode = %s')
            data = (Coutdate, Ccode)
            mycursor.execute(q, data)
            print('\nRecord Updated .... ')
            db.commit()
            mycursor.close()
            db.close()
        elif c == 4:
            db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
            mycursor = db.cursor()
            Ccode = int(input('\nEnter Code of Customer to be Updated: '))
            Room_no = input("Enter Customer Room Number: ")
            q = ('UPDATE hoteldata SET Room_no = %s WHERE Ccode = %s')
            data = (Room_no, Ccode)
            mycursor.execute(q, data)
            print('\nRecord Updated .... ')
            db.commit()
            mycursor.close()
            db.close()
        elif c == 5:
            db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
            mycursor = db.cursor()
            Ccode = int(input('\nEnter Code of Customer to be Updated: '))
            Ccontact_no = input("Enter Customer Contact number: ")
            q = ('UPDATE customer SET Ccontact_no = %s WHERE Ccode = %s')
            data = (Ccontact_no, Ccode)
            mycursor.execute(q, data)
            print('\nRecord Updated .... ')
            db.commit()
            mycursor.close()
            db.close()
        else:
            print("Invalid Input!!")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main_menu():
    while True:
        print("\n\t\t\t\t\t\t\t\tWELCOME TO THE TAJ PALACE")
        print("\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("1. Speciality of your Hotel")
        print("2. Customer Management")
        print("3. Booking for Private Party")
        print("4. EXIT")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

        b = input("\nEnter your choice: ")

        if b == '1':
            speciality()
        elif b == '2':
            hotelfarecal()
        elif b == '3':
            # party()  # This function is not defined in the provided code
            print("This feature is not yet implemented.")
        elif b == '4':
            quit()
        else:
            print("Wrong Choice")


def speciality():
    db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
    mycursor = db.cursor()
    qry = ("SELECT * FROM room")
    mycursor.execute(qry)
    print("\nDESCRIPTION:")
    print("The Taj Mahal Palace, Mumbai makes a wonderful starting point from which to discover the charms that bring people from around the globe flocking to Mumbai city, India's commercial and entertainment capital. Around the corner from the hotel is Colaba Causeway - a vibrant stretch filled with roadside stores, jewellery shops, pubs and restaurants that whisks guests back in time to old Bombay. Take a tour of and learn about the rich history and architecture of this vibrant city, accompanied by Government of India appointed and trained tourism officials. Walk past Gothic buildings and through narrow streets. Visit historic locations such as Wellington Fountain, Regal Cinema, Indian Merchant Building, Asiatic Library, CSMVS Museum, Jehangir Art Gallery, Elphinstone College and other prominent buildings in varying styles of architecture, each symbolic of a particular period of Bombay's social and commercial history.\n")
    for (Rooms, Type, Charges, Features, Occupancy) in mycursor:
        print("We have Rooms", Rooms, "of type", Type, ", it has", Features, "and occupancy of", Occupancy, "persons.")
    db.commit()
    print("\nSERVICES:")
    print("For the disabled, Breakfast, Restaurant, Adsl wi-fi internet, Fax, Newspapers, Transfer, Tourist information, Small animals welcome, Private parking, Guarded garage, 24h reception, 24h bar, Beaches at 500 m, Shuttle bus stop for the airport only 10 minutes away.\n")
    print("FACILITIES:")
    print("ReceptionHall, Bar, Pool 10.00 a.m. - 6.00 p.m.\n")
    print("BOOKING:")
    print("Excursions, Guided tours, Private parties")
    mycursor.close()
    db.close()


if __name__ == "__main__":
    main_menu()


