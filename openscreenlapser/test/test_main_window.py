import unittest
from aesthetic import main_window as window
from logic import capture

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.w = window.MainWindow()
        pass

    def test_handleCapture_when_not_capturing(self):
        self.w.isCapturing = False

        self.w.handleCapture()

        self.assertNotEqual(self.w.isCapturing, False)
        self.assertNotEqual(capture.instance.isCapturing, False)
        self.assertEqual(self.w.startbtntext.get(), 'Stop Capturing!')
        self.assertEqual(self.w.intervaltime.get(), capture.intervaltime)
    
    def test_handleCapture_while_capturing(self):
        self.w.isCapturing = True

        self.w.handleCapture()

        self.assertNotEqual(self.w.isCapturing, True)
        self.assertNotEqual(capture.instance.isCapturing, True)
        self.assertEqual(self.w.startbtntext.get(), 'Start Capturing!')

    def test_handleCapture_for_interval_time(self):
        self.helper_test_handleCapture_for_interval_time(100)
        self.helper_test_handleCapture_for_interval_time(1000)
        self.helper_test_handleCapture_for_interval_time(50000)

    def helper_test_handleCapture_for_interval_time(self, number):
        self.w.isCapturing = False
        self.w.intervaltime.set(number)
        self.w.handleCapture()
        self.assertEqual(capture.instance.intervaltime, number)


if __name__ == '__main__':
    unittest.main()
