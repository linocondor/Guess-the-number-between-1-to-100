import random

print("Welcome to the guessing number game")
print("I'm thinking a number between 1 to 100")

#difficulty
difficulty = input("Choose a difficulty: 'easy' or 'hard': ")
easy = 10
hard = 5


Computer_number = random.randint(1,100)

guessed = False
if difficulty == "easy":
    print("You have {easy} attemps to guess the number")
    attemps = easy
elif difficulty == "hard":
    print("You have {hard} attemps to guess the number")
    attemps = hard

while attemps > 0 and guessed == False:
    
    print(f"You have {attemps} left.")
    guess = int(input("Make a guess: "))
    if guess == Computer_number:
        guessed = True
        print("Great you win")
    elif guess < Computer_number:
        
        print("Too low.")
        attemps -= 1
    elif guess > Computer_number:
        
        print("Too high.")
        attemps -= 1


print(f"You don't have more attemps: attemps = {attemps}. You loose")