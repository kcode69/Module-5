# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
# The program should first ask for the number of years. The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask 
# the user for the inches of rainfall for that month. After all iterations, the program should display the number 
# of months, the total inches of rainfall, and the average rainfall per month for the entire period.

# import calendar month names
import calendar 

#string for month names from caledar
list_of_months = list(calendar.month_name)[1:]

print("Let's calculate the average rainfall for a period of years")

#number of years to be calculated
num_Year = int(input('Enter the number of years? '))

#initial values for total rainfall and months to 0
total_Ranifall = 0.0
total_Months = 0

for i in range(0, num_Year):
    
    for j in range(0, 12):
        total_Months += 1
        print("Enter the amount of rainfall for", list_of_months[j], "in year", i+1)
        total_Ranifall = total_Ranifall + float(input())

print("Total number of months is:       ", total_Months)
print("Total amount of rainfall is      ","{:.2f}".format(total_Ranifall))
print("The average rainfal per month is:", "{:.2f}".format(total_Ranifall/total_Months))
        



