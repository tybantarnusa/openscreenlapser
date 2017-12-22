import unittest
from openscreenlapser.logic import capture
from PIL import Image

class TestCaptureLogic(unittest.TestCase):
    def setUp(self):
        capture.instance = capture.Capture()

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

    def test_combine_image_webcam(self):
        im1 = Image.new('RGB', (100, 100))
        im2 = Image.new('RGB', (100, 100))

        combined = capture.instance.combineImageWebcam(im1, im2)
        self.assertIsInstance(combined, Image.Image)

    def test_start_webcam(self):
        class MockWebcam:
            def start(self):
                pass
            def stop(self):
                pass
                
        capture.instance.cam = MockWebcam()
        capture.instance.startWebcam()
        self.assertEqual(capture.instance.usingWebcam, True)

    def test_stop_webcam(self):
        class MockWebcam:
            def start(self):
                pass
            def stop(self):
                pass

        capture.instance.cam = MockWebcam()
        capture.instance.stopWebcam()
        self.assertEqual(capture.instance.usingWebcam, False)

    def test_logic_loop(self):
        class MockApp:
            def after(self, time, loop, app):
                pass
        app = MockApp()
        capture.instance.isCapturing = True
        capture.instance.timer = 0
        capture.instance.intervaltime = 0

        capture.instance.logicLoop(app)

        self.assertEqual(capture.instance.timer, 0)


if __name__ == '__main__':
    unittest.main()