import csv
import os


#Get path of csv1
filepath = os.path.join('..','..','10-16-2017-GW-Arlington-Class-Repository-DATA','Homework','03-Python','Instructions','PyBank','raw_data','budget_data_1.csv')

i=[]
j=[]
rev_incr = 0
rev_decr = 0


#read csv
with open(filepath,newline='') as file:
	fileread = csv.reader(file,delimiter=',')
	#skip header row
	next(fileread,None)
	for row in fileread:
		#Months
		i.append(str(row[0]))
		#Revenue
		j.append(int(row[1]))
		#Greatest increase
		if int(row[1]) > rev_incr:
			rev_incr_mo = row[0]
			rev_incr = int(row[1])
		#Greatest decrease
		if int(row[1]) < rev_decr:
			rev_decr_mo = row[0]
			rev_decr = int(row[1])
		
	
print('Financial Analysis')
print('-------------------------------')
print('Total Months:  ' + str(len(i)))
print('Total Revenue:  $' + str(sum(j)))
print('Average Change in Revenue:  $' + str(int(sum(j)/len(i))))
print('Greatest Increase in Revenue:  ' + rev_incr_mo + ' $' +str(rev_incr))
print('Greatest Decrease in Revenue:  ' + rev_decr_mo + ' $' +str(rev_decr))

outputfile = os.path.join('..','..','10-16-2017-GW-Arlington-Class-Repository-DATA','Homework','03-Python','Instructions','PyBank','raw_data','results.txt')

with open(outputfile,'w') as newfile:
	newfile.write('Financial Analysis\n')
	newfile.write('-------------------------------\n')
	newfile.write('Total Months:  ' + str(len(i))+'\n')
	newfile.write('Total Revenue:  $' + str(sum(j))+'\n')
	newfile.write('Average Change in Revenue:  $' + str(int(sum(j)/len(i)))+'\n')
	newfile.write('Greatest Increase in Revenue:  ' + rev_incr_mo + ' $' +str(rev_incr)+'\n')
	newfile.write('Greatest Decrease in Revenue:  ' + rev_decr_mo + ' $' +str(rev_decr)+'\n')
	
	
	
	