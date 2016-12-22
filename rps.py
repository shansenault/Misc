import random
import sys

class InputHandler():

    VALID_MOVES = ('rock', 'paper', 'scissors')
    VALID_OPTIONS = ['quit']

    def capture(self, text="", prompt='> '):

        if text:
            return raw_input("{0}\n{1}".format(text, prompt))
        else:
            return raw_input(prompt)

    def validate(self, user_input):

        for option in self.VALID_OPTIONS:
            if user_input.lower() in option:
                if option == "quit":
                    print "Goodbye."
                    sys.exit()

        for move in self.VALID_MOVES:
            if user_input.lower() in move:
                return True, move

        return False, None

    def check_winner(self, user_choice):

        computer_choice = random.choice(self.VALID_MOVES)
        
        if user_choice == computer_choice:
            return "The computer chose {0}. It's a draw.".format(computer_choice)
        elif user_choice == 'rock' and computer_choice == 'paper':
            return "The computer chose {0}. You lose.".format(computer_choice)
        elif user_choice == 'paper' and computer_choice == 'scissors':
            return "The computer chose {0}. You lose.".format(computer_choice)
        elif user_choice == 'scissors' and computer_choice == 'rock':
            return "The computer chose {0}. You lose.".format(computer_choice)
        else:
            return "The computer chose {0}. You win.".format(computer_choice)

def main():

    ih = InputHandler()

    success, user_choice = ih.validate(ih.capture("\nWelcome to Rock, Paper, Scissors. Make your move:"))

    while True:
        if success:
            success, user_choice = ih.validate(ih.capture(ih.check_winner(user_choice)))
        else:
            success, user_choice = ih.validate(ih.capture("Invalid input. Please select either rock, paper or scissors. Use 'q' to quit."))

if __name__ == '__main__':
    main()