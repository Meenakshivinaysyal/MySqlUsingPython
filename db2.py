#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#       Name    ............Meenakshi Kumari
#       Batch ID............D10(GUVI)
#       Course Name.........Master’s in Python & Data Science with IIT Certification
#  
# Task1: To Create a database learning with student table.

#  USE Create,INSERT,SELECT,UPDATE,DELETE and Exit queries in a table.
#               
#  Display in Menu to choose  options:
#      1.To ADD new Student.(Enter Name ,Dept and five subjects marks of a student ,then calculate totalmarks,totalaverage and then on the basis of average assign Grades)
#      2.Get all Student.----This menu will display all students marks.
#      3.Edit Student------This menu will update the records.
#      4.Delete Student----This menu option will delete the selected record.
#      5.Exit--------------This option will exit the program.
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

import mysql.connector              # import mysql connector

def fn_Menu():                     # define func for menu
    ch = 255

    while ch != 0:                                            #  use while not equal to 0 and print the menu option one by one
        print("\n****Menu****")
        print ("[1] Add new student")
        print ("[2] Get all student")
        print ("[3] Edit student")
        print ("[4] Delete a student")
        print ("[0] Exit")
        ch = 255
        while ch > 4:
            ch=int(input("\nEnter your choice: "))                          # prompt to enter your choice 

        if ch == 1:
            fn_AddNewStudent()
        elif ch == 2:
            fn_GetAllStudent()
        elif ch == 3:
            fn_EditStudent()
        elif ch == 4:
            fn_DeleteStudent()
        else:
            con.close()
            exit
                                                                #  create a function to addnew student details
def fn_AddNewStudent():
    cur=con.cursor()                                            # Use the cursor() method of a MySQLConnection object to create a cursor object 
    query="select * from student"                               # write a select query 
    cur.execute(query)                                          # execute the query 
    data = cur.fetchall()                                       # extract the query data using fetchall 

    while True:
        j = cur.rowcount + 1
        print(j)
        n=input("name: ")
        s=input("dept: ")
        m=int(input("Marks1: "))
        o=int(input("Marks2: "))
        p=int(input("Marks3: "))
        q=int(input("Marks4: "))
        r=int(input("Marks5: "))
        query = "Insert into student values(%s,'%s','%s',%s,%s,%s,%s,%s)" %(j,n,s,m,o,p,q,r)
        print(query)
        cur.execute(query)
        con.commit()
        cur.execute("select * from student")
        data = cur.fetchall()
        ch=input("Enter More records?(y/n)")
        if ch in 'Nn':
            break
    for i in data:
        print(i)
    print("total record entered", cur.rowcount)
    print("----------------------------------")
        
# define a function Getallstudent to display all the records of the student table.            

