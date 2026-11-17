my_number = 42
your_guess = 0
while (your_guess != my_number):
    your_input = input("Guess my number: ")
    your_guess = int(your_input)
    if your_guess < my_number:
        print("guess higher!")
    elif your_guess > my_number:
        print("guess lower!")
print("You got it!")

