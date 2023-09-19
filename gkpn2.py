import random
import json

def load_results():
    try:
        with open("results.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"player_wins": 0, "computer_wins": 0, "ties": 0, "total_rounds": 0, "rounds": []}

def save_results(results):
    with open("results.json", "w") as file:
        json.dump(results, file, indent=4)

def reset_results():
    results = {"player_wins": 0, "computer_wins": 0, "ties": 0, "total_rounds": 0, "rounds": []}
    with open("results.json", "w") as file:
        json.dump(results, file, indent=4)

def get_user_choice():
    while True:
        user_choice = input("Choose your weapon: rock, paper, or scissors.\nEnter your choice: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please select rock, paper, or scissors.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "win"
    else:
        return "lose"

def display_results(player_wins, computer_wins, ties, total_rounds):
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties: {ties}")
    print(f"Total rounds played: {total_rounds}")

def main():
    print("Welcome to the Rock-Paper-Scissors game!")

    results = load_results()

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)

        if result == "win":
            print("Congratulations, you won this round!")
            results["player_wins"] += 1
        elif result == "lose":
            print("The computer won this round. Maybe you'll do better next time.")
            results["computer_wins"] += 1
        else:
            print("This round ended in a tie!")
            results["ties"] += 1

        results["total_rounds"] += 1

        # Dodaj szczegóły rundy do listy "rounds"
        round_details = {
            "round_number": results["total_rounds"],
            "player_choice": user_choice,
            "computer_choice": computer_choice,
            "result": result
        }
        results["rounds"].append(round_details)

        save_results(results)

        display_results(results["player_wins"], results["computer_wins"], results["ties"], results["total_rounds"])

        print("-" * 150)

        play_again = input("Would you like to play again? (Y/N): ").lower()
        if play_again != "y":
            print("Thank you for playing with me. See you in the future :) ")
            break

if __name__ == "__main__":
    main()