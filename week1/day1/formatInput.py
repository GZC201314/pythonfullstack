# __author:gzc
# date:2018/8/20
name = input("name:")
age = input("age:")
salary = input("salary:")
if age.isdigit() and salary.isdigit():
    age = int(age)
    salary = int(salary)
    msg = '''
--------------infomation for %s---------
Name   : %s
Age    : %d
salary : %f
retirde: %s
''' % (name, name, age, salary, str(65 - age))
    print(msg)
else:
    exit("age must input digit");
