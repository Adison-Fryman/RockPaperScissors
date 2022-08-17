import random

rounds = int(
    input("Hello how many rounds of rock paper sissors would you like to play agianst the computer? We recomend 3: "))
current_round = 0
user_points = 0
computer_points = 0
# computer_output generation:

choices = ['Rock', 'Paper', "Scissors"]
# game loop: goes for number of user specified rounds.

while current_round < rounds and ((computer_points + user_points) - 1) < rounds:
    print('The current round is ' + str(current_round) + '/' + str(rounds) + ' and the score is Computer: ' + str(
        computer_points) + ' and You: ' + str(user_points))
    # take player input
    user_input = input(' Type your choice of either Rock, Paper or Scissors: ').lower().title()
    # produce computer input
    random_num = random.randrange(0, 3, 1)
    comp_input = choices[random_num]
    print(f'{comp_input} vers {user_input} !')
    # compare(user_input,comututer_output)
    if (user_input == 'Rock' and comp_input == 'Scissors') or (user_input == 'Paper' and comp_input == 'Rock') or (
            user_input == 'Scissors' and comp_input == 'Paper'):
        user_points += 1
        current_round += 1
        print(f'{user_input} WINS!!! You get a point!')

    elif (comp_input == 'Rock' and user_input == 'Scissors') or (comp_input == 'Paper' and user_input == 'Rock') or (
            comp_input == 'Scissors' and user_input == 'Paper'):
        computer_points += 1
        current_round += 1
        print(f'{comp_input} WINS! The Computer got a point!')
    elif comp_input == user_input:
        print(f"You both chose {user_input}, That's a tie! Go again.")
    else:
        print("Did you enter Rock, Paper or Scissors? Please try again")

if user_points > computer_points:
    print("you win with")
if computer_points > user_points:
    print('computer wins')

# when rounds are over ask if they want to play again. Y for yes and N for exit
# best two out of three logic, not this quit after number of rounds.
# write exit game
#add time between display of vrs and you win