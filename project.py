import random
import sys
from pyglet.window import Window, key
from pyglet import app
from pyglet import shapes
import pyglet

win = Window(width=1040, height=640)
shape_list = []

def draw_columns(numbers: list[int]):
    global batch,line, shape_list, label
    batch = pyglet.graphics.Batch()
    line = shapes.Line(0, 60, 1040, 60, width=4, color=(0, 0, 200), batch=batch)

    for i, v in enumerate(numbers):
        rectangle = shapes.BorderedRectangle(10 + (1020//100) * i, 62, 10, v*5, color=(150,150,0),batch=batch)
        shape_list.append(rectangle)
        label = pyglet.text.Label(f'{v}',
                                  font_size=6,
                                  font_name="Times New Roman",
                                  x=int((10 + (1020//100) * i) + 5), y=50,
                                  anchor_x='center', anchor_y='center',
                                  dpi=100,
                                  batch=batch)

def bubble_sort(arr: list[int]):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# TODO
def bubble_sort_shapes(shapes):
    global label
    n = len(shapes)

    for i in range(n):
        for j in range(0, n-i-1):
            if shapes[j].height > shapes[j+1].height:
                shapes[j], shapes[j+1] = shapes[j+1], shapes[j]
    new_numbers = list()
    for shape in shapes:
        new_numbers.append(shape.height/5)
    draw_columns(new_numbers)

def generate_numbers(n: int):
    if n < 0:
        sys.exit("Negative number inserted in 'generate_numbers'")
    numbers = list(range(0, n))
    random.shuffle(numbers)
    return numbers

@win.event
def on_draw():
    win.clear()
    batch.draw()

@win.event
def on_key_press(symbol, modifiers):
    global numbers, shape_list
    if symbol == key.UP:
        bubble_sort(numbers)
        draw_columns(numbers)
    if symbol == key.DOWN:
        bubble_sort_shapes(shape_list)


def main():
    global numbers
    numbers = generate_numbers(100)
    draw_columns(numbers)
    app.run()

if __name__ == "__main__":
    main()
