from datetime import datetime
 
# datetime object containing current date and time
now = datetime.now()
 
# dd/mm/YY H:M:S
#dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
 
#mm/dd/YY
#%I stands for 12 hour clock
#%p stands for AM or PM
ust_string = now.strftime("%m/%d/%Y %I:%M:%S %p")
print("It is currently: ", ust_string)
