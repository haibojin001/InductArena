from engine import run_single_game
import random

def main():
    for i in range(1, 256):
        rows = random.randint(8, 15)
        cols = random.randint(7, 15)
        print(f"Generating game {i} with board {rows}x{cols}")
        run_single_game(i, rows, cols)

if __name__ == "__main__":
    main()