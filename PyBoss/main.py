import csv
import os


#Get path of csv1
filepath = os.path.join('..','..','10-16-2017-GW-Arlington-Class-Repository-DATA','Homework','03-Python','Instructions','PyBoss','raw_data','employee_data1.csv')

emp_id = []
fname = []
lname =[]
dob = []
ssn = []
state = []

states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#read csv
with open(filepath,newline='') as file:
	fileread = csv.reader(file,delimiter=',')
	#skip header row
	next(fileread,None)
	for row in fileread:
		#emp_id
		emp_id.append(str(row[0]))
		#split the name into first & last
		name = row[1].split(' ')
		#first name
		fname.append(name[0])
		#last name
		lname.append(name[1])
		#DOB
		dob.append(str(row[2][5:7])+'/'+str(row[2][-2:])+'/'+str(row[2][0:4]))
		#SSN
		ssn.append('***-**-'+str(row[3][-4:]))
		#State
		state.append(states[row[4]])

#zip list
newcsv = zip(emp_id,fname,lname,dob,ssn,state)
#for row in newcsv:
#	print(row)

#create new csv
outputfile = os.path.join('..','..','10-16-2017-GW-Arlington-Class-Repository-DATA','Homework','03-Python','Instructions','PyBoss','raw_data','results.csv')

#write to csv
with open(outputfile,'w',newline='') as newfile:
	newfilewriter = csv.writer(newfile, delimiter=',')
	newfilewriter.writerow(['EmpID','FirstNm','LastNm','DOB','SSN','State'])
	for row in newcsv:
		newfilewriter.writerow(row)
	
