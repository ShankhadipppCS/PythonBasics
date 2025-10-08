import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0 

is_running = True

print("Welcome to the number guessing game!")
print(f"Select a number between {lowest_num} and {highest_num}.")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print(f"out of range.")
            print(f"Please Select a number between {lowest_num} and {highest_num}.")
        elif guess < answer:
            print("too low.")
        elif guess > answer:
            print("too high.")
        else:
            print(f"congratulations! you guessed the number {answer} in {guesses} guesses.")
            is_running = False
    else:
        print("invalid guess.")
        print(f"Please Select a number between {lowest_num} and {highest_num}")