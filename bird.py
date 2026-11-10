from pico2d import load_image

import game_framework

FRAMES_PER_SECOND = 14.0

FRAME_RECTS = tuple(
    (col * 918 // 5, 506 - (row + 1) * 506 // 3,
     (col + 1) * 918 // 5 - col * 918 // 5,
     (row + 1) * 506 // 3 - row * 506 // 3)
    for row in range(3) for col in range(5)
)[:14]


class Bird:
    image = None
    width, height = 100, 92

    def __init__(self, x, y):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0.0

    def update(self):
        self.frame = (self.frame + FRAMES_PER_SECOND * game_framework.frame_time) % len(FRAME_RECTS)

    def draw(self):
        self.image.clip_draw(*FRAME_RECTS[int(self.frame)],
                             self.x, self.y, self.width, self.height)
