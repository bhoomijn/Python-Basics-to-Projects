import random

def play_game():
    print("\nWelcome to the Snake, Water, Gun Game!")
    print("Rules:")
    print("🐍 Snake drinks water (Snake wins)")
    print("💧 Water drowns gun (Water wins)")
    print("🔫 Gun kills snake (Gun wins)")
    print("If both choose the same, it's a draw.\n")

    rounds = int(input("Enter the number of rounds you want to play: "))
    user_score = 0
    computer_score = 0

    youDict = {"snake": 1, "water": -1, "gun": 0}

    for i in range(rounds):
        print("-" * 30)
        youstr = input(f"\nRound {i+1}: Enter your choice (snake, water, gun): ").lower()

        if youstr not in youDict:
            print("❌ Invalid input! Please choose snake, water, or gun.")
            continue
        
        you = youDict[youstr]
        computer = random.choice(["snake", "water", "gun"])
        comp = youDict[computer]
        print(f"Computer chose: {computer}")

        if comp == 1 and you == -1:
            print("🐍 Snake drank the water! Computer wins!")
            computer_score += 1
        elif comp == 1 and you == 0:
            print("🐍 Snake is killed by gun! You win!")
            user_score += 1
        elif comp == -1 and you == 0:
            print("💧 Water is killed by gun! Computer wins!")
            computer_score += 1
        elif comp == 0 and you == 1:
            print("🔫 Gun kills 🐍 snake! You win!")
            user_score += 1
        elif comp == -1 and you == 1:
            print("💧 Water drank the 🐍 snake! You win!")
            user_score += 1
        elif comp == 0 and you == -1:
            print("🔫 Gun drowned the water! Computer wins!") 
            computer_score += 1
        elif comp == you:
            print("🤝 You both chose the same! It's a draw.")
            
            
        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")

    print(f"\n🏆 Final Score: You: {user_score}, Computer: {computer_score}")
    if user_score > computer_score:
        print("🎉 Congratulations! You won the game!")
    elif user_score < computer_score:
        print("💻 Computer won the game! Better luck next time.")
    else:
        print("🤝 The game is a draw!")
        

while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! 👋 Goodbye!")
        break
