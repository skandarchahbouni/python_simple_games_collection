import tkinter as tk
import random


# ------- Global variables and constantes
HEIGHT = 600
WIDTH = 600
STEP = 20
INIT_POS = [0, STEP * 2]
SPEED = 100
DIRECTION = "Down"
PRIZE = 10
score = 0
food_id = None
food_pos = [None, None]
snake = [
    INIT_POS,
    [INIT_POS[0], INIT_POS[1] - STEP],
]
old_snake = []


# ------- Functions
def draw_snake():
    global old_snake
    old_snake = []
    for rectangle in snake:
        rectangle_id = canvas.create_rectangle(
            rectangle[0],
            rectangle[1],
            rectangle[0] + STEP,
            rectangle[1] + STEP,
            fill="green",
        )
        old_snake.append(rectangle_id)


def collision() -> bool:
    head = snake[0]
    return (
        head[0] < 0
        or head[0] >= WIDTH
        or head[1] < 0
        or head[1] >= HEIGHT
        or head in snake[1:]
    )


def move_snake():
    global snake, rectangle_id
    for id in old_snake:
        canvas.delete(id)
    skip_delete = False
    head = snake[0][:]
    if head == food_pos:
        skip_delete = True
        eat()

    if collision():
        draw_snake()
        game_over()
        return
    if DIRECTION == "Up":
        head[1] -= STEP
    elif DIRECTION == "Down":
        head[1] += STEP
    elif DIRECTION == "Left":
        head[0] -= STEP
    elif DIRECTION == "Right":
        head[0] += STEP
    if skip_delete:
        snake = [head] + snake
    else:
        snake = [head] + snake[:-1]
    draw_snake()
    root.after(SPEED, move_snake)


def eat():
    global score
    score += PRIZE
    put_food()


def put_food():
    global food_id, food_pos
    if food_id:
        canvas.delete(food_id)
    food_pos[0] = random.choice(range(0, WIDTH - STEP + 1, 20))
    food_pos[1] = random.choice(range(0, HEIGHT - STEP + 1, 20))
    food_id = canvas.create_rectangle(
        food_pos[0], food_pos[1], food_pos[0] + STEP, food_pos[1] + STEP, fill="purple"
    )


def on_key_press(event):
    global START_MOVING
    global DIRECTION
    forbidden = [["Up", "Down"], ["Left", "Right"]]
    new_direction = event.keysym
    if [DIRECTION, new_direction] in forbidden or [
        new_direction,
        DIRECTION,
    ] in forbidden:
        return
    DIRECTION = new_direction


def game_over():
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
        text=f"Score: {score}",
        fill="white",
        font=("Helvetica", 20, "bold"),
    )


# ------- Create the main window
root = tk.Tk()
root.title("Snake Game")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="black")
canvas.pack()

put_food()
draw_snake()
move_snake()

root.bind("<Up>", on_key_press)
root.bind("<Down>", on_key_press)
root.bind("<Left>", on_key_press)
root.bind("<Right>", on_key_press)

root.mainloop()
