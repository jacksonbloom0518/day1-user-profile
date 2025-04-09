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
    global computer_number
    computer_number = random.randint(1, 100)
    return computer_number
def check_guess():
    for i in range(7):
        guess = int(input("guess a number between 1 and 100: "))
        if guess == computer_number:
            print("Correct!!! You win!")
            global wins
            wins += 1
            break
        elif guess < computer_number:
            print("Too low!")
        else:
            print("Too high!")
    else:
        global losses
        losses += 1
        print("Sorry, you ran out of guesses. The number was " + str(computer_number))


def start_game():
    get_guess()
    check_guess()
    print(f"total wins: {wins} total losses: {losses}")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == "y":
        start_game()
    else:
        print("Thank you for playing!")
        return
start_game()


# project 2 tip calculator
def calculate_tip(amount, rating):
    if rating == "bad":
        return amount * 0.10
    elif rating == "okay":
        return amount * 0.15
    elif rating == "great":
        return amount * 0.20
    else:
        print("Invalid rating")
        return None
def get_bill_details():
    amount = float(input("Enter bill amount: "))
    rating = input("Rate the service (bad, okay, great): ")
    tip = calculate_tip(amount, rating)
    if tip is None:
        return
    bill = amount + tip
    print(f"tip is: ${tip} and total bill is: ${bill}")
get_bill_details()

# function project 3 - rock paper scissors game
import random
def get_computer_choice():
    random_number = random.randint(1, 3)
    if random_number == 1:
        return "rock"
    elif random_number == 2:
        return "paper"
    else:
        return "scissors"
def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "rock" and computer_choice == "scissors" or player_choice == "scissors" and computer_choice == "paper"\
            or player_choice == "paper" and computer_choice == "rock":
        return "You win!"
    else:
        return "Computer wins!"
def play_game():
    player_choice = input("rock, paper, or scissors? ").lower()
    if player_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        return
    computer_choice = get_computer_choice()
    winner = get_winner(player_choice, computer_choice)
    print(f"You choose {player_choice} and computer choose {computer_choice}")
    print(winner)
play_game()

# func PROJECT 4 - GRADE CALCULATOR
def calculate_average(grades):
    return sum(grades) / len(grades)
def get_highest_grade(grades):
    return max(grades)
def get_lowest_grade(grades):
    return min(grades)
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def summarize_grades(grades):
    average = calculate_average(grades)
    maximum = get_highest_grade(grades)
    minimum = get_lowest_grade(grades)
    avg_letter_grade = get_letter_grade(average)
    max_letter_grade = get_letter_grade(maximum)
    min_letter_grade = get_letter_grade(minimum)
    print(f"The average score is: {str(average)} ({avg_letter_grade})")
    print(f"The maximum score is: {str(maximum)} ({max_letter_grade})")
    print(f"The minimum score is: {str(minimum)} ({min_letter_grade})")
grades = [92, 88, 74, 97, 62, 85]
summarize_grades(grades)
