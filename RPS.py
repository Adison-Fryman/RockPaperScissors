import random
import time
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

class RockPaperScissors:

    def __init__(self):
        self.current_round = 0
        self.user_points = 0
        self.computer_points = 0
        self.choices = ['Rock', 'Paper', "Scissors"]
        self.comp_input = ''
        self.user_input = ''

    def get_inputs(self):
        user_input = input("Enter Rock, Paper, or Scissors: ").lower().title()
        self.user_input = user_input
        return user_input

    def computer_random_choice(self):
        # produce random computer object choice
        random_num = random.randrange(0, 3, 1)
        self.comp_input = self.choices[random_num]

    def user_choice_check(self):
        while self.user_input not in self.choices:
            print('That is not a valid choice, please submit: Rock, Paper, or Scissors')
            self.user_input = input("Enter Rock, Paper, or Scissors: ").lower().title()
            logging.info("user did not enter correct input")
        logging.info(f'user gave correct input:{self.user_input}')

    def compare_user_and_comp(self):
        logging.info(f'comp: {self.comp_input} vers user: {self.user_input} ')
        print(f'{self.comp_input} vers {self.user_input} !')
        if (self.user_input == 'Rock' and self.comp_input == 'Scissors') or (
                self.user_input == 'Paper' and self.comp_input == 'Rock') or (
                self.user_input == 'Scissors' and self.comp_input == 'Paper'):
            self.user_points += 1
            self.current_round += 1
            logging.info('user gets a point')
            print(f'{self.user_input} WINS!!! You get a point!')

        elif (self.comp_input == 'Rock' and self.user_input == 'Scissors') or (
                self.comp_input == 'Paper' and self.user_input == 'Rock') or (
                self.comp_input == 'Scissors' and self.user_input == 'Paper'):
            self.computer_points += 1
            self.current_round += 1
            time.sleep(2)
            logging.info('computer gets a point')
            print(f'{self.comp_input} WINS! The Computer got a point!')
        elif self.comp_input == self.user_input:
            time.sleep(2)
            logging.info('user and computer had the same item choice')
            print(f"You both chose {self.user_input}, That's a tie! Go again.")
        else:
            #it should never get to this line
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
        The                                      Goes to:
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
        logging.info("---new game started----")
        while True:
            if self.computer_points >=2 or self.user_points >=2:
                time.sleep(2)
                self.winner_is()
                logging.info('game is over')
                break
            else:
                logging.info('round started')
                self.get_inputs()
                self.user_choice_check()
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



