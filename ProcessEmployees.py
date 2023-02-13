'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

infile=open('employee_data.csv','r')
employees=csv.reader(infile, delimiter=',')

#create an empty dictionary
es_dict={}
dep='Marketing'
title='CSR'
#use a loop to iterate through the csv file

for employee in employees:

    #check if the employee fits the search criteria
    if employee[3]==dep and employee[4]==title:
        print('Manager Name:',employee[1],employee[2],'Current Salary:',employee[5])

    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout

for employee in employees:
    if employee[3]==dep and employee[4]==title:
        print('Manager Name:',employee[1],employee[2],'Current Salary:',employee[5]*1.10)

          
        

        
    
