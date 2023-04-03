print("Hello User!")
yourname = str(input("What is your name?"))
print("Hello " +yourname)
their_fave_number = int(input("What is your favorite number?"))
my_fave_number = 87
if (my_fave_number > their_fave_number):
    print("My favorite number is " +(int(my_fave_number)), "which is higher than yours.")
elif (my_fave_number < their_fave_number):
    print("My favorite number is " +(int(my_fave_number)), "which is less than yours.")
elif(my_fave_number == their_fave_number):
    print("Our favorite numbers are the same!")


