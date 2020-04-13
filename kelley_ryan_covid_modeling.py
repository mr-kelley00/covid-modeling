# Simple COVID-19 Exponential Growth Simulator Template -- Ryan K.  -- 04/13/20 -- 11:16am -- Version 0.6

import time

num_infected_ppl = 0 
current_day = 0
days_sim = 0 
num_deaths_ppl = 0 

print("This program will model potential COVID-19 infections and deaths in the U.S.  Right now, the number of infections will double every six days.\n")
time.sleep(4)

num_infected_ppl = int(input("How many people are currently infected?  Please enter an INTEGER number with no commas.  Then press enter.   "))
days_sim = int(input("How many days of infection growth do you want to simulate?  Please enter an INTEGER number with no commas.  Then press enter.   "))

print(f"The current number of people infected with COVID-19 is {num_infected_ppl:,} and you will simulate {days_sim} days worth of infection growth.\n")


while current_day <= days_sim:
    
    num_infected_ppl += num_infected_ppl
    num_deaths_ppl = round(num_infected_ppl * 0.023)
    
    # Write a print() statement that displays the number of infected people and the number of deaths. 
    current_day += 6  
    # Use time.sleep() to pause for a few seconds to allow the user to read the instructions.  

# Write a print() statement that shows the total number of infections and the number of deaths after running your simulation.  

    
    
    
