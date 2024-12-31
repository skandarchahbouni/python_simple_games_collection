import tkinter as tk


#
WIDTH = 500
HEIGHT = 300
STEP = 10
BLUE_PLAYER = None
RED_PLAYER = None
BALL = None
SPEED = 50
DIRECTION = "DR"

#
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.resizable(False, False)
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()


BLUE_PLAYER = canvas.create_rectangle(0, 0, 10, 60, fill="blue")
RED_PLAYER = canvas.create_rectangle(WIDTH - 10, 0, WIDTH, 60, fill="red")
BALL = canvas.create_rectangle(50, 50, 60, 60, fill="white")


def move_ball():
    global BALL, DIRECTION
    if DIRECTION == "DR":
        coords = canvas.coords(BALL)
        new_coords = [x + STEP for x in coords]
        canvas.delete(BALL)
        BALL = canvas.create_rectangle(*new_coords, fill="white")
        if new_coords[2] == WIDTH:
            game_over(winner="blue")
            return
        elif new_coords[2] == WIDTH - STEP:
            red_player_coords = canvas.coords(RED_PLAYER)
            if (
                new_coords[1] >= red_player_coords[1]
                and new_coords[3] <= red_player_coords[3]
            ):
                DIRECTION = "DL"
            elif new_coords[1] + STEP == red_player_coords[1]:
                DIRECTION = "UL"
        elif new_coords[3] == HEIGHT:
            DIRECTION = "UR"
    elif DIRECTION == "DL":
        coords = canvas.coords(BALL)
        coords[1] += STEP
        coords[3] += STEP
        coords[0] -= STEP
        coords[2] -= STEP
        canvas.delete(BALL)
        BALL = canvas.create_rectangle(*coords, fill="white")
        if coords[0] == 0:
            game_over(winner="red")
            return
        elif coords[0] == STEP:
            blue_player_coords = canvas.coords(BLUE_PLAYER)
            if (
                coords[1] >= blue_player_coords[1]
                and coords[1] <= blue_player_coords[3]
            ):
                DIRECTION = "DR"
            elif coords[1] + STEP == blue_player_coords[1]:
                DIRECTION = "UR"
        elif coords[3] == HEIGHT:
            DIRECTION = "UL"
    elif DIRECTION == "UR":
        coords = canvas.coords(BALL)
        coords[0] += STEP
        coords[2] += STEP
        coords[1] -= STEP
        coords[3] -= STEP
        canvas.delete(BALL)
        BALL = canvas.create_rectangle(*coords, fill="white")
        if coords[2] == WIDTH:
            game_over(winner="blue")
            return
        elif coords[2] == WIDTH - STEP:
            red_player_coords = canvas.coords(RED_PLAYER)
            if coords[1] >= red_player_coords[1] and coords[3] <= red_player_coords[3]:
                DIRECTION = "UL"
            elif coords[1] == red_player_coords[3]:
                DIRECTION = "DL"
        elif coords[1] == 0:
            DIRECTION = "DR"
    elif DIRECTION == "UL":
        coords = canvas.coords(BALL)
        new_coords = [x - STEP for x in coords]
        canvas.delete(BALL)
        BALL = canvas.create_rectangle(*new_coords, fill="white")
        if new_coords[0] == 0:
            game_over(winner="red")
            return
        elif new_coords[0] == STEP:
            blue_player_coords = canvas.coords(BLUE_PLAYER)
            if (
                new_coords[1] >= blue_player_coords[1]
                and new_coords[3] <= blue_player_coords[3]
            ):
                DIRECTION = "UR"
            elif new_coords[1] == blue_player_coords[3]:
                DIRECTION = "DR"
        elif new_coords[1] == 0:
            DIRECTION = "DL"
    root.after(SPEED, move_ball)


def game_over(winner: str):
    root.unbind("<Key>")
    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 - 20,
        text="GAME OVER",
        fill="red",
        font=("Helvetica", 30, "bold"),
    )
    canvas.create_text(
        WIDTH // 2,
        HEIGHT // 2 + 20,
        text=f"Winner: {winner} player!",
        fill="white",
        font=("Helvetica", 20, "bold"),
    )


def on_key_press(event):
    global BLUE_PLAYER, RED_PLAYER
    if event.char == "a":
        coords = canvas.coords(BLUE_PLAYER)
        if coords[1] > 0:
            coords[1] -= STEP
            coords[3] -= STEP
            canvas.delete(BLUE_PLAYER)
            BLUE_PLAYER = canvas.create_rectangle(*coords, fill="blue")
    elif event.char == "q":
        coords = canvas.coords(BLUE_PLAYER)
        if coords[3] < HEIGHT:
            coords[1] += STEP
            coords[3] += STEP
            canvas.delete(BLUE_PLAYER)
            BLUE_PLAYER = canvas.create_rectangle(*coords, fill="blue")
    elif event.char == "p":
        coords = canvas.coords(RED_PLAYER)
        if coords[1] > 0:
            coords[1] -= STEP
            coords[3] -= STEP
            canvas.delete(RED_PLAYER)
            RED_PLAYER = canvas.create_rectangle(*coords, fill="red")
    elif event.char == "m":
        coords = canvas.coords(RED_PLAYER)
        if coords[3] < HEIGHT:
            coords[1] += STEP
            coords[3] += STEP
            canvas.delete(RED_PLAYER)
            RED_PLAYER = canvas.create_rectangle(*coords, fill="red")


move_ball()

root.bind("<Key>", on_key_press)
root.mainloop()
