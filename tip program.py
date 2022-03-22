#tip program

meal_total = input("Enter you meal total amount here: $")

#tax = 8% and tip = %15 
meal_total = float(meal_total)
tax = 0.080 * meal_total
tip = 0.15 * meal_total
total = meal_total + tax + tip


response = input(f'''You entered: ${meal_total}
Confirm by entering: Yes ''')
response = response.lower()

if response == "yes":
    print("Thank you for your purchase at Bob's Lobster Shack")
    print("--------------------")
    print(f"Meal total: ${meal_total}")
    print(f"Tip: ${tip}")
    print(f"Tax: ${tax}")
    print("--------------------")
    print(f"Your total: ${total}")
    print("--------------------")
else:
    print("Try again later.")
    print(':(')
    quit()