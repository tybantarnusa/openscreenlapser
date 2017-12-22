import unittest
from openscreenlapser.aesthetic import main_window as window
from openscreenlapser.logic import capture
from Tkinter import Checkbutton, IntVar

class TestMainWindow(unittest.TestCase):
    def setUp(self):
        self.w = window.MainWindow()
        capture.instance = capture.Capture()

    def test_handleCapture_when_not_capturing(self):
        self.w.isCapturing = False

        self.w.handleCapture()

        self.assertNotEqual(self.w.isCapturing, False)
        self.assertNotEqual(capture.instance.isCapturing, False)
        self.assertEqual(self.w.startbtntext.get(), 'Stop Capturing!')
        self.assertEqual(self.w.intervaltime.get(), capture.instance.intervaltime)
    
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

    def test_create_webcam_checkbox(self):
        checkbox = self.w.createWebcamCheckbox()
        self.assertIsInstance(checkbox, Checkbutton)

    def test_update_webcam_logic(self):
        class MockWebcam:
            def start(self):
                pass
            def stop(self):
                pass

        capture.instance.cam = MockWebcam()
        self.w.usingWebcam.set(0)
        self.w.updateWebcamLogic()
        self.assertEqual(capture.instance.usingWebcam, False)

        self.w.usingWebcam.set(1)
        self.w.updateWebcamLogic()
        self.assertEqual(capture.instance.usingWebcam, True)

    def test_hide_create_video_button(self):
        self.w.hideCreateVideoButton()

    def test_show_capture_button(self):
        self.w.showCaptureButton()

    def test_handle_start_over(self):
        self.w.handleStartOver()
        self.assertEqual(self.w.startbtntext.get(), 'Start Capturing!')
        self.assertEqual(self.w.startButton.cget('state'), 'normal')

    def test_disable_all(self):
        capture.instance.cam = 1
        self.w.disableAll()
        self.assertEqual(self.w.nameEntry.cget('state'), 'disabled')
        self.assertEqual(self.w.pathEntry.cget('state'), 'disabled')
        self.assertEqual(self.w.intervalEntry.cget('state'), 'disabled')
        self.assertEqual(self.w.dirLocatorBtn.cget('state'), 'disabled')
        self.assertEqual(self.w.webcamCheckbox.cget('state'), 'disabled')

    def test_enable_all(self):
        capture.instance.cam = 1
        self.w.enableAll()
        self.assertEqual(self.w.nameEntry.cget('state'), 'normal')
        self.assertEqual(self.w.pathEntry.cget('state'), 'normal')
        self.assertEqual(self.w.intervalEntry.cget('state'), 'normal')
        self.assertEqual(self.w.dirLocatorBtn.cget('state'), 'normal')
        self.assertEqual(self.w.webcamCheckbox.cget('state'), 'normal')

if __name__ == '__main__':
    unittest.main()
