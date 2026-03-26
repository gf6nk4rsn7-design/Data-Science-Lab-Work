import random
import time

def clear_screen():
    print("\n" * 50)

def print_header():
    print("=" * 40)
    print("     ROCK PAPER SCISSORS - THE GAME")
    print("=" * 40)
    print()

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "player"
    else:
        return "computer"

def display_ascii_art(choice):
    if choice == 'rock':
        return """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
    elif choice == 'paper':
        return """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
    elif choice == 'scissors':
        return """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def play_game():
    player_score = 0
    computer_score = 0
    
    while True:
        clear_screen()
        print_header()
        
        print(f"SCOREBOARD:")
        print(f"You: {player_score} | Computer: {computer_score}")
        print("-" * 40)
        
        print("Choose your weapon:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '4' or choice.lower() == 'quit':
            print("\nThanks for playing! Final Score:")
            print(f"You: {player_score} | Computer: {computer_score}")
            if player_score > computer_score:
                print("YOU ARE THE CHAMPION! 🏆")
            elif computer_score > player_score:
                print("BETTER LUCK NEXT TIME! 🤖")
            else:
                print("IT'S A DRAW! 🤝")
            break
            
        choices_map = {'1': 'rock', '2': 'paper', '3': 'scissors'}
        if choice in choices_map:
            player_choice = choices_map[choice]
        elif choice.lower() in choices_map.values():
            player_choice = choice.lower()
        else:
            print("Invalid choice. Try again!")
            time.sleep(1)
            continue
            
        computer_choice = get_computer_choice()
        
        print("\n" + "="*40)
        print("ROCK...")
        time.sleep(0.5)
        print("PAPER...")
        time.sleep(0.5)
        print("SCISSORS...")
        time.sleep(0.5)
        print("SHOOT!\n")
        
        print("YOUR CHOICE:")
        print(display_ascii_art(player_choice))
        time.sleep(1)
        
        print("COMPUTER'S CHOICE:")
        print(display_ascii_art(computer_choice))
        time.sleep(1)
        
        winner = determine_winner(player_choice, computer_choice)
        
        print("="*40)
        if winner == "tie":
            print("IT'S A TIE!")
        elif winner == "player":
            print("YOU WIN THIS ROUND! 🎉")
            player_score += 1
        else:
            print("COMPUTER WINS THIS ROUND! 😈")
            computer_score += 1
            
        print("="*40)
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    play_game()
