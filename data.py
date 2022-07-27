# Name={"Joe","Jill","Rick","james","Sandy","Gomer","Lance","Kevin","Ron","Valerie"}

# Amount={2000,3000,4000,6000,8000,900,200,5000,-20000,-700}

# data ={"Name":["Joe","Jill","Rick","james","Sandy","Gomer","Lance","Kevin","Ron","Valerie"],
# "Amount":[2000,3000,4000,6000,8000,900,200,5000,-20000,-700]}
# print
# 1st install tabulate to print data in table form in python
# Use this line to install --> pip install tabulate
from tabulate import tabulate

#create Table using Dictionary
# create data dict 
di={"Joe":2000,"Jill":3000,"Rick":4000,"james":6000,"Sandy":8000,
    "Gomer":900,"Lance":200,"Kevin":5000,"Ron":-20000,"Valerie":-700}

#create 2 new dict to store less or more than 1000 value
less_1000=dict()
more_1000=dict()

# show the data in table
print(tabulate(di.items(),headers=headers))
headers=["Name","Amount"]

#for loop to iterate 1 by 1 item from dict 
for k,v in di.items():
  if v<0:                 # check the negative value in dict
    di.update({k:abs(v)}) #abs function use change -ve to +ve value and then update dict


for k,v in di.items():
  if v<1000:                 #check for less value 
    # print("less")
    less_1000.update({k:v})   #check for less value and update dict
  else:                       #check for more value 
    # print("more") 
    more_1000.update({k:v})   #check for less value and update dict
#print the table less then 1000 amount
print("============================")
print("Less then 1000 amount")
print(tabulate(less_1000.items(),headers=headers))
#print the table less then 1000 amount
print("============================")
print("More then 1000 amount")
print(tabulate(more_1000.items(),headers=headers))
