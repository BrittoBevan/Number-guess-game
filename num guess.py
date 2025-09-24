import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")
i=True
while i:
    sn=random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess <= (sn-5):
                print("Too low! Try again.")
            elif guess >= (sn+5):
                print("Too high! Try again.")
            elif guess !=sn:
                if guess in range(sn-5,sn+5):
                    print("Near it")
            else:
                print(f"Congratulations! You guessed the number in {attempts} tries.")
                break
        except ValueError:
            print("Please enter a valid number.")
    a=input("Do u want to continue 'y'/'n': ")
    if a=="n":
        break

