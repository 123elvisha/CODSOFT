import random

class RockPaperScissor:
    def __init__(self):
        self.item_list = ["Rock", "Paper", "Scissor"]

    def get_user_choice(self):
        while True:
            user_choice = input("Enter your move (Rock, Paper, Scissor): ")
            if user_choice in self.item_list:
                return user_choice
            else:
                print("Invalid choice. Please try again.")

    def get_computer_choice(self):
        return random.choice(self.item_list)

    def determine_winner(self, user_choice, comp_choice):
        if user_choice == comp_choice:
            return "Both chooses same: Match Tie"
        elif user_choice == "Rock":
            if comp_choice == "Paper":
                return "Paper covers Rock = Computer Win"
            else:
                return "Rock smashes Scissor = You win"
        elif user_choice == "Paper":
            if comp_choice == "Scissor":
                return "Scissor cuts paper, Computer Win"
            else:
                return "Paper covers rock, You win"
        elif user_choice == "Scissor":
            if comp_choice == "Paper":
                return "Scissor cuts paper, You win"
            else:
                return "Rock smashes scissor, Computer win"

    def play(self):
        user_choice = self.get_user_choice()
        comp_choice = self.get_computer_choice()

        print(f"User choice = {user_choice}, Computer choice = {comp_choice}")
        print(self.determine_winner(user_choice, comp_choice))

if __name__ == "__main__":
    game = RockPaperScissor()
    game.play()