import time
import curses
import random

def game_loop(window):

    #Setup inicial
    curses.curs_set(0)
    snake= [
        [10, 15],
        [9, 15],
        [8, 15],
        [7, 15]
    ]
    fruit = get_new_fruit(window=window)
    curent_direction = curses.KEY_DOWN

    while True:
        draw_screan(window=window)
        draw_snake(snake=snake, window=window)
        draw_actor(actor=fruit, window=window, char=curses.ACS_DIAMOND)
        direction = get_new_direction(window=window, timeout=1000)
        if direction is None:
            direction = curent_direction
        move_snake(snake=snake, direction=direction)
        if snake_hit_border(snake=snake, window=window):
            return
        if snake_hit_fruit(snake = snake, fruit=fruit):
            fruit = get_new_fruit(window=window)
        curent_direction = direction

def snake_hit_border(snake, window):
    head = snake[0]
    return actor_hit_border(actor=snake[0], window=window)

def snake_hit_fruit(snake, fruit):
    if fruit in snake:
        return True

def draw_screan(window):
    window.clear()
    window.border(0)

def draw_snake(snake, window):
    head = snake[0]
    draw_actor(actor=head, window=window, char='@')
    body = snake[1:] 
    for body_party in body:
        draw_actor(actor=body_party, window=window, char='S')

def get_new_fruit(window):
    height, width = window.getmaxyx()
    return [random.randint(1, height-2), random.randint(1, width-2)]

def draw_actor(actor, window, char):
    window.addch(actor[0], actor[1], char)

def get_new_direction(window, timeout):
    window.timeout(1000)
    direction = window.getch()
    if direction in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
        return direction

def move_snake(snake, direction):
    head = snake[0].copy()
    move_actor(actor=head, direction=direction)
    snake.insert(0, head)
    snake.pop()

def move_actor(actor, direction):

    match direction:
            case curses.KEY_UP:
                actor[0] -= 1
            case curses.KEY_DOWN:
                actor[0] += 1
            case curses.KEY_LEFT:
                actor[1] -= 1
            case curses.KEY_RIGHT:
                actor[1] += 1

def actor_hit_border(actor, window):

    height, width = window.getmaxyx()

    if (actor[0] <= 0) or (actor[0] >= height - 1):
        return True
    elif (actor[1] <= 0) or (actor[1] >= width - 1):
        return True
    else:
        return False
    


if __name__ == '__main__':
    curses.wrapper(game_loop)
    print('Perdeu.')

    
 
        
        
       

