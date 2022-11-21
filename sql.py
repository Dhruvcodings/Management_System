#----------------------------------------project on mysql querry----------------------------------------
# invented by Dhruv Garg
# class 12th science

#input

import mysql.connector

#it take sql password to stablish connectivity in any sql with python if the host is local host and user root
pw=input('enter your sql password : ')

while True :
    try:
        con=mysql.connector.connect(host='localhost',
                                    user='root',
                                    password=str(pw))
        print('connection successfull ')
        break
    except :
        print()
        print('wrong password enter  _____________________________________________')
        pw=input('enter your sql password or 0 for exit : ')
        if pw=='0':
            exit()
cur=con.cursor()
def show_databases():
    print('-'*50)
    cur.execute('show databases')
    for i in cur:
        print(i)
    print('-'*50)
    
def create_database():
    while True :
        print('_'*50)
        print('for exit enter 0 and ')
        a=input('enter the name of data_base : ')

        #it is used so if the databse name is empty it can not created databse
        if len(a)==0:
            print()
            print('not empty ........')
            print()
        elif a=='0':
            break
        else:
            q='create database if not exists '+str(a)
            cur.execute(q)
            con.commit()
            print()
            print('database created successfully')
            print()
            print(':'*50)
            ask=input('want to create more databases y/n : ')
            print(':'*50)
            if ask.lower()=='n':
                break
            print('_'*50)
            
def create_table():
    while True :
        print('.'*50)
        print()
        try:
            while True :
                db=input('enter the name of data_base :')
                tb=input('enter the name of table to be created :')
                if len(db)!=0 and len(tb)!=0:
                    break
                else:
                    print()
                    print('name of database and table should be compulsory ')
                    print()
            cur.execute('use '+str(db))
            con.commit()
            print('------------for exit enter 0 and for creating table ---------------------------------')
            a=int(input('enter the number of columns to be created in table : '))

            #it use so if user does not want to create table it can exit
            if a==0:
                
                break
            else:
                try:
                    q="create table "+str(tb)+"("
                    for i in range(a):
                        c=input('enter data in format "column_name column_type(limit)" : ')
                        
                        # it is used so that querry q for execute has commas(,) between columns e.g. rollno int(10),name varchar(10)
                        #all commas between this is given by this statement
                        if i!=a-1:
                            q=q+str(c)+","
                        else:
                            # this is used with absent of ',' and present of ')' .we do this so in last we do not require any ',' and require to close the bracket
                            #e.g. rollno int(10),name varchar(20))- in last we close the bracket which is opened in above querry 'q' and under try block
                            q=q+str(c)+")"
                    cur.execute(q)
                    con.commit()
                    print()
                    print('table create successfully')
                    print()
                    print(':'*50)

                    #it asks user that they continue create table or not
                    ask=input('do you wants more table to create y/n : ')
                    print(':'*50)
                    if ask.lower()=='n':
                        break
                except Exception:
                    print()
                    print('something went wrong in creating a tuble structure , please try again .....................................')
                    print()
        except Exception :
            print()
            print('you entered wrong information, please try again ________________')
            print()
        print('.'*50)
        