def fn_GetAllStudent():
    cur=con.cursor()
    query="select * from student"
    cur.execute(query)
    result=cur.fetchall()
    print ("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format('id','Name','Dept','Marks1', 'Marks2', 'Marks3', 'Marks4', 'Marks5', 'Total', 'Avg', 'Grade'))
    for i in result:
        id, name, dept, Marks1, Marks2, Marks3, Marks4, Marks5 = i                         # all the fields is equal to i
        l_lTotal = Marks1 + Marks2 + Marks3 + Marks4 + Marks5                              # calculate total od all the 5 marks fields.
        l_lAvg = l_lTotal/5                                                                #calculate the total average .

        if l_lAvg >= 90:                                                                   # using if condition we retrieve the grades 
            l_strGrade = 'A'
        elif l_lAvg >= 80 and l_lAvg <90:
            l_strGrade = 'B'
        elif l_lAvg >= 70 and l_lAvg <80:
            l_strGrade = 'C'
        else:
            l_strGrade = 'D'

        print ("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8}".format(id,name, dept, Marks1, Marks2, Marks3, Marks4, Marks5, l_lTotal, l_lAvg, l_strGrade ))

# Define function to edit the student records

def fn_EditStudent():
    #-------------------------------------
    cur=con.cursor()
    query="select * from student"
    cur.execute(query)
    result=cur.fetchall()
    print ("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} ".format('id','Name','Dept','Marks1', 'Marks2', 'Marks3', 'Marks4', 'Marks5'))
    for i in result:
        id, name, dept, Marks1, Marks2, Marks3, Marks4, Marks5 = i
        print ("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} ".format(id,name, dept, Marks1, Marks2, Marks3, Marks4, Marks5))
    #-------------------------------------

    L_List = ""   # use local list here 
    while True:                     
        try:
            l_id = input("enter the id : ")                         # prompt for id (choose the id of the record needed to be updated )
            if True == l_id.isnumeric():                            # id should be numeric
                break
        except ValueError:
            print("Please input printable characters only...")  
            continue

    for i in result:
        if i[0] == int(l_id):
            L_List = list(i)
            break

    if "" == L_List:
        print("Record Not Present !")
        return
    else:
        print("Selected Record For Updation: ", L_List)                            # Record of selected id get selected for updation
    #-------------------------------------
    while True:
        try:
            l_input=input("Edit the name?(" + str(L_List[1]) + ") or Just enter to skip:")      # edit the name or skip to move to next column 
            if True == l_input.isprintable():
                break
        except ValueError:
            print("Please input printable characters only...")  
            continue
    if l_input != "":
        L_List[1] = l_input
    print(L_List[1])

    while True:
        try:
            l_input=input("Edit the dept?(" + str(L_List[2]) + ") or Just enter to skip:")      # edit the dept or skip to move to next column 
            if True == l_input.isprintable() or True == l_input.isalpha():
                break
        except ValueError:
            print("Please input printable characters only...")  
            continue
    if l_input != "":
        L_List[2] = l_input.upper()
    print(L_List[2])

    while True:
        try:
            l_input=input("Edit the Marks1?(" + str(L_List[3]) + ") or Just enter to skip:")        # edit the Marks1 or skip to move to next column 
            if True == l_input.isnumeric() or 0 == len(l_input):
                break
        except ValueError:
            print("Please input integer only...")  
            continue
    if l_input != "":
        L_List[3] = l_input

    while True:
        try:
            l_input=input("Edit the Marks2?(" + str(L_List[4]) + ") or Just enter to skip:")        # edit the Marks2 or skip to move to next column 
            if True == l_input.isnumeric() or 0 == len(l_input):
                break
        except ValueError:
            print("Please input integer only...")  
            continue
    if l_input != "":
        L_List[4] = l_input

    while True:
        try:
            l_input=input("Edit the Marks3?(" + str(L_List[5]) + ") or Just enter to skip:")        # edit the Marks3 or skip to move to next column 
            if True == l_input.isnumeric() or 0 == len(l_input):
                break
        except ValueError:
            print("Please input integer only...")  
            continue
    if l_input != "":
        L_List[5] = l_input

    while True:
        try:
            l_input=input("Edit the Marks4?(" + str(L_List[6]) + ") or Just enter to skip:")            ## edit the Marks4 or skip to move to next column 
            if True == l_input.isnumeric() or 0 == len(l_input):
                break
        except ValueError:
            print("Please input integer only...")  
            continue
    if l_input != "":
        L_List[6] = l_input

    while True:

        try:
            l_input=input("Edit the Marks6?(" + str(L_List[7]) + ") or Just enter to skip:")            # edit the Marks5 or skip to move to next column 
            if True == l_input.isnumeric() or 0 == len(l_input):
                break
        except ValueError:
            print("Please input integer only...")  
            continue
    if l_input != "":
        L_List[7] = l_input


    print(L_List)
    #-------------------------------------


# -----------------Query for updation of records---------------------------------------------------------------------------------
    query2="update student SET name='%s', dept='%s', Marks1=%s, Marks2=%s, Marks3=%s, Marks4=%s, Marks5=%s where id= %s" %(L_List[1], L_List[2], L_List[3], L_List[4], L_List[5], L_List[6], L_List[7], l_id) 

    cur.execute(query2)
    con.commit()
    print("total record updated", cur.rowcount)     #------Print the total record updated with count

    cur.execute("select * from student")            #------Display all the student records.
    data = cur.fetchall()
    for i in data:
        print(i)
    print("total record entered", cur.rowcount)
    
    
#--------------Define a function to delete the selected record from the table------------------------------
def fn_DeleteStudent():
    #-------------------------------------
    cur=con.cursor()
    query="select * from student"
    cur.execute(query)
    result=cur.fetchall()
    print ("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} ".format('id','Name','Dept','Marks1', 'Marks2', 'Marks3', 'Marks4', 'Marks5'))
    for i in result:
        id, name, dept, Marks1, Marks2, Marks3, Marks4, Marks5 = i
        print ("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} ".format(id,name, dept, Marks1, Marks2, Marks3, Marks4, Marks5))
    #-------------------------------------
    L_List = ""
    while True:
        try:
            l_id = input("enter the id : ")
            if True == l_id.isnumeric():
                break
        except ValueError:
            print("Please input printable characters only...")  
            continue
    for i in result:
        if i[0] == int(l_id):
            L_List = list(i)
            break

    if "" == L_List:
        print("Record Not Present !")
        return
    else:
        print("Selected Record For Deletion: ", L_List)
    #-------------------------------------deletion query with promption for ID --------------------------------------
    query="DELETE from  student where id=%s" %(l_id) 
    cur.execute(query)
    con.commit()
    print("total record deleted", cur.rowcount)   

#-------------Connection with mysql database-----------------------------------------------------------
con =mysql.connector.connect(host='localhost',
                            user='root',
                            password='',
                            database='learning')
con._open_connection()
cur=con.cursor()
fn_Menu()           # fnmenu function will dispaly all the menus at the beginning of program .....choose the options one by one.


#-----------------Code by Meenakshi kumari -----------------------------------------------