def make_sandwich(main, *ingredients):
    if not main:
        pass
    else:
        all_ingredients = [main] + list(ingredients)
        return f"Making a sandwich with {', '.join(all_ingredients)}"
print(make_sandwich("ham", "cheese", "pickles"))

def print_order_details(**order_details):
    for key, value in order_details.items():
        print(f"{key}: {value}")
print_order_details(name="Jackson", order_id=456)

# scope exercise
total_score = 0
def play_game():
    round_score = 0
    def win_round():
        nonlocal round_score
        round_score += 10
        global total_score
        total_score += 10
    win_round()
    win_round()
    win_round()
    print(round_score)
play_game()
print(total_score)

# lambda function
greet_user = lambda name : print("hey there " + name)
greet_user("John")

grade_status = lambda score : print('pass') if score >= 60 else print('fail')
grade_status(75)
grade_status(59)
grade_status(60)

#lambda map exercise
names = ["jackson", "olivia", "mia"]
capitalized_names = list(map(lambda name : name[0].upper() + name[1:], names))

print(capitalized_names)

# project remake number guessing game with functions
import random
wins = 0
losses = 0
def get_guess():
    """ will give the computer a random guess number"""
    global computer_number
    computer_number = random.randint(1, 100)
    return computer_number

def check_guess():

        for i in range(7):
            guess_num = int(input('what number would you like to guess: '))
            if guess_num == computer_number:
                print("Correct!!! You win!")
                global wins
                wins += 1
                return
            elif guess_num < computer_number:
                print("Too low!")
            else:
                print("Too high!")

        global losses
        losses += 1
        print("out of guesses you lose")
        print(f"computer number: {computer_number}")
def start_game():
    global computer_number
    get_guess()
    check_guess()
    print(f'total wins: {wins} total losses: {losses}')
    play_again = int(input("type 1 to play again or 0 to quit: "))
    if play_again == 1:
        start_game()
    else:
        return

start_game()