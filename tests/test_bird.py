import unittest
from unittest.mock import Mock, patch

import bird
import game_world
import play_mode


class BirdTests(unittest.TestCase):
    def setUp(self):
        bird.Bird.image = None
        self.loader = patch('bird.load_image', return_value=Mock()).start()
        self.addCleanup(patch.stopall)
        self.addCleanup(game_world.clear)
        self.addCleanup(setattr, bird.Bird, 'image', None)
        game_world.clear()

    def test_shared_image_and_first_frame(self):
        first = bird.Bird(400, 300)
        second = bird.Bird(800, 400)
        self.assertIs(first.image, second.image)
        self.loader.assert_called_once_with('bird_animation.png')
        first.draw()
        first.image.clip_draw.assert_called_once_with(
            0, 338, 183, 168, 400, 300, 100, 92)

    @patch('play_mode.Grass')
    @patch('play_mode.Boy')
    def test_scene_and_cleanup(self, boy, grass):
        play_mode.init()
        birds = [obj for layer in game_world.world for obj in layer
                 if isinstance(obj, bird.Bird)]
        self.assertEqual(len(birds), 1)
        self.assertIn(boy.return_value, game_world.world[1])
        self.assertIn(grass.return_value, game_world.world[0])
        play_mode.finish()
        self.assertTrue(all(not layer for layer in game_world.world))
        self.assertIsNone(play_mode.boy)


if __name__ == '__main__':
    unittest.main()
