import random
import time


class RockPaperScissors:

    def __init__(self):
        self.current_round = 0
        self.user_points = 0
        self.computer_points = 0
        self.choices = ['Rock', 'Paper', "Scissors"]
        #self.game = {user: [], computer: []}
        self.comp_input = ''
        self.user_input = ''

    def computer_random_choice(self):
        # produce random computer object choice
        random_num = random.randrange(0, 3, 1)
        self.comp_input = self.choices[random_num]

    def user_choice(self):
        # take player input
            user_input = input(' Type your choice of either Rock, Paper or Scissors: ').lower().title()

            if user_input in self.choices:
                self.user_input = user_input
            else:
                print('That is not a valid choice, please submit: Rock, Paper, or Scissors')
                user_input = input(' Type your choice of either Rock, Paper or Scissors: ').lower().title()

    def compare_user_and_comp(self):
        print(f'{self.comp_input} vers {self.user_input} !')
        if (self.user_input == 'Rock' and self.comp_input == 'Scissors') or (
                self.user_input == 'Paper' and self.comp_input == 'Rock') or (
                self.user_input == 'Scissors' and self.comp_input == 'Paper'):
            self.user_points += 1
            self.current_round += 1
            print(f'{self.user_input} WINS!!! You get a point!')

        elif (self.comp_input == 'Rock' and self.user_input == 'Scissors') or (
                self.comp_input == 'Paper' and self.user_input == 'Rock') or (
                self.comp_input == 'Scissors' and self.user_input == 'Paper'):
            self.computer_points += 1
            self.current_round += 1
            time.sleep(2)
            print(f'{self.comp_input} WINS! The Computer got a point!')
        elif self.comp_input == self.user_input:
            time.sleep(2)
            print(f"You both chose {self.user_input}, That's a tie! Go again.")
        else:
            print("Did you enter Rock, Paper or Scissors? Please try again")

    def animation(self):
        pass

    def print_score(self):
        print(f'''
        SCORES ARE :
        PERSON PLAYER: {self.user_points}  COMPUTER PLAYER: {self.computer_points}
        ''')
        pass

    def winner_is(self):
        print('''
        The                                       Goes to:
              W           W    I   N     N
               W    W    W     I   N N   N
                W  W  W W      I   N  N  N
                 W     W       I   N     N       
        ''')
        if self.computer_points > self.user_points:
            print("THE COMPUTER!!!>>>>SORRY!!!!!")
        else:
            print("YOU")

    def run_game(self):
        while True:
            if self.computer_points >=2 or self.user_points >=2:
                time.sleep(2)
                self.winner_is()
                break
            else:
                self.user_choice()
                self.computer_random_choice()
                self.compare_user_and_comp()
                self.print_score()




# game loop: goes for number of user specified rounds.


# https://codereview.stackexchange.com/questions/231706/python-rock-paper-scissors-via-a-class-to-handle-the-game

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run_game()


  #  continue_prompt = input('\nDo you want to play again? (y/n): ').lower()
 #   if continue_prompt == 'n':
 #       print("Your LAME!")
 #       exit()
  #  elif continue_prompt == 'y':

  #  else:
       # print("Invalid input!\n")



