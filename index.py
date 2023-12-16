from random import randint
import time
while True:
    try:
        import datetime
        a1=randint(10000,100000)
        print(a1)
        a=input('enter password : ')
        print()
        a11=str(a1)
        a111=' '*int(a11[0])
        a2=str(a1)*2+str(a111)+'DSQL'
       
    
        if a==a2 or a.lower()=='dpcsp100':

            print()
            print('.'*140)
            print('you are logged in into the system ')
            print('.'*140)
            print()
            break
    

    

        else:
            print()
            print('you enter wrong password ')
            print()
            print('-'*140)
            o=input('want to continue y/n : ')
            print('-'*140)
            print()
            if o.lower()=='n':
                print()
                print('!'*140)
                print('ok you are going to exit ')
                print('!'*140)
                print()
                exit()
    except :
            print()
            print('!'*140)
            print('something went wrong ')
            print('!'*140)
            print()



print()
print()
time.sleep(0)
print('*'*140)
print('\t\t\t\t welcome to the database management system')
print('*'*140)
print('invented by Dhruv Garg')
time.sleep(0)
print()
print()
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
    except Exception:
        print()
        print('wrong password enter  _____________________________________________')
        pw=input('enter your sql password or 0 for exit : ')
        if pw=='0':
            exit()
cur=con.cursor()
def show_databases():
    print('-'*50)
    cur.execute('show databases')
    print('.'*100)
    print('name of databases : ')
    print('.'*100)
    print()
    for i in cur:
        print('%20s'%i)
    print()
    print('-'*50)
    
def create_database():
    while True :
        print('_'*50)
        print('for exit enter 0 and for creating ')
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
            
            while True :
                db=input('enter the name of data_base :')
                tb=input('enter the name of table :')
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
                            
                            
                            a=input('enter the '+str(tup[i])+'  '+str(tup2[i])+' '+str(tup3[i])+' : ')
                            #a=input('enter the   column_name_of input_table    datatype    key')
                            
                            print()
                            if i==le-1:

                                # it use to identify the data type
                                if str(tup2[i][0]).lower()=='v' or str(tup2[i][0]).lower()=='d' or str(tup2[i][0]).lower()=='t' or str(tup2[i][0]).lower()=='c':
                                    s+="'"+str(a)+"'"+''
                        

                                else:

                                    #this is used to avoid ',' in the last while inserting e.g insert into tablename value(12,'ok') 
                                    s=s+str(a)+''
                                
                            else:

                                if tup2[i][0].lower()=='v' or tup2[i][0].lower()=='d' or tup2[i][0].lower()=='t' or str(tup2[i][0]).lower()=='c':
                                    s+="'"+str(a)+"'"+','

                                
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
            print('selected table details are ->')
            print('.'*100)
            print()
            for x in range (len(tup)):
                
                print('%20s'%tup[x],end='')
                # display columns name in above format
                
            print()
            print('.'*100)
            
            for j in cur:
                # show all table detail
                
                for y in j:
                    # show table row detail row wise
                    
                    print('%20s'%y,end='')
                    #display in above format 
                print()
            print('-'*100)

                # print table details 
               
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
            print('-'*50)
            print('table inside database ->')
            print('-'*50)
            print()
            cur.execute('use '+str(db))
            cur.execute('show tables ')
            for i in cur:
                #it is used to print the name of every table in a selected database
                print('%20s'%i)
                
            print('.'*50)
            print()
            print()
            
            tb=input('enter the name of table to show details :')

            #it descibe the table 
            cur.execute('desc '+str(tb))
            
            tup=list()

            #it is used here to store columns name in tup list 
            for i in cur:

                #it concatenate the columns of 0 index value in list
                #as in describing the table 1st word is the column name and rest of the details of the columns
                tup=tup+[i[0]]
                
            print()
            print('table details of selected table and selected database :')
            print()
            print('.'*140)
            
            for i in range (len(tup)):
                print('%20s'%tup[i],end='')
            print()
            print('.'*140)
            print()
            
            cur.execute('select * from '+str(tb))
            for j in cur:
                for k in j:
                    print('%20s'%k,end='')
                print()
            print('-'*100)
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
            print('.'*140)
            print('%20s'%'column_name','%20s'%'type','%20s'%'null','%20s'%'key','%20s'%'default','%20s'%'extra')
            print('.'*140)
            for i in cur:
                for j in i:
                    print('%20s'%j,end='')
                print()
            print()
            print(':'*50)
            ask=input('want to describe more tables y/n : ')
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
            print()
            print('table name in selected database ->')
            print()
            print('.'*100)
            print()
            
            for i in cur:
                    print('%20s'%i)
            print()
            print('.'*100)
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
            print('.'*100)
            print()
            print('databases name : ')
            print()
            for i in cur:
                print('%20s'%i)
            print()
            print('.'*100)
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
            print('.'*100)
            print()
            print('table names in selected database ')
            print()
            for i in cur:
                print('%20s'%i)
            print()
            print('.'*100)
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

        

