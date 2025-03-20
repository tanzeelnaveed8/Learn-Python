import random 

print("Welcome to the Number Guessing Game!")
print("You have 5 attempts to guess the number between 50 and 100.")
print("Let's start the game!\n")   

# Generate a random number
number_guess = random.randint(50, 100)

# Initialize attempt counter
chances = 0

while chances < 5:
    try:
        # Take user input
        guess = int(input("Enter your guess: "))

        chances += 1  # Increment attempt counter

        if guess == number_guess:
            print(f"🎉 Congratulations! You guessed the number in {chances} attempts.")
            break  # Exit loop if guessed correctly
        elif guess < number_guess:
            print("📉 Your guess is too low, try again!")
        else:
            print("📈 Your guess is too high, try again!")

    except ValueError:
        print("⚠️ Invalid input! Please enter a number between 50 and 100.")

# If all attempts are used
if chances == 5 and guess != number_guess:
    print(f"❌ Opps! The correct number was {number_guess}. Better luck next time!")
