from pico2d import get_canvas_width, load_image

import game_framework
from boy import RUN_SPEED_MPS, PIXEL_PER_METER

FRAMES_PER_SECOND = 14.0
BIRD_SPEED_MPS = RUN_SPEED_MPS * 1.5
BIRD_SPEED_PPS = BIRD_SPEED_MPS * PIXEL_PER_METER

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
        self.dir = 1

    def update(self):
        dt = game_framework.frame_time
        if dt == 0:
            return
        self.frame = (self.frame + FRAMES_PER_SECOND * dt) % len(FRAME_RECTS)
        left = self.width / 2
        span = get_canvas_width() - self.width
        # 왕복 경로를 펼쳐 이동한 뒤 접으면 경계 초과 거리도 보존된다.
        phase = self.x - left if self.dir == 1 else 2 * span - (self.x - left)
        phase = (phase + BIRD_SPEED_PPS * dt) % (2 * span)
        self.x = left + min(phase, 2 * span - phase)
        self.dir = 1 if phase < span else -1

    def draw(self):
        flip = 'h' if self.dir == -1 else ''
        self.image.clip_composite_draw(*FRAME_RECTS[int(self.frame)],
                                       0, flip, self.x, self.y,
                                       self.width, self.height)
