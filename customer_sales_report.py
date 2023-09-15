import csv
file1 = open('sales.csv','r')
sales = csv.reader(file1, delimiter=',')
outfile = open('salesreport.csv','w')
outfile.write('Customer ID, Total')
next(sales) 

customer_id = ' '
total = 0.0

for rec in sales:
    if customer_id == rec[0]:
        total += float(rec[3]) + float(rec[4]) + float(rec[5])

    else: 
        outfile.write(f'{customer_id}, ${total:.2f}\n')
        customer_id = rec[0]
        total = float(rec[3]) + float(rec[4]) + float(rec[5])
        #print(customer_id)
        #print(f'${total:.2f}\n')

file1.close()
outfile.close()  