import tkinter as tk
from tkinter import messagebox


# ------- Global variables and constantes
DIMENSION = 300
STEP = 100
TURN = "X"
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
remaining = [i for i in range(1, 10)]

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)

# Create a canvas widget
canvas = tk.Canvas(root, width=DIMENSION, height=DIMENSION, bg="black")
canvas.pack()


def show_board():
    global board
    factor = [1, 3, 5]
    for i in range(3):
        for j in range(3):
            canvas.create_text(
                factor[j] * STEP // 2,
                factor[i] * STEP // 2,
                text=str(board[i][j]),
                fill="white",
                font=("Helvetica", 30, "bold"),
            )
    for i in range(0, DIMENSION, STEP):
        canvas.create_line(i, 0, i, DIMENSION, fill="white", width=1)
        canvas.create_line(0, i, DIMENSION, i, fill="white", width=1)


def get_position(number):
    for i, row in enumerate(board):
        if number in row:
            return i, row.index(number)
    return None


def check_winner() -> bool:
    factor = [1, 3, 5]
    # Check rows
    for i in range(3):
        if board[i] == [TURN] * 3:
            start = (0, factor[i] * STEP // 2)
            end = (DIMENSION, factor[i] * STEP // 2)
            canvas.create_line(start[0], start[1], end[0], end[1], fill="red", width=2)
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == TURN and board[1][i] == TURN and board[2][i] == TURN:
            start = (factor[i] * STEP // 2, 0)
            end = (factor[i] * STEP // 2, DIMENSION)
            canvas.create_line(start[0], start[1], end[0], end[1], fill="red", width=2)
            return True
    # Check diagonal (top-left to bottom-right)
    if board[0][0] == TURN and board[1][1] == TURN and board[2][2] == TURN:
        start = (0, 0)
        end = (DIMENSION, DIMENSION)
        canvas.create_line(start[0], start[1], end[0], end[1], fill="red", width=2)
        return True
    # Check diagonal (top-right to bottom-left)
    if board[0][2] == TURN and board[1][1] == TURN and board[2][0] == TURN:
        start = (DIMENSION, 0)
        end = (0, DIMENSION)
        canvas.create_line(start[0], start[1], end[0], end[1], fill="red", width=2)
        return True
    return False


def show_dialog(tie=False):
    global TURN
    if tie:
        messagebox.showinfo("Game Over", "Tie.")
    else:
        messagebox.showinfo("Game Over", f"Player {TURN} Won!")
    root.quit()


def on_key_press(event):
    global board, TURN, remaining
    if event.char.isdigit():
        pos = get_position(int(event.char))
        if pos is not None:
            remaining.remove(int(event.char))
            board[pos[0]][pos[1]] = TURN
            canvas.delete("all")
            show_board()
            winner = check_winner()
            if winner:
                show_dialog()
            if remaining == []:
                show_dialog(tie=True)
            if TURN == "X":
                TURN = "O"
            else:
                TURN = "X"


show_board()

root.bind("<Key>", on_key_press)
root.mainloop()
