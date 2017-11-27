import os
from os.path import expanduser
import pyscreenshot as ImageGrab

class Capture:
    def __init__(self):
        self.savedir = expanduser('~')
        self.intervaltime = 60
        self.isCapturing = False
        self.counter = 0
        self.timer = 0
        self.filename = ''

    def start(self):
        if not os.path.exists(self.savedir):
            os.makedirs(self.savedir)
        self.isCapturing = True

    def stop(self):
        self.isCapturing = False
        self.counter = 0
        self.timer = 0

    def takeScreenshots(self):
        if not os.path.exists(self.savedir):
            os.makedirs(self.savedir)
        targetfile = os.path.join(self.savedir, ('%s%03d' % (self.filename, self.counter)) + '.png')
        image = ImageGrab.grab()
        image.save(targetfile)
        self.counter = self.counter + 1

    def logicLoop(self, app):
        app.after(1000, self.logicLoop, app)
        if self.isCapturing:
            self.timer = self.timer + 1
            if self.timer == self.intervaltime + 1:
                self.takeScreenshots()
                self.timer = 0

    def setFileName(self, name):
        pass

instance = Capture()