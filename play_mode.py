from pico2d import *
import game_world
import game_framework
from boy import Boy
from grass import Grass
from bird import Bird

boy = None


def handle_events():


    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def init():
    global boy

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

    for i in range(10):
        x = Bird.width / 2 + (get_canvas_width() - Bird.width) * (i + 0.5) / 10
        y = 160 + (get_canvas_height() - Bird.height / 2 - 160) * i / 9
        game_world.add_oject(Bird(x, y))


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy
    game_world.clear()
    boy = None


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()









