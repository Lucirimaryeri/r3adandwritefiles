import csv
employee = open('EmployeePay.csv','r')
employee_file = csv.reader(employee)
outfile = open('Employee_bonus.csv', 'w')
outfile.write('Full Name, Salary, Bonus, Total Pay\n')
next(employee_file)

for rec in employee_file:
    f_name = rec[1].rstrip('\n') 
    l_name = rec[2]
    salary = float(rec[3])
    bonus = float(rec[4]) * salary
    total_pay = float(rec[3] + rec[4])

    fullname = rec[1] + ' ' + rec[2]

    print('First Name: ', f_name)
    print('Last Name: ', l_name)
    print(f'Salary:  ${salary:10,.2f}')
    print(f'Bonus:  ${bonus:10,.2f}')
    print(f'Total Pay:  ${total_pay:10,.2f}')
    print()

outfile.close()
