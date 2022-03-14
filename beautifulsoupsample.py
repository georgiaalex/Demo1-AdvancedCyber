# Friendly Hal’s Used Cars has four sales people named Pam, Leo, Kim and Bob.
# Create a function called print_car_sales to accept values for the number of cars sold
# by each salesperson in a month, and create a bar chart that illustrates sales, similar
# to the following one.
# Create a function called test_print_car_sales to test your function. Ensure you
# capture the user input and call the relevant function, in order to test your code.

def print_car_sales(Pam_no,Leo_no,kim_no,bob_no):
    sales_list = []
    sales_list.append(Pam_no)
    sales_list.append(Leo_no)
    sales_list.append(kim_no)
    sales_list.append(bob_no)
    for values in sales_list:
        print(values* 'X')


pam_no = int(input())
kevin_no = int(input())
bob_no = int(input())
leo_no = int(input())


print_car_sales(pam_no,kevin_no,bob_no,leo_no)