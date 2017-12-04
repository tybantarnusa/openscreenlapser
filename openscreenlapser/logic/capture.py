import os
import time
from os.path import expanduser
import pyscreenshot as ImageGrab
import pygame
import pygame.camera
from pygame.locals import *
from PIL import Image

class Capture:
    def __init__(self):
        self.savedir = expanduser('~')
        self.intervaltime = 60
        self.isCapturing = False
        self.counter = 0
        self.timer = 0
        self.filename = ''
        self.usingWebcam = False
        self.initWebcam()

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

        if self.usingWebcam:
            webcam = self.takeWebcam()
            image.paste(webcam, (0, 0))
        
        image.save(targetfile)
        self.counter = self.counter + 1

    def initWebcam(self):
        pygame.init()
        pygame.camera.init()

        camlist = pygame.camera.list_cameras()
        if camlist:
            self.cam = pygame.camera.Camera(camlist[0], (640,480))

    def startWebcam(self):
        self.cam.start()
        self.usingWebcam = True

    def stopWebcam(self):
        self.cam.stop()
        self.usingWebcam = False

    def takeWebcam(self):
        image = self.cam.get_image()
        string_image = pygame.image.tostring(image, "RGBA", False)
        pil_image = Image.frombytes("RGBA", (640,480), string_image)
        return pil_image

    def logicLoop(self, app):
        app.after(1000, self.logicLoop, app)
        if self.isCapturing:
            self.timer = self.timer + 1
            if self.timer == self.intervaltime + 1:
                self.takeScreenshots()
                self.timer = 0

    def setFileName(self, name):
        self.filename = name

instance = Capture()