print("What is your name?")
player = input("> ")
print(f"Hi, {player}!")
print("Step right up and guess my favorite color!")

# repeat until guess is correct

while True:
    print("What is your guess?")

    # store the user's guess
    guess = input("> ")

    if guess == "green":
        #if guess equals (green) then you got it!
        print("You got it!")
        break
    else:
        print("Nope, that's not it.")
        # ask again