def insert_into_table():
    while True:
        print('*'*50)
        print()
        try:
            db=input('enter the name of data_base :')
            tb=input('enter the name of table :')
            while True : 
                if len(db)!=0 and len(tb)!=0:
                    break
                else:
                    print()
                    print('name of database and table is compulsory  ')
                    print()
            cur.execute('use '+str(db))
            cur.execute('desc '+str(tb))
            
            #this list tup can store all columns name in itself when we describe table in above line
            tup=list()
            
            #this tup2 list can store all datatype of the followinf columns include limit e.g. varchar(20),int(10),etc.
            tup2=list()
            
            # this tup3 list can you tell you about the keys set on particular columns like primary key
            tup3=list()
            for i in cur:
                
                #tup concatenate all columns name in list
                tup=tup+[i[0]]
                
                #tup2 concatenate all datatype in list
                tup2+=[i[1]]
                
                #tup3 concatenate all key information in list
                tup3+=[i[3]]
            le=len(tup)
            print()
            co=int(input('enter 0 for exit and 1 for continue : '))
            if co==0:
                break
            else:
                while True:
                    s=str()
                    try:
                        for i in range (le):
                            print()
                            print("please enter the string in quotes'-----' if any..............................'")
                            
                            a=input('enter the '+str(tup[i])+'  '+str(tup2[i])+' '+str(tup3[i])+' : ')
                            #a=input('enter the   column_name_of input_table    datatype    key')
                            
                            print()
                            if i==le-1:

                                #this is used to avoid ',' in the last while inserting e.g insert into tablename value(12,'ok') 
                                s=s+str(a)+''
                                
                            else:

                                #this is used place ',' between the columns value e.g 12,'ok'
                                s=s+str(a)+','
                                
                        print(s)
                        print()
                        q='insert into '+str(tb)+' value('+str(s)+')'
                
                        cur.execute(q)
                        con.commit()
                        print('insert successfully')
                        print()
                        c=input('more enteries to insert in same table  y/n : ')
                        if c.lower()=='n':
                            break
                    except Exception :
                        print()
                        print('something went wrong in inserting the value please try again ................')
                        print()
            print(':'*50)
            ask=input('want to insert in more any table y/n : ')
            print(':'*50)
            if ask.lower()=='n':
                break
        except Exception :
            print()
            print('you enter some wrong information , please try again ..............................')
            print()
        print('*'*50)
        
def update_table():
    while True:
        print('#'*50)
        try:
            db=input('enter the name of data_base :')
            tb=input('enter the name of table :')
            print()
            cur.execute('use '+str(db))
            cur.execute('desc '+str(tb))

            #store columns name of inputed table
            tup=list()
            
            for i in cur:

                #concatenate columns name in list
                tup=tup+[i[0]]
                
            cur.execute('select * from '+str(tb))
            print(tup) # display columns name
            for j in cur:

                # print table details 
               print(j)
            while True:
                print()
                print('what do you want to update in ',tb)
                for k in range (len(tup)):

                    #display all columns name
                    #it is used to select the particular columns which we have to update 
                    print('enter ',k,' for ',tup[k])
                    
                a1=int(input('enter : '))
                print()
                print('how you identify the particular that you want to update')
                for l in range (len(tup)):

                    #it is used to indentify particular row record e.g we update the record by  a particular columns like rollno,id ,anythinf in atable
                    print('enter ',l,' for ',tup[l])
                    
                a2=int(input('enter : '))
                print()

                #this print statement is used as to inserting value in varchar type a string is used
                print("please enter the string in quotes'-----' if any..............................")

                #it take the old column name value from which we update the record
                a21=input('enter old '+str(tup[a2])+' from which you want to change : ')

                #it takes the new value which should be updated 
                a3=input('what do you want to place now in '+str(tup[a1])+' whose '+str(tup[a2])+' is '+str(a21)+' : ')
                
                q='update '+str(tb)+' set '+str(tup[a1])+'='+str(a3)+'\n where '+str(tup[a2])+'='+str(a21)
                print()
                cur.execute(q)
                con.commit()
                print()
                print('updation succeessfull \n')
                ask=input('more record for update in same table y/n : ')
                if ask.lower()=='n':
                    break
            print(':'*50)
            ask=input('more record for update in another table y/n : ')
            print(':'*50)
            if ask.lower()=='n':
                break
        except Exception :
            print()
            print('enter correct information ')
            print()
        print('#'*50)
        
            
def select_table_detail():
    while True:
        print('='*50)
        try:
            db=input('enter the name of data_base :')
            print()
            print('table inside database ')
            cur.execute('use '+str(db))
            cur.execute('show tables ')
            for i in cur:

                #it is used to print the name of every table in a selected database
                print(i)
                
            print()
            tb=input('enter the name of table :')

            #it descibe the table 
            cur.execute('desc '+str(tb))
            
            tup=list()

            #it is used here to store columns name in tup list 
            for i in cur:

                #it concatenate the columns of 0 index value in list
                #as in describing the table 1st word is the column name and rest of the details of the columns
                tup=tup+[i[0]]
                
            print()
            print(tup)
            print()
            cur.execute('select * from '+str(tb))
            for j in cur:
                print(j)
            print(':'*50)
            ask=input('want to select another table details y/n : ')
            print(':'*50)
            if ask.lower()=='n':
                break
        except Exception :
            print()
            print('enter correct information to select table details  ')
            print()
        print('='*50)
        
