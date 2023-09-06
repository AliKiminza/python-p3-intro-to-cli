#!/usr/bin/env python3
def create_grade_report (student_grades):
    with open('/home/ali/Desktop/lectures/phase-3/python/python-p3-intro-to-cli/lib/grade_report.txt', 'w') as gr:
        for grade in student_grades:
            gr.write(grade+'\n')

if __name__ == '__main__':
    student_grades=[]
    grade = input("student name, grade:")
    while grade:
        student_grades.append(grade)

        grade = input("student name, grade:")
    create_grade_report(student_grades)
