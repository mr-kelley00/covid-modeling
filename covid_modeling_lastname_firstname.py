# Simple COVID-19 Exponential Growth Simulator Template -- Ryan K. - 04/07/2020, 1:04PM Version 1.0

import time

num_infected = 0  
num_days = 0
num_simulate = 0
num_deaths = 0 

print("Currently, the number of infections of COVID-19 will double every six days.\n")


time.sleep(3)

num_infected = int(input("Please enter the current number of infections as an integer.  Do not use commas or spaces.  Type the number and press enter."))
num_simulate = int(input("How many days do you want to simulate?  Do not use commas or spaces.  Type the number and press enter.")) 


print(f"There are currently {num_infected:,} people in the U.S. and you will simulate for {num_simulate} days.")

while num_days <= num_simulate:
    
    num_infected += num_infected
    num_deaths = round(num_infected * 0.023)
    print(f"On day {num_days} there are {num_infected:,} infected people.")
    print(f"Approximately {num_deaths:,} will die from COVID-19.") 
    num_days += 6  
    time.sleep(3)   

# Write a print() statement that shows the total number of infections and the number of deaths after running your simulation.  

    
    
    
