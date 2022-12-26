#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[2]:


db=sqlite3.connect('Student Database.db')


# In[3]:


cursor=db.cursor()


# In[57]:


cursor.execute('create table student_data(phone_number int primary key,email_id text,course_name text,fees_paid int)')


# In[58]:


cursor.execute("insert into student_data(phone_number,email_id,course_name,fees_paid)values(9795862210,'Rudrapratapsingh176@gmail.com','Data Science',110000),(9453083351,'Preetisingh1204@gmail.com','Data Analysis',150000),(9415923471,'GajendraSingh534@gmail.com','Marketing',50000),(9648642210,'rudrapratapsingh7979@gmail.com','Data Mining',200000)")
db.commit()
print(cursor.rowcount,'Rows inserted')


# In[7]:


cursor.execute('drop table students_details')


# In[59]:


column=cursor.execute('select*from student_data')


# In[60]:


for row in column:
    print(row)


# In[61]:


with open ('DT_Students.csv',"r") as file:
    no_records=0
    for row in file:
        cursor.execute('insert into student_data values(?,?,?,?)',row.split(","))
        db.commit()
        no_records+=1
  


# In[62]:


sql=cursor.execute('select * from student_data  ')
for row in sql:
    print(row)


# In[63]:


sql=cursor.execute('select * from student_data where course_name= "Data Science" ')
for row in sql:
    print(row)


# In[64]:


sql=cursor.execute('select * from student_data where course_name= "Data Science" and fees_paid<=50000')
for row in sql:
    print(row)


# In[65]:


cursor.execute('delete from student_data where phone_number=9415923471')
db.commit()


# In[66]:


sql=cursor.execute('select * from student_data  ')
for row in sql:
    print(row)


# In[67]:


sql=cursor.execute('select * from student_data order by fees_paid')
for row in sql:
    print(row)


# In[19]:


sql=cursor.execute('select * from student_data order by fees_paid desc ')
for row in sql:
    print(row)


# In[20]:


cursor.execute('update student_data set course_name="Data Science" where phone_number=9648642210')
db.commit()


# In[21]:


sql=cursor.execute('select * from student_data  ')
for row in sql:
    print(row)


# In[22]:


result=cursor.execute('select * from student_data where course_name="Digital Marketing" and phone_number=9988776613')
for row in result:
    print(row)


# In[23]:


result=cursor.execute('select * from student_data where course_name="Digital Marketing" and fees_paid>=30000')
for row in result:
    print(row)


# In[24]:


cursor.execute('update student_data set fees_paid=50000 where phone_number in(9988776622,9988776615)')
db.commit()


# In[25]:


sql=cursor.execute('select phone_number,fees_paid from student_data where phone_number in(9988776622,9988776615)')
for row in sql:
    print(row)


# In[26]:


cursor.execute('update student_data set fees_paid=140000 where phone_number between 9988776618 and 9988776622')
db.commit()


# In[27]:


sql=cursor.execute('select * from student_data  ')
for row in sql:
    print(row)


# In[28]:


sql=cursor.execute('select min(fees_paid) from student_data')
for row in sql:
    print(row)


# In[29]:


sql=cursor.execute('select max(fees_paid) from student_data')
for row in sql:
    print(row)
  


# In[30]:


import sqlite3


# In[31]:


db=sqlite3.connect("students_course.db")


# In[32]:


cursor=db.cursor()


# In[36]:


cursor.execute('create table course(courseid int primary key,course_name text,duration int)')


# In[37]:


cursor.execute('create table students(roll_no int primary key,student_name text,age int,courseid int,foreign key (courseid)references course(courseid))')


# In[35]:


cursor.execute('drop table students')
cursor.execute('drop table course')


# In[38]:


cursor.execute('insert into course values(78,"Data Science",12),(56,"python",8),(101,"Database",7)')
cursor.execute('insert into students values(1,"jack",22,78),(2,"john",21,56),(3,"Rudolf",18,78),(4,"Jim",21,56)')
db.commit()


# In[39]:


result=cursor.execute("select*from course")
for row in result:
    print(row)


# In[40]:


result=cursor.execute("select*from students")
for row in result:
    print(row)


# In[41]:


result=cursor.execute("select*from course where courseid=(select courseid from students where course_name='Data Science')")
for row in result:
    print(row)


# In[42]:


result=cursor.execute("select*from students where courseid=(select courseid from course where course_name='python')")
for row in result:
    print(row)


# In[74]:


cursor.execute('create table students_details(phone_number int primary key,student_name text,enrolled_date int,marks int)')


# In[69]:


cursor.execute('drop table students_details')


# In[75]:


with open('Students_details.csv','r') as file:
    no_records=0
    for rows in file:
        cursor.execute('insert into students_details values(?,?,?,?)',rows.split(","))
        db.commit()
        no_records+=1
        


# In[76]:


result=cursor.execute('select*from students_details')
for rows in result:
    print(rows)


# In[77]:


result=cursor.execute('select*from student_data')
for rows in result:
    print(rows)


# In[78]:


sql='select student_data.phone_number,students_details.enrolled_date,students_details.marks,students_details.student_name from student_data inner join students_details on student_data.phone_number=students_details.phone_number'
results=cursor.execute(sql)
for rows in results:
    print(rows)


# In[81]:


sql='select student_data.phone_number,students_details.enrolled_date,students_details.marks,students_details.student_name from students_details left join student_data on student_data.phone_number=students_details.phone_number'
results=cursor.execute(sql)
for rows in results:
    print(rows)


# In[82]:


sql='select student_data.phone_number,students_details.enrolled_date,students_details.marks,students_details.student_name from student_data right join students_details on student_data.phone_number=students_details.phone_number'
results=cursor.execute(sql)
for rows in results:
    print(rows)


# In[ ]:


while True:
    try:
        phone_number=int(input('Enter Your Phone Number-'))
        if len(str(phone_number)) !=10:
            print('phone_no.is not 10 digits')
            continue
        else:
            result=cursor.execute('select*from student_data')
            for rows in result:
                if rows[0]==phone_number:
                    print('Email id-',rows[1])
                    print('Course-',rows[2])
                    print('Fees_paid',rows[3])
                    break
    except:
        print('Phone Number Should br Numeric')
        continue


# In[ ]:




