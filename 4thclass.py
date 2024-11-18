'''tree1=float(input("Enter height of tree1 : "))
price1=float(input("Enter price of tree1 : "))
tree2=float(input("Enter height of tree2 : "))
price2=float(input("Enter price of tree2 : "))
tree3=float(input("Enter height of tree3 : "))
price3=float(input("Enter price of tree3 : "))
tree4=float(input("Enter height of tree4 : "))
price4=float(input("Enter price of tree4 : "))
Total=tree1+tree2+tree3+tree4
avr_height=Total/4
Total_price=price1+price2+price3+price4
Discount_price=Total_price-Total_price*0.1
print(f"Total Price is : {Total_price} And Your Discount price is {Discount_price}")'''
# Taking total amount as input from the user
amount= int(input("Please Enter the amount for withdrawl : "))
# Calculating the number of 100 notes for each other denomination
notes_of_100=amount//100
remaining_after_100=amount%100

# Calculating the number of 50 notes for each other denomination
notes_of_50=remaining_after_100//50
remaining_after_50= remaining_after_100%50
# Calculating the number of 10 notes for each other denomination
notes_of_10=remaining_after_50//10
remaining_after_10=remaining_after_50%10
# Calculating the number of 5 notes for each other denomination
notes_of_5=remaining_after_10//5
remaining_after_5=remaining_after_10%5

#Printing the number of notes
print("notes of 100 taka: ",notes_of_100)
print("notes of 50 taka: ",notes_of_50)
print("notes of 10 taka: ",notes_of_10)
print("notes of 5 taka: ",notes_of_5)
print("Remaining Amount: ",remaining_after_5)