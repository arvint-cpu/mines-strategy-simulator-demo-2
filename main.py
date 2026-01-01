import random

# Constants
GRID_SIZE = 5
INITIAL_BALANCE = 100
MIN_BET = 0.1

# Symbols
MINE = '💣'
HIDDEN = '.'
EXPLOSION = '💥'

# Function to place mines randomly
def place_mines(num_mines):
    mines = []
    for _ in range(num_mines):
        while True:
            x, y = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
            if (x, y) not in mines:
                mines.append((x, y))
                break
    return mines

# Function to display the grid
def display_grid(revealed, mines, explosion_cell=None, show_all_mines=False):
    print("\n  " + " ".join(str(i) for i in range(GRID_SIZE)))
    for i in range(GRID_SIZE):
        print(i, end=" ")
        for j in range(GRID_SIZE):
            if explosion_cell and (i, j) == explosion_cell:
                print(EXPLOSION, end=" ")  # Show explosion if mine is hit
            elif show_all_mines and (i, j) in mines:
                print(MINE, end=" ")  # Show all mines if game is lost
            elif (i, j) in mines and revealed[i][j]:
                print(MINE, end=" ")
            elif revealed[i][j]:
                print("💰", end=" ")  # Safe cell
            else:
                print(HIDDEN, end=" ")
        print()

# Main game loop
def main():
    balance = INITIAL_BALANCE

    # Ask the player for the number of mines
    while True:
        try:
            num_mines = int(input(f"Enter the number of mines (1 to {GRID_SIZE * GRID_SIZE - 1}): "))
            if num_mines < 1 or num_mines >= GRID_SIZE * GRID_SIZE:
                print("Invalid number of mines. Try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Place mines
    mines = place_mines(num_mines)

    while balance > 0:
        print(f"\nBalance: ${balance:.2f}")
        revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        display_grid(revealed, mines)

        # Ask for bet
        while True:
            try:
                bet = float(input(f"Enter your bet (min ${MIN_BET}, max ${balance:.2f}): "))
                if bet < MIN_BET or bet > balance:
                    print(f"Invalid bet. Must be between ${MIN_BET} and ${balance:.2f}.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

        balance -= bet
        reward_multiplier = 1.0
        round_over = False
        explosion_cell = None  # Track the cell where the mine explodes

        while not round_over:
            # Ask for cell to reveal
            try:
                x = int(input("Enter row: "))
                y = int(input("Enter column: "))
                if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
                    print("Invalid input. Try again.")
                    continue
                if revealed[x][y]:
                    print("Cell already revealed. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Try again.")
                continue

            # Reveal the cell
            revealed[x][y] = True
            if (x, y) in mines:
                explosion_cell = (x, y)  # Set the explosion cell
                print(f"Boom! You hit a mine. You lose your bet of ${bet:.2f}.")
                display_grid(revealed, mines, explosion_cell, show_all_mines=True)  # Show all mines
                round_over = True
            else:
                reward_multiplier += 0.5  # Increase reward for each safe cell
                print(f"Safe! Current reward multiplier: {reward_multiplier:.1f}x")
                display_grid(revealed, mines)

                # Ask if the player wants to cash out or continue
                choice = input("Do you want to (c)ash out or (k)eep playing? ").strip().lower()
                if choice == 'c':
                    reward = bet * reward_multiplier
                    balance += reward
                    print(f"You cashed out and won ${reward:.2f}!")
                    round_over = True
                elif choice != 'k':
                    print("Invalid choice. Continuing...")

        if balance <= 0:
            print("Game Over! You ran out of balance.")

    print("Thanks for playing!")

if __name__ == "__main__":
    main()


 
