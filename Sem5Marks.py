from bs4 import BeautifulSoup
import requests
import csv
regno =[]
students = []

#converting 0 to 000 -> Pad number with zeros (left padding, width 2)
for i in range (160):
    regno.append('{:0>3}'.format(i))

#each student object - Name , Marks , Average
class student :
    def __init__(self,name,student_marks,average):
        self.name = name 
        self.student_marks = student_marks 
        self.average = average
        
        # def average(self) :
        #     sum =0
        #     for i in range (9) :
        #             sum = sum + self.student_marks[i].marks
        #     self.average = sum / 9
        

for i in range (3) :
    html_text = requests.get('http://www.adhiyamaan.ac.in/anew/result1.php?regno=AC18UCS' + regno[i] + '&submit=submit').text
    soup = BeautifulSoup(html_text, 'lxml')
    string_content = soup.get_text()
    stringarray = string_content.split()
    #print(string_content)
    incorrect = False
    correct = False

    class studentMarks :
        def __init__(self, subname , marks):
            self.subname = subname
            self.marks = marks
        def __repr__(self):
            return "%s : %d" % (self.subname,self.marks)

    marks = []
    name = ''
    subname = ['PROBABILITY AND QUEUEING THEORY','MICROPROCESSORS AND MICROCONTROLLERS','OBJECT ORIENTED ANALYSIS AND DESIGN','THEORY OF COMPUTATION','ENGINEERING ETHICS AND HUMAN VALUES','C# and .NET PROGRAMMING','MICROPROCESSORS AND MICROCONTROLLERS LABORATORY','OBJECT ORIENTED ANALYSIS AND DESIGN LABORATORY','EMPLOYABILITY SKILL LABORATORY']

    for index , item in enumerate(stringarray) :
        if item == '2020No' or item == 'W' or item == 'TUMATI':
            incorrect = True
            break
        if item == 'Name' and name =='' :
            name = stringarray[index + 2]
            i = index + 3
            while stringarray[i] != "Reg.No:" :
                    name += " "+ stringarray[i]
                    i = i+1
                    
        if  item == 'PASS' or item == 'FAIL' :
                marks.append( int (stringarray[index - 1]))
                correct = True
        # else :
        #     incorrect = True
        #     break

    def average(student_marks) :
            sum =0
            for i in range (9) :
                        sum = sum + student_marks[i].marks
            average = sum / 9 
            return average

    if incorrect == False and correct == True :
        student_marks = []
        for i in range (9) :
           #print (name)
            student_marks.append(studentMarks(subname[i],marks[i]))
        average = average(student_marks)
        # print('Name : ',name)
        # print("Average : ",average(student_marks))
        students.append(student(name,student_marks,average))

newlist = sorted(students, key=lambda x: x.average, reverse=True)
c =0
for i,j in enumerate ( newlist ):
    c = c+1
    print (c," ",newlist[i].name," : ",newlist[i].average) 
filename = "test.csv"
with open(filename, 'w') as f:
        writer = csv.writer(f)
        for item in students:
            writer.writerow([item.name, item.student_marks, item.average])
   

    



