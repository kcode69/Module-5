#The CSU Global Bookstore has a book club that awards points to its students based on the number of books 
# purchased each month. The points are awarded as follows:
#    • If a customer purchases 0 books, they earn 0 points. 
#    • If a customer purchases 2 books, they earn 5 points. 
#    • If a customer purchases 4 books, they earn 15 points. 
#    • If a customer purchases 6 books, they earn 30 points. 
#    • If a customer purchases 8 or more books, they earn 60 points. 
# Write a program that asks the user to enter the number of books that they have purchased this month and then 
# display the number of points awarded.



customer_Points = 0 #Customer Points
customer_Books = 0.0 #Number of books being purchased
control = True #Control variable for while loop initially True, False to exit while

while control is True: #while loop until control is False 
    try:
    #is customer_Books and integer
        customer_Books = int(input("Hello! How many books have you purchased this month? "))

    #when input is not an integer    
    except ValueError:
        print("Opps! That was an invalid entry. Try again.")
    
    else:
        #customer_Books is a valid number, control = False to exit while
        control = False

        if customer_Books < 2:
            customer_Points = 0

        if customer_Books >= 2 and customer_Books < 4:
            customer_Points = 5

        if customer_Books >= 4 and customer_Books < 6:
            customer_Points = 15

        if customer_Books >= 6 and customer_Books < 8:
            customer_Points = 30

        if customer_Books >= 8:
            customer_Points = 60


print("You have earned", customer_Points, "points this month.")