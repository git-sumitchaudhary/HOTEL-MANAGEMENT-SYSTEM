import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005')
mycursor = db.cursor()
mycursor.execute('create database if not exists HOTEL_MANAGEMENT')
db = mysql.connector.connect(host='localhost', user='root', password='sUmit1975#2005', database='HOTEL_MANAGEMENT')
mycursor = db.cursor()

mycursor.execute("create table if not exists hoteldata(Ccode int(5) primary key,Cname varchar(20),Cadd varchar(20),Cindate varchar(5),Coutdate varchar(5),Room_no varchar(5), Room_rent varchar(10),Food_bill varchar(10) default '00',Laudry_bill varchar(10) default '00',Game_bill varchar(10) default '00',SubTotal_bill varchar(10),Add_charges varchar(10) default '1800',GrandTotal_bill varchar(10))")
mycursor.execute("insert into hoteldata values(25,'Deepak','Morar,Gwalior',25,26, 1000, 6000,150,10,180,6340,1800,8140)")
mycursor.execute("insert into hoteldata values(26,'Amit','Morar,Gwalior',5,8,1017, 10000,5,0,50,10155,1800,11955)")
mycursor.execute("insert into hoteldata values(27,'Anuj','New Delhi',12,20,1407, 000,130,7,80,4217,1800,6017)")
mycursor.execute("insert into hoteldata values(28,'Kunal','Morar,Gwalior',5,8,1405, 9000,20,0,90,9110,1800,10910)")
mycursor.execute("insert into hoteldata values(29,'Smith','Canada',23,30,1008, 3000,20,5,50,30075,1800,31875)")
mycursor.execute("insert into hoteldata values(30,'Alex','America',25,30,1012, 3000,30,6,0,30036,1800,31836)")

mycursor.execute("create table if not exists Room(Rooms varchar(10),Type varchar(45), Charges int(7),Features varchar(90),Occupancy int(45))")
mycursor.execute("insert into Room values('1-500','Duplex',6000,'Two rooms on same floor connected by common stairs',5)")
mycursor.execute("insert into Room values('501-1000','Cabana',5000,'Faces water body,beach or a swimming pool',3)")
mycursor.execute("insert into Room values('1001-1500','Lanai',4000,'This room faces a landscape, a waterfall, or a garden',4)")
mycursor.execute("insert into Room values('1501-2000','Suit',3000, 'It is composed of one or more bedrooms, a living room, and a dining area',12)")

mycursor.execute("create table if not exists Customer(Ccode int(5),Cid_type varchar (20),Cid_no varchar(15) primary key , Cname varchar(15), Ccontact_no varchar(15),Cadd varchar(20),Cindate varchar(5), Coutdate varchar(5), CNationality varchar(10))")
mycursor.execute("insert into Customer values(25,'Aadhaar card',412563578952, 'Deepak',8269513294,'Morar,Gwalior',25,26,'Indian' )")
mycursor.execute("insert into Customer values(26,'Pan card', 5874695325,'Amit', 9063560847,'Morar,Gwalior',5,8,'Indian')")
mycursor.execute("insert into Customer values(27,'Pan card', 8456958236, 'Anuj', 9770563593,'New Delhi',12,20,'Indian')")
mycursor.execute("insert into Customer values(28,'Service Id',8546952156,'Kunal', 4856985123,'Morar,Gwalior',5,8,'Indian')")
mycursor.execute("insert into Customer values(29,'Voter Id Card',45896244,'Smith', 6598541256,'Canada',23,30,'Canadian')")
mycursor.execute("insert into Customer values(30,'Aadhaar card',485962578545, 'Alex',6325489652,'America',25,30,'American')")
db.commit()

print("Database and tables created successfully.")


