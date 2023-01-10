## 과제 안 내신 분..?
import sys

student_list = list(range(1,31))
for i in range(28) :
    called = int(input())
    student_list.remove(called)

for missed in student_list :
    print(missed)