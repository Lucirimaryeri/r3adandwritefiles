import csv
customers = open('customers.csv','r')
customer_file = csv.reader(customers)
outfile = open('customer_country.csv', 'w')
outfile.write('Full Name,Country\n')
next(customer_file)

counter = 0

for rec in customer_file:
    f_name = rec[1].rstrip('\n') #to be eff. do not use variables. so for concat use rec1,2,etc)
    l_name = rec[2]
    country = rec[4]
    fullname = f_name + ' ' + l_name
    outfile.write(fullname + ' , ' +  country + '\n')
    counter += 1

outfile.close()

print(f'total number of customers: {counter}')