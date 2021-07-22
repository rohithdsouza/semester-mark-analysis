
from bs4 import BeautifulSoup
import requests
import csv

regno =[]
students = []

for i in range (160): #Pad number with zeros (left padding, width 3) eg: 053
    regno.append('{:0>3}'.format(i))

class student : #student object with attributes name, marks, avg
    def __init__(self,name,student_marks,average):
        self.name = name 
        self.student_marks = student_marks 
        self.average = average

#web scrap from 0-160 Roll No
for i in range (160) :
    html_text = requests.get('http://www.adhiyamaan.ac.in/anew/result1.php?regno=AC18UCS' + regno[i] + '&submit=submit').text
    soup = BeautifulSoup(html_text, 'lxml')
    string_content = soup.get_text()
    stringarray = string_content.split()
    #print(string_content)

    incorrect = False
    correct = False

    class studentMarks : #class containing subject wise marks 
        def __init__(self, name, subname , marks):
            self.name = name
            self.subname = subname
            self.marks = marks
        def __repr__(self):
            return "%s : %s : %d" % (self.name,self.subname,self.marks)

    marks = []
    name = ''
    subname = ['Mobile Application Development','Compiler Design','Data Warehousing and Data Mining','Web Programming','Artificial Intelligence','Software Project Management']


    for index , item in enumerate(stringarray) :
        if item == '2020No' or item == 'W' or item == 'TUMATI':
            incorrect = True
            break
        if item == 'Name' and name =='' : #fetch each name
            name = stringarray[index + 2]
            i = index + 3
            while stringarray[i] != "Reg.No:" : #second name
                    name += " "+ stringarray[i]
                    i = i+1
                    
        if  item == 'PASS' or item == 'FAIL' or item == 'AAA': #fetching marks
                marks.append( int (stringarray[index - 1]))
                correct = True
        # else :
        #     incorrect = True
        #     break

#to calculate average of a list of marks
    def average(student_marks) :
            sum =0
            for i in range (6) :
                        sum = sum + student_marks[i].marks
            average = sum / 6
            return average


    if incorrect == False and correct == True :
        student_marks = []
        for i in range (6) :
           #print (name)
            student_marks.append(studentMarks(name, subname[i],marks[i])) #subject wise marks list
        average = average(student_marks)
        # print('Name : ',name)
        # print("Average : ",average(student_marks))
        students.append(student(name,student_marks,average)) #appending only average / name / total

#sort the list to find rank
newlist = sorted(students, key=lambda x: x.average, reverse=True)
c =0
for i,j in enumerate ( newlist ):
    c = c+1
    print (c," ",newlist[i].name," : ",newlist[i].average) 

# output the student ranklist as CSV file    
filename = "sem6RankListCSE.csv"
with open(filename, 'w') as f:
       writer = csv.writer(f)
       for item in students:
            writer.writerow([item.name, item.student_marks, item.average])

#output subject wise mark list of students
filename = "sem6SubjectMarkListCSE.csv"
with open(filename , 'w') as g :
    writer = csv.writer(g)
    for item in studentMarks:
        writer.writerow([item.name,item.subname,item.marks])

   