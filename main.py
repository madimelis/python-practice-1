name = input("Enter customer name: ")
item1 = input("Enter name of item 1: ")
price1 = float(input("Enter price of item 1 (KZT): "))
item2 = input("Enter name of item 2: ")
price2 = float(input("Enter price of item 2 (KZT): "))
people = int(input("Enter number of people: "))
subtotal = price1 + price2
tip = subtotal * 0.1
total = subtotal + tip
per_person = total / people
print("=" * 30)
print("          CAFE BILL           ")
print("=" * 30)
print(f"Customer : {name}")
print(f"Item 1 : {item1} - {price1} KZT")
print(f"Item 2 : {item2} - {price2} KZT")
print("-" * 30)
print(f"Subtotal : {subtotal} KZT")
print(f"Tip (10%) : {tip} KZT")
print(f"Total : {total} KZT")
print(f"Per Person: {per_person} KZT")
print("=" * 30)
print("Tip included: ", tip > 0)
print("Bill cover 5000 KZT: ", total > 5000) 
