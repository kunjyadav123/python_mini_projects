# Mini Projects :  Cafe Management System : 

# Defining menu of Restraunt : 

menu = {
    "Pizza" : 50,
    "Pasta" : 60,
    "Burger": 70,
    "Salad" : 80,
    "Coffee": 100
}


 
print("WELCOME TO CHAR CHAWANNI RESTRAUNT!")
print("Pizza : 50\nPasta : 60\nBurger : 70\nSalad : 80\nCoffee : 100")

Order_total = 0

item_1 = input("Enter name of item you want to order : ")
if item_1 in menu: 
  Order_total += menu[item_1]
  print(f"Your item {item_1} has been added to your order ")

else:
  print(f"Ordered item{item_1} is not available yet")

another_order  = input("Do you want to add another item? (Yes/No)")  
if another_order  == "Yes":
  item_2 = input("Enter name of second order : ")
  if item_2 in menu :
    Order_total += menu[item_2]
    print(f"Your item {item_2} has been added to your order ")
  else :
    print(f"Ordered item {item_2} is not available yet ")

print(f"The total amount of ordered item is to pay { Order_total }")