def search_operation():
    while True:
        try:
            
            print('-'*140)
            db=input('enter the name of data_base :')
            tb=input('enter the name of table :')
            print()
            cur.execute('use '+str(db))
            cur.execute('desc '+str(tb))
            tup=list()
            tup2=list()
            tup3=list()
            for i in cur:
                tup=tup+[i[0]]
                tup2+=[i[1]]
                tup3+=[i[3]]
            cur.execute('select * from '+tb)
               
            print('selected table details -> ')
            print('.'*140)
            for k in tup:
                print('%20s'%k,end=' ')
            print()
            print('.'*140)
            
            for i in cur:
                for j in i:
                    print('%20s'%j,end='')
                print()

            
            print()
            print('select seach mode ')
            print('''1-using where
2-using between
3-for exit
''')
            op=input('enter you choice : ')
            while True:
                    if op[0]=='1':
                        print()
                        print('enter ')
                        print("1- for 'and '")
                        print("2- for 'or' ")
                        ch=input('enter choice : ')
                        if ch[0]=='1':
                            print()
                            print('enter the two column where condition applied for selecting one by one')
                            for i in range(len(tup)):
                                print('enter ',i,' for ',tup[i])
                            ch2=int(input('enter choice 1 : '))
                            ch3=int(input('enter chice 2 : '))
                            print()
                            print('now enter the detail of ',tup[ch2],' ',tup[ch3],' which you want to find details ')
                            print("..................................please enter string in quotes('')............................................. ")
                            ch4=input('enter details of '+tup[ch2]+' '+tup2[ch2]+' : ')
                            ch5=input('enter details of '+tup[ch3]+' '+tup2[ch3]+' : ')
                            print()
                            cur.execute('select * from '+tb+' where '+tup[ch2]+'='+ch4+' and '+tup[ch3]+'='+ch5)
                            print('selected record details are : ')
                            print('.'*140)
                            for k in tup:
                                print('%20s'%k,end=' ')
                            print()
                            print('.'*140)
                            for i in cur:
                                for j in i:
                                    print('%20s'%j,end=' ')
                                print()
                            print()
                            print('#'*60)
                            chl=input('want to seach more y/n : ')
                            print('#'*60)
                            print()
                            if chl.lower()=='n':
                                break
                        elif ch[0]=='2':
                            print()
                            print('enter the two column where condition applied for selecting one by one')
                            for i in range(len(tup)):
                                print('enter ',i,' for ',tup[i])
                            ch2=int(input('enter choice 1 : '))
                            ch3=int(input('enter chice 2 : '))
                            print()
                            print('now enter the detail of ',tup[ch2],' ',tup[ch3],' which you want to find details ')
                            print("..................................please enter string in quotes('')............................................. ")
                            ch4=input('enter details of '+tup[ch2]+' '+tup2[ch2]+' : ')
                            ch5=input('enter details of '+tup[ch3]+' '+tup2[ch3]+' : ')
                            print()
                            cur.execute('select * from '+tb+' where '+tup[ch2]+'='+ch4+' or '+tup[ch3]+'='+ch5)
                            print('selected record details are : ')
                            print('.'*140)
                            for k in tup:
                                print('%20s'%k,end=' ')
                            print()
                            print('.'*140)
                            for i in cur:
                                for j in i:
                                    print('%20s'%j,end=' ')
                                print()
                            print()
                            print('#'*60)
                            chl=input('want to seach more y/n : ')
                            print('#'*60)
                            print()
                            if chl.lower()=='n':
                                break
                            
                    elif op[0]=='2':
                        print()
                        print('enter ')
                        print("1- for 'and '")
                        print("2- for exit ")
                        ch=input('enter choice : ')
                        if ch[0]=='1':
                            print()
                            print('enter the one column where condition applied for selecting one by one')
                            for i in range(len(tup)):
                                print('enter ',i,' for ',tup[i])
                            ch2=int(input('enter choice 1 : '))
                            print()
                            print('now enter the detail of ',tup[ch2],' which you want to find details ')
                            print("..................................please enter string in quotes('')............................................. ")
                            ch4=input('enter lower range details of '+tup[ch2]+' for start searching range'+' : ')
                            ch5=input('enter upper range details of '+tup[ch2]+' for ending searching range : ')
                            print()
                            cur.execute('select * from '+tb+' where '+tup[ch2]+' between '+ch4+' and '+ch5)
                            print('selected record details are : ')
                            print('.'*140)
                            for k in tup:
                                print('%20s'%k,end=' ')
                            print()
                            print('.'*140)
                            for i in cur:
                                for j in i:
                                    print('%20s'%j,end=' ')
                                print()
                            print()
                            print('#'*60)
                            chl=input('want to seach more in same table  y/n : ')
                            print('#'*60)
                            print()
                            if chl.lower()=='n':
                                break
                        elif ch[0]=='2':
                            break
                    elif op[0]=='3':
                        break
                
            ask2=input('wants to search more y/n : ')
            print()
            if ask2.lower()=='n':
                break
                    
                   
        except:
            print()
            print('!'*50)
            print('wrong input')
            print('!'*50)
            print()
            ask=input('want to continue or not y/n : ')
            print()
            if ask.lower()=='n':
                break


   

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
11- to search record
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

    elif ch=='11':
        print('_'*40)
        search_operation()
        print('_'*40)
        
    elif ch=='0':
        exit()
    else:
        print('_'*40)
        print('sorry no result found')
        print('_'*40)
        print()
        

        
        
# end of the project


# output
    
    
            
                            
            
        
    

        

                
