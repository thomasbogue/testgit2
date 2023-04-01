import random

def main():
    number_one =  random.randint(1,int(input("Select an upper bound for the first random number: ")))
    number_two = random.randint(1, int(input("Select an upper bound for the second random number: ")))
    product = number_one * number_two
    print(f"Your two random numbers multiplied equals {product}")

main()