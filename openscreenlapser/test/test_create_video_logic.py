import unittest
import shutil
import os.path
from openscreenlapser.logic import create_video
from openscreenlapser.logic import capture
import pygame

class TestCaptureLogic(unittest.TestCase):
    def setUp(self):
        capture.instance = capture.Capture()

    def test_successful_create(self):
        class MockWebcam:
            def get_image(self):
                return pygame.Surface((1000, 1000))

        capture.instance.savedir = './captures'
        capture.instance.cam = MockWebcam()
        capture.instance.usingWebcam = True
        
        capture.instance.takeScreenshots()
        create = create_video.instance
        status = create.create(24, capture.instance.savedir, 'out.mp4')
        fileExist = os.path.isfile('out.mp4')
        self.assertEqual(status, True)
        self.assertEqual(fileExist, True)
        shutil.rmtree('./captures')
    
    def test_failing_create(self):
        create = create_video.instance
        status = create.create(24, '~/notexist', 'out.mp4')
        self.assertEqual(status, False)
        
if __name__ == '__main__':
    unittest.main()