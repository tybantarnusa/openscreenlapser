import unittest
from logic import capture
from SimpleCV.ImageClass import Image

class TestCaptureLogic(unittest.TestCase):
    def setUp(self):
        pass

    def test_start(self):
        capture.instance.isCapturing = False
        capture.instance.start()
        self.assertEqual(capture.instance.isCapturing, True)

    def test_stop(self):
        capture.instance.isCapturing = True
        capture.instance.counter = 712
        capture.instance.timer = 3
        capture.instance.stop()
        self.assertEqual(capture.instance.isCapturing, False)
        self.assertEqual(capture.instance.counter, 0)
        self.assertEqual(capture.instance.timer, 0)

    def test_counter_increased_after_taking_a_screenshot(self):
        capture.instance.counter = 32
        capture.instance.takeScreenshots()
        self.assertEqual(capture.instance.counter, 33)

    def test_set_filename(self):
        capture.instance.setFileName('screen')
        self.assertEqual(capture.instance.filename, 'screen')

    def test_take_webcam(self):
        img = capture.instance.takeWebcam()
        self.assertIsInstance(img, Image)

if __name__ == '__main__':
    unittest.main()