def describe_table():
    while True:
        print("'"*50)
        try:
            db=input('enter the name of data_base :')
            tb=input('enter the name of table :')
            print()
            cur.execute('use '+str(db))
            cur.execute('desc '+str(tb))
            for i in cur:
                print(i)
            print()
            print(':'*50)
            ask=input('want to describe more tables : ')
            print(':'*50)
            if ask.lower()=='n':
                break
        except Exception :
            print()
            print('please enter correct information , table is unable to describe .................')
        print("'"*50)
        
def show_tables():
    while True :
        print('"'*50)
        try:
            db=input('enter the name of data_base :')
            print()
            cur.execute('use '+str(db))
            cur.execute('show tables ')
            for i in cur:
                print(i)
            print()
            print(':'*40)
            ask=input('want to show more tables y/n : ')
            print(':'*40)
            if ask.lower()=='n':
                break
        except Exception :
            print()
            print('please try again you enter wrong information for showing table............................')
            print()
        print('"'*50)
        
def drop_database():
    while True :
        print('/'*50)
        try:
            cur.execute('show databases')
            for i in cur:
                print(i)
            print()
            b=input('enter the name of the database which you want to drop : ')
            cur.execute('drop database '+str(b))
            print()
            print('delete succeessfully')
            print(':'*50)
            ask=input('want to drop more database y/n : ')
            print(':'*50)
            if ask.lower()=='n':
                break
        except Exception :
            print()
            print('please check the above information and enter correct inmformation for droping databse ')
            print()
        print('/'*50)
        
def delete_table():
    while True :
        print('!'*50)
        try:
            db=input('enter the name of data_base :')
            print()
            cur.execute('use '+str(db))
            cur.execute('show tables ')
            for i in cur:
                print(i)
            print()
            tb=input('enter the table name for deletion : ')
            cur.execute('drop table '+str(tb))
            print()
            print('table deleted successfully ')
            print(':'*50)
            ask=input('want to show more tables y/n : ')
            print(':'*50)
            if ask.lower()=='n':
                break

        except Exception :
            print()
            print('please try again you enter wrong information or incorrect table name ............................')
            print()
        print('!'*50)

   

while True:
    print()
    print('-'*40)
    print()
    print("""1- to show databases
2- to create database
3- to create table
4- to insert into table
5- to update table
6- to select table details
7- to describe table structure
8- to show tables in particular databases
9- to drop database
10- to delete table in a particular database  
0- for exit""")
    
    ch=input('enter choice : ')
    
    print('-'*40)
    
    if ch=='1':
        print('_'*40)
        show_databases()
        print('_'*40)
        
    elif ch=='2':
        print('_'*40)
        create_database()
        print('_'*40)
        
    elif ch=='3':
        print('_'*40)
        create_table()
        print('_'*40)
        
    elif ch=='4':
        print('_'*40)
        insert_into_table()
        print('_'*40)
        
    elif ch=='5':
        print('_'*40)
        update_table()
        print('_'*40)
        
    elif ch=='6':
        print('_'*40)
        select_table_detail()
        print('_'*40)
        
    elif ch=='7':
        print('_'*40)
        describe_table()
        print('_'*40)
        
    elif ch=='8':
        print('_'*40)
        show_tables()
        print('_'*40)
        
    elif ch=='9':
        print('_'*40)
        drop_database()
        print('_'*40)
        
    elif ch=='10':
        print('_'*40)
        delete_table()
        print('_'*40)
        
    elif ch=='0':
        break
    else:
        print('_'*40)
        print('sorry no result found')
        print('_'*40)
        print()
        

        
        
# end of the project


# output
    
    
            
                            
            
        
    

        

                
