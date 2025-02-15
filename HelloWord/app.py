secret_number = 9
guess_no = 1
guess_limit = 3
while guess_no <= guess_limit:
    input_no = int(input("Make a guess: "))
    guess_no += 1
    if input_no == secret_number:
        print("Correct guess")
        break
    elif guess_no < guess_limit:
        print("Wrong guess, please try again")
        continue
    else:
        print("Sorry please try again")
