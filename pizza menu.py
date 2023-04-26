#Jordan Chambers
import datetime
#define price variable
S = 9.99
M = 12.99
L = 14.99
E = 17.99
TAX = 0.055

#define another order variable

number_of_pizzas = 0
pizza_cost = 0
tax_amount = 0
order_total = 0
def main():
    another_order = True
    while another_order:
        get_user_data()
        calculate()
        display()
        another_order = input("\nAnother Order? (Y/N):")
        if another_order.upper() != "Y":
            another_order = False

def get_user_data():
    global pizza_size, number_of_pizzas
    number_of_pizzas = int(input("Number_of_pizzas: "))
    pizza_size = str(input("Enter pizza_size: S, M, L, E: "))
   

def calculate():
    global pizza_cost, tax_amount, order_total
    if pizza_size == 'S' or pizza_size == 's':
        pizza_cost = number_of_pizzas * S
    elif pizza_size == 'M' or pizza_size == 'm':
        pizza_cost = number_of_pizzas * M
    elif pizza_size == 'L' or pizza_size == 'l':
        pizza_cost = number_of_pizzas * L
    else:
        pizza_cost = number_of_pizzas * E
    tax_amount = pizza_cost * TAX
    order_total = pizza_cost + tax_amount

def display():
    print('\n******** Chambers Pizza Shop *******')
    print('Pizza:     $'+ format(pizza_cost, '10,.2f'))
    print('Sales Tax: $'+ format(tax_amount, '10,.2f'))
    print('Total:     $'+ format(order_total, '10,.2f'))
    print('Thank you for stopping in!')

main()        
