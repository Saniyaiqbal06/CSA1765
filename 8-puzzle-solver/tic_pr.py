import random
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None
        self.difficulty = 'medium'
    
    def print_board(self):
        print("\n   |   |   ")
        for i in range(3):
            row = self.board[i*3:(i+1)*3]
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if i < 2:
                print("___|___|___")
                print("   |   |   ")
        print("   |   |   \n")
    
    def print_board_nums(self):
        print("\nPosition numbers:")
        print(" 0 | 1 | 2 ")
        print("___|___|___")
        print(" 3 | 4 | 5 ")
        print("___|___|___")
        print(" 6 | 7 | 8 \n")
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False
    
    def minimax(self, is_maximizing, alpha, beta):
        if self.current_winner == 'O':
            return 1
        elif self.current_winner == 'X':
            return -1
        elif not self.empty_squares():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for move in self.available_moves():
                self.board[move] = 'O'
                if self.winner(move, 'O'):
                    self.current_winner = 'O'
                score = self.minimax(False, alpha, beta)
                self.board[move] = ' '
                self.current_winner = None
                best_score = max(score, best_score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                self.board[move] = 'X'
                if self.winner(move, 'X'):
                    self.current_winner = 'X'
                score = self.minimax(True, alpha, beta)
                self.board[move] = ' '
                self.current_winner = None
                best_score = min(score, best_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return best_score
    
    def get_best_move(self, difficulty):
        if difficulty == 'easy':
            return self.get_easy_move()
        elif difficulty == 'medium':
            return self.get_medium_move()
        else:
            return self.get_hard_move()
    
    def get_easy_move(self):
        available = self.available_moves()
        if available:
            return random.choice(available)
        return None
    
    def get_medium_move(self):
        for letter in ['O', 'X']:
            for move in self.available_moves():
                self.board[move] = letter
                if self.winner(move, letter):
                    self.board[move] = ' '
                    return move
                self.board[move] = ' '
        
        corners = [0, 2, 6, 8]
        available_corners = [c for c in corners if c in self.available_moves()]
        if available_corners and random.random() < 0.7:
            return random.choice(available_corners)
        
        return self.get_random_move()
    
    def get_hard_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.available_moves():
            self.board[move] = 'O'
            if self.winner(move, 'O'):
                self.current_winner = 'O'
            score = self.minimax(False, -float('inf'), float('inf'))
            self.board[move] = ' '
            self.current_winner = None
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def get_random_move(self):
        available = self.available_moves()
        if available:
            return random.choice(available)
        return None


def play_game():
    game = TicTacToe()
    
    print("\n" + "="*40)
    print("          TIC TAC TOE")
    print("="*40)
    
    difficulty = select_difficulty()
    game.difficulty = difficulty
    
    print("\nBoard positions are numbered 0-8:")
    game.print_board_nums()
    
    first = choose_first_player()
    print(f"\n{first} goes first!")
    
    if first == 'computer':
        computer_letter = 'O'
        player_letter = 'X'
        print("You are X, Computer is O")
    else:
        computer_letter = 'X'
        player_letter = 'O'
        print("You are O, Computer is X")
    
    print("\nGame starts now!")
    time.sleep(1)
    
    current_letter = 'X'
    
    while game.empty_squares():
        game.print_board()
        
        if current_letter == computer_letter:
            print("Computer's turn...")
            time.sleep(0.5)
            square = game.get_best_move(difficulty)
            if square is not None:
                game.make_move(square, computer_letter)
                print(f"Computer chooses square {square}")
        else:
            square = player_move(game, player_letter)
            game.make_move(square, player_letter)
        
        if game.current_winner:
            game.print_board()
            if game.current_winner == player_letter:
                print("\n🎉 Congratulations! You win! 🎉")
            else:
                print("\n💻 Computer wins! Better luck next time! 💻")
            return
        
        current_letter = 'O' if current_letter == 'X' else 'X'
    
    game.print_board()
    print("\n🤝 It's a tie! 🤝")


def select_difficulty():
    print("\nSelect difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def choose_first_player():
    print("\nWho goes first?")
    print("1. You")
    print("2. Computer")
    print("3. Random")
    
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice == '1':
            return 'player'
        elif choice == '2':
            return 'computer'
        elif choice == '3':
            return random.choice(['player', 'computer'])
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def player_move(game, player_letter):
    while True:
        try:
            square = input(f"Your turn ({player_letter}). Choose a position (0-8): ").strip()
            square = int(square)
            
            if square < 0 or square > 8:
                print("Please enter a number between 0 and 8.")
            elif square not in game.available_moves():
                print("That square is already taken. Choose another.")
            else:
                return square
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_again():
    print("\n" + "="*40)
    again = input("Do you want to play again? (y/n): ").strip().lower()
    return again == 'y' or again == 'yes'


def main():
    print("\n" + "="*50)
    print("     WELCOME TO TIC TAC TOE")
    print("="*50)
    
    playing = True
    wins = 0
    losses = 0
    ties = 0
    
    while playing:
        play_game()
        
        print("\n" + "="*40)
        again = play_again()
        playing = again
        
        if not playing:
            print("\nThanks for playing Tic Tac Toe!")
            print("Goodbye! 👋")
        else:
            print("\n" + "="*40)
            print("Starting new game...")
            print("="*40)


if __name__ == '__main__':
    main()