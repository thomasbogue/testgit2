name = "Tom"
condition = "y"
while condition == "y":
    print(f"Hi {name}! It's Adam")
    condition = input("Would you like to see another greeting? (type 'y' for yes, type 'n' for no) ")
    if condition == "y":
        name = input("Who am I sending this greeting to? (type in their name) ")