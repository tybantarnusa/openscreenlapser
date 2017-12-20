from Tkinter import *
import tkFileDialog
import time
from openscreenlapser.logic import capture
from openscreenlapser.logic import create_video

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, padx=10, pady=10)

        self.savedir = StringVar()
        self.savedir.set(capture.instance.savedir)

        self.filename = StringVar()
        self.filename.set(capture.instance.filename)

        self.startbtntext = StringVar()

        self.intervaltime = IntVar()
        self.intervaltime.set(60)

        self.usingWebcam = IntVar()
        self.usingWebcam.set(0)

        self.isCapturing = False

        self.master.title('OpenScreenLapsers')
        self.master.minsize(width=400, height=100)
        self.master.resizable(False, False)
        self.pack(fill=BOTH)
        self.createWidgets()

    def createWidgets(self):
        self.dirLocator = self.createDirLocator()
        if capture.instance.hasCam():
            self.webcamCheckbox = self.createWebcamCheckbox()
        Label(self).pack()
        self.intervalTimer = self.createIntervalTimer()
        self.startButton = self.createStartButton()
        self.createVideoButton = self.createCreateVideoButton()

    def createDirLocator(self):
        dirLocator = Frame(self)

        label = Label(dirLocator, text='Output file name:', anchor=E, justify=RIGHT)
        label.grid(row=0, column=0, sticky=E)

        self.nameEntry = Entry(dirLocator, textvariable=self.filename)
        self.nameEntry.grid(row=0, column=1)
        
        label = Label(dirLocator, text='Output screenshots folder:')
        label.grid(row=1, column=0)

        entry = Entry(dirLocator, textvariable=self.savedir)
        entry.grid(row=1, column=1)
        self.pathEntry = entry

        self.dirLocatorBtn = Button(dirLocator, text='...', command=self.locateSaveDir)
        self.dirLocatorBtn.grid(row=1, column=2, padx=5)

        dirLocator.pack(fill=X)
        return dirLocator

    def locateSaveDir(self):
        output = tkFileDialog.askdirectory(parent=self, initialdir=capture.instance.savedir, title='Output screenshots directory...')
        if len(output) > 0:
            self.savedir.set(output)
            capture.instance.savedir = output

    def createWebcamCheckbox(self):
        frame = Frame(self)

        checkbox = Checkbutton(frame, text='Use webcam', variable=self.usingWebcam, command=self.updateWebcamLogic)
        checkbox.pack(side=RIGHT)

        frame.pack(fill=X)

        return checkbox

    def updateWebcamLogic(self):
        if self.usingWebcam.get() == 1:
            capture.instance.startWebcam()
        else:
            capture.instance.stopWebcam()


    def createIntervalTimer(self):
        intervalTimer = Frame(self)

        label = Label(intervalTimer, text='Interval:')
        label.pack(side=LEFT)

        entry = Entry(intervalTimer, textvariable=self.intervaltime, width=3)
        entry.pack(side=LEFT)
        self.intervalEntry = entry

        label = Label(intervalTimer, text='sec')
        label.pack(side=LEFT)

        intervalTimer.pack(anchor=E)
        return intervalTimer

    def createStartButton(self):
        self.startbtntext.set('Start Capturing!')
        button = Button(self, command=self.handleCapture, textvariable=self.startbtntext)
        button.pack(fill=X)
        self.ori_abg = button.cget('activebackground')
        self.ori_bg = button.cget('bg')

        return button

    def handleCapture(self):
        if not self.isCapturing:
            self.isCapturing = True
            self.startbtntext.set('Stop Capturing!')
            capture.instance.savedir = self.savedir.get()
            capture.instance.setFileName(self.filename.get())
            capture.instance.intervaltime = self.intervaltime.get()
            self.startButton.configure(activebackground='red3', bg='red2')
            self.disableAll()
            capture.instance.start()
        else:
            self.isCapturing = False
            self.startbtntext.set('Start Capturing!')
            self.startButton.configure(activebackground=self.ori_abg, bg=self.ori_bg)
            capture.instance.stop()
            self.hideCaptureButton()
            self.showCreateVideoButton()

    def createCreateVideoButton(self):
        frame = Frame(self)

        button = Button(frame, command=self.handleCreateVideo, text='Create Video!')
        button.grid(row=0, column=0)

        button = Button(frame, command=self.handleStartOver, text='Start Over')
        button.grid(row=0, column=1)
        return frame

    def showCreateVideoButton(self):
        self.createVideoButton.pack(fill=X)

    def hideCreateVideoButton(self):
        self.createVideoButton.pack_forget()

    def showCaptureButton(self):
        self.startButton.pack(fill=X)
    
    def hideCaptureButton(self):
        self.startButton.pack_forget()

    def handleCreateVideo(self):
        ftypes = [('MP4', '.mp4'), ('All files', '*')]
        out = tkFileDialog.asksaveasfilename(parent=self, initialdir=capture.instance.savedir, title='Save video as', filetypes=ftypes, defaultextension='.mp4')
        if len(out) > 0:
            self.hideCreateVideoButton()
            self.showCaptureButton()
            self.startbtntext.set('Creating video...')
            self.startButton.config(state='disabled')
            self.update()
            create_video.instance.create(24, capture.instance.savedir, out)
            self.handleStartOver()

    def handleStartOver(self):
        self.hideCreateVideoButton()
        self.startbtntext.set('Start Capturing!')
        self.startButton.config(state='normal')
        self.showCaptureButton()
        self.enableAll()

    def disableAll(self):
        self.nameEntry.config(state='disabled')
        self.pathEntry.config(state='disabled')
        self.intervalEntry.config(state='disabled')
        self.dirLocatorBtn.config(state='disabled')
        if capture.instance.hasCam():
            self.webcamCheckbox.config(state='disabled')

    def enableAll(self):
        self.nameEntry.config(state='normal')
        self.pathEntry.config(state='normal')
        self.intervalEntry.config(state='normal')
        self.dirLocatorBtn.config(state='normal')
        if capture.instance.hasCam():
            self.webcamCheckbox.config(state='normal')
