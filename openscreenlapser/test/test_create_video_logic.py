import unittest
import os.path
from logic import create_video
from logic import capture

class TestCaptureLogic(unittest.TestCase):
    def setUp(self):
        pass

    def test_successful_create(self):
        capture.instance.takeScreenshots()
        create = create_video.instance
        status = create.create(24, capture.instance.savedir, 'out.mp4')
        fileExist = os.path.isfile('out.mp4')
        self.assertEqual(status, True)
        self.assertEqual(fileExist, True)
    
    def test_failing_create(self):
        create = create_video.instance
        status = create.create(24, '~/notexist', 'out.mp4')
        self.assertEqual(status, False)
        
if __name__ == '__main__':
    unittest.main()