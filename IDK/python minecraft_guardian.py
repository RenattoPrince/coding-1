import subprocess
import sys
import os
import time
import threading
import json
import random
import tkinter as tk
from tkinter import messagebox
import chess
import psutil

MINECRAFT_EXE = r"C:\Program Files\Microsoft\Microsoft Minecraft Education\Minecraft.Education.exe"
MEMORY_FILE = "chess_memory.json"
ALLOWED_TO_PLAY = False

PIECE_SYMBOLS = {
    chess.KING: ('♔', '♚'),
    chess.QUEEN: ('♕', '♛'),
    chess.ROOK: ('♖', '♜'),
    chess.BISHOP: ('♗', '♝'),
    chess.KNIGHT: ('♘', '♞'),
    chess.PAWN: ('♙', '♟')
}

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

PAWN_TABLE = [
    0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
     5,  5, 10, 25, 25, 10,  5,  5,
     0,  0,  0, 20, 20,  0,  0,  0,
     5, -5,-10,  0,  0,-10, -5,  5,
     5, 10, 10,-20,-20, 10, 10,  5,
     0,  0,  0,  0,  0,  0,  0,  0
]

KNIGHT_TABLE = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50,
]

BISHOP_TABLE = [
    -20,-10,-10,-10,-10,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5, 10, 10,  5,  0,-10,
    -10,  5,  5, 10, 10,  5,  5,-10,
    -10,  0, 10, 10, 10, 10,  0,-10,
    -10, 10, 10, 10, 10, 10, 10,-10,
    -10,  5,  0,  0,  0,  0,  5,-10,
    -20,-10,-10,-10,-10,-10,-10,-20,
]

ROOK_TABLE = [
      0,  0,  0,  0,  0,  0,  0,  0,
      5, 10, 10, 10, 10, 10, 10,  5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
     -5,  0,  0,  0,  0,  0,  0, -5,
      0,  0,  0,  5,  5,  0,  0,  0
]

QUEEN_TABLE = [
    -20,-10,-10, -5, -5,-10,-10,-20,
    -10,  0,  0,  0,  0,  0,  0,-10,
    -10,  0,  5,  5,  5,  5,  0,-10,
     -5,  0,  5,  5,  5,  5,  0, -5,
      0,  0,  5,  5,  5,  5,  0, -5,
    -10,  5,  5,  5,  5,  5,  0,-10,
    -10,  0,  5,  0,  0,  0,  0,-10,
    -20,-10,-10, -5, -5,-10,-10,-20
]

KING_MID_TABLE = [
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -30,-40,-40,-50,-50,-40,-40,-30,
    -20,-30,-30,-40,-40,-30,-30,-20,
    -10,-20,-20,-20,-20,-20,-20,-10,
     20, 20,  0,  0,  0,  0, 20, 20,
     20, 30, 10,  0,  0, 10, 30, 20
]

class ChessGateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Minecraft Chess Gate - 10s Time-Limit Grandmaster")
        self.root.geometry("460x540")
        self.root.attributes('-topmost', True)
        self.root.resizable(False, False)
        
        self.board = chess.Board()
        self.selected_square = None
        self.current_game_moves = []
        self.memory = self.load_memory()
        
        self.label = tk.Label(root, text="Minecraft Locked! Defeat the 10-Second Thinking Bot.", font=("Arial", 11, "bold"), fg="#b58863")
        self.label.pack(pady=8)
        
        self.canvas_size = 400
        self.square_size = self.canvas_size / 8
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, highlightthickness=0)
        self.canvas.pack(pady=5)
        self.canvas.bind("<Button-1>", self.on_square_click)
        
        self.status_label = tk.Label(root, text="Your turn (White) | Ready", font=("Arial", 9, "bold"), fg="#312e2b")
        self.status_label.pack(pady=8)
        
        self.draw_board()

    def load_memory(self):
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "r") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def save_memory(self, won_game):
        reward = 1.0 if won_game else -1.0
        for fen, move in self.current_game_moves:
            if fen not in self.memory:
                self.memory[fen] = {}
            if move not in self.memory[fen]:
                self.memory[fen][move] = 0.0
            self.memory[fen][move] += reward

        try:
            with open(MEMORY_FILE, "w") as f:
                json.dump(self.memory, f, indent=4)
        except Exception as e:
            print(f"Could not save memory: {e}")

    def draw_board(self):
        self.canvas.delete("all")
        light_color = "#eeeed2"
        dark_color = "#769656"
        highlight_color = "#baca2b"
        
        for r in range(8):
            for c in range(8):
                x1 = c * self.square_size
                y1 = r * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                
                color = light_color if (r + c) % 2 == 0 else dark_color
                square_index = chess.square(c, 7 - r)
                if self.selected_square == square_index:
                    color = highlight_color
                
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
                
                piece = self.board.piece_at(square_index)
                if piece:
                    is_white = (piece.color == chess.WHITE)
                    symbol = PIECE_SYMBOLS[piece.piece_type][0 if is_white else 1]
                    self.canvas.create_text(
                        x1 + self.square_size / 2, 
                        y1 + self.square_size / 2, 
                        text=symbol, 
                        font=("Segoe UI Symbol", 28, "bold"),
                        fill="#f8f9fa" if is_white else "#212529"
                    )

    def on_square_click(self, event):
        col = int(event.x // self.square_size)
        row = int(7 - (event.y // self.square_size))
        
        if not (0 <= col <= 7 and 0 <= row <= 7):
            return
            
        clicked_square = chess.square(col, row)
        
        if self.selected_square is None:
            piece = self.board.piece_at(clicked_square)
            if piece and piece.color == self.board.turn:
                self.selected_square = clicked_square
                self.draw_board()
        else:
            move = chess.Move(self.selected_square, clicked_square)
            
            if self.board.piece_at(self.selected_square) and self.board.piece_at(self.selected_square).piece_type == chess.PAWN:
                if (chess.square_rank(clicked_square) == 7 and self.board.turn == chess.WHITE) or \
                   (chess.square_rank(clicked_square) == 0 and self.board.turn == chess.BLACK):
                    move = chess.Move(self.selected_square, clicked_square, promotion=chess.QUEEN)
            
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.draw_board()
                
                if self.board.is_game_over():
                    self.check_game_result()
                    return
                
                self.status_label.config(text="Bot is thinking for up to 10 seconds...", fg="#d9534f")
                self.root.update()
                self.root.after(100, self.ai_move)
            else:
                piece = self.board.piece_at(clicked_square)
                if piece and piece.color == self.board.turn:
                    self.selected_square = clicked_square
                else:
                    self.selected_square = None
                self.draw_board()

    def evaluate_board(self):
        if self.board.is_checkmate():
            return 99999 if self.board.turn == chess.BLACK else -99999
        if self.board.is_stalemate() or self.board.is_insufficient_material():
            return 0

        total_evaluation = 0
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece is not None:
                val = PIECE_VALUES[piece.piece_type]
                pst_val = 0
                sq = square if piece.color == chess.BLACK else chess.square_mirror(square)
                
                if piece.piece_type == chess.PAWN: pst_val = PAWN_TABLE[sq]
                elif piece.piece_type == chess.KNIGHT: pst_val = KNIGHT_TABLE[sq]
                elif piece.piece_type == chess.BISHOP: pst_val = BISHOP_TABLE[sq]
                elif piece.piece_type == chess.ROOK: pst_val = ROOK_TABLE[sq]
                elif piece.piece_type == chess.QUEEN: pst_val = QUEEN_TABLE[sq]
                elif piece.piece_type == chess.KING: pst_val = KING_MID_TABLE[sq]

                total_val = val + pst_val
                if piece.color == chess.BLACK:
                    total_evaluation += total_val
                else:
                    total_evaluation -= total_val
        return total_evaluation

    def quiescence(self, alpha, beta, maximizing_player):
        stand_pat = self.evaluate_board()
        if maximizing_player:
            if stand_pat >= beta: return beta
            if alpha < stand_pat: alpha = stand_pat
            for move in self.board.legal_moves:
                if self.board.is_capture(move):
                    self.board.push(move)
                    score = self.quiescence(alpha, beta, False)
                    self.board.pop()
                    if score >= beta: return beta
                    if score > alpha: alpha = score
            return alpha
        else:
            if stand_pat <= alpha: return alpha
            if beta > stand_pat: beta = stand_pat
            for move in self.board.legal_moves:
                if self.board.is_capture(move):
                    self.board.push(move)
                    score = self.quiescence(alpha, beta, True)
                    self.board.pop()
                    if score <= alpha: return alpha
                    if score < beta: beta = score
            return beta

    def minimax(self, depth, alpha, beta, maximizing_player):
        if depth == 0 or self.board.is_game_over():
            return self.quiescence(alpha, beta, maximizing_player)

        legal_moves = list(self.board.legal_moves)
        legal_moves.sort(key=lambda m: (self.board.is_capture(m), self.board.gives_check(m)), reverse=True)

        if maximizing_player:
            max_eval = -float('inf')
            for move in legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, alpha, beta, False)
                self.board.pop()
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha: break
            return max_eval
        else:
            min_eval = float('inf')
            for move in legal_moves:
                self.board.push(move)
                eval = self.minimax(depth - 1, alpha, beta, True)
                self.board.pop()
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha: break
            return min_eval

    def get_best_move(self):
        fen = self.board.fen()
        legal_moves = list(self.board.legal_moves)
        random.shuffle(legal_moves)  # Shuffle initially to prevent static identical patterns

        # Check memory first
        if fen in self.memory:
            scored_moves = self.memory[fen]
            best_memory_move = None
            highest_score = -float('inf')
            for m_str, score in scored_moves.items():
                m = chess.Move.from_uci(m_str)
                if m in legal_moves and score > highest_score:
                    highest_score = score
                    best_memory_move = m
            if best_memory_move and highest_score >= 0:
                return best_memory_move

        # Iterative Deepening Search with a strict 10-second time limit
        best_move = legal_moves[0]
        start_time = time.time()
        time_limit = 10.0  # Bot thinks for up to 10 seconds

        for current_depth in range(1, 7): # Goes deeper each loop until time runs out
            if time.time() - start_time > time_limit:
                break
            
            best_value = float('inf')
            current_best_moves = []

            for move in legal_moves:
                if time.time() - start_time > time_limit:
                    break
                
                self.board.push(move)
                board_value = self.minimax(current_depth - 1, -float('inf'), float('inf'), True)
                self.board.pop()

                if board_value < best_value:
                    best_value = board_value
                    current_best_moves = [move]
                elif board_value == best_value:
                    current_best_moves.append(move)

            if current_best_moves:
                # Randomize among equally best moves to avoid repetitive loops!
                best_move = random.choice(current_best_moves)

        self.current_game_moves.append((fen, best_move.uci()))
        return best_move

    def ai_move(self):
        best_move = self.get_best_move()
        self.board.push(best_move)
        self.draw_board()
            
        if self.board.is_game_over():
            self.check_game_result()
        else:
            self.status_label.config(text="Your turn (White) | Ready", fg="#312e2b")

    def check_game_result(self):
        result = self.board.result()
        if result == "1-0":
            self.save_memory(won_game=False)
            self.unlock_minecraft()
        elif result == "0-1":
            self.save_memory(won_game=True)
            messagebox.showinfo("Game Over", "The 10-Second Bot outcalculated you and won! Resetting...")
            self.reset_game_state()
        else:
            self.save_memory(won_game=False)
            messagebox.showinfo("Game Over", "It's a draw! Resetting board...")
            self.reset_game_state()

    def reset_game_state(self):
        self.board.reset()
        self.selected_square = None
        self.current_game_moves = []
        self.draw_board()
        self.status_label.config(text="Your turn (White) | Ready", fg="#312e2b")

    def unlock_minecraft(self):
        global ALLOWED_TO_PLAY
        messagebox.showinfo("Unlocked!", "Amazing! You beat the 10-second thinking bot! Launching Minecraft...")
        ALLOWED_TO_PLAY = True
        self.root.destroy()
        try:
            subprocess.Popen([MINECRAFT_EXE])
        except Exception as e:
            messagebox.showerror("Error", f"Could not launch Minecraft: {e}")

def run_chess_gate():
    root = tk.Tk()
    app = ChessGateApp(root)
    root.mainloop()

def monitor_minecraft():
    global ALLOWED_TO_PLAY
    print("Minecraft Guardian (10-Second Thinker) is running...")
    
    while True:
        try:
            for proc in psutil.process_iter(['name', 'exe']):
                proc_name = proc.info['name']
                if proc_name and "minecraft" in proc_name.lower():
                    if not ALLOWED_TO_PLAY:
                        proc.kill()
                        print("Minecraft launch blocked! Opening 10-second chess gate...")
                        threading.Thread(target=run_chess_gate).start()
                        time.sleep(3)
                    else:
                        time.sleep(10)
                        ALLOWED_TO_PLAY = False
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
        time.sleep(0.5)

if __name__ == "__main__":
    monitor_thread = threading.Thread(target=monitor_minecraft, daemon=True)
    monitor_thread.start()
    
    try:
        while True:
            time.sleep(3600)
    except KeyboardInterrupt:
        print("Guardian stopped.")