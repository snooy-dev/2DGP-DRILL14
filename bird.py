from pico2d import load_image


class Bird:
    image = None
    width, height = 100, 92

    def __init__(self, x, y):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y = x, y
        self.frame = 0.0

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 338, 183, 168,
                             self.x, self.y, self.width, self.height)
