from collections import namedtuple
# Car = namedtuple('Car','Price Mileage Colour Class')
# xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# print (xyz)
# print (xyz.Class)


a = int(input())
s = input().split()
sum = 0
for i in range(a):
    students = namedtuple('students',s)
    s1 ,s2,s3,s4 = input().split()
    student = students(s1 ,s2,s3,s4)
    sum += int(student.MARKS)

print(  '{:.2f}'.format(sum/a))