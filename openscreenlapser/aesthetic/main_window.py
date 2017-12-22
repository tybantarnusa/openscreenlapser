from Tkinter import *
import ttk
import tkFileDialog
import time
from openscreenlapser.logic import capture
from openscreenlapser.logic import create_video

class MainWindow(Frame):
    def __init__(self, master=None):
        self.intervalEntry = None
        self.webcamCheckbox = None
        self.ori_abg = None
        self.ori_bg = None

        Frame.__init__(self, master)

        self.pages = ttk.Notebook(self)
        self.pages.pack()

        self.create_capture_tab()
        self.create_settings_tab()

        self.pages.add(self.tab1, text='Capture')
        self.pages.add(self.tab2, text='Settings')

        self.master.title('OpenScreenLapser')
        self.master.minsize(width=400, height=100)
        self.master.resizable(False, False)
        self.pack(fill=BOTH)

    def create_capture_tab(self):
        self.tab1 = Frame(self.pages, padx=10, pady=10)

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
        self.createWidgets()

    def create_settings_tab(self):
        self.selected_webcam_layout = StringVar(value='NW')

        self.tab2 = Frame(self.pages, padx=5, pady=5)
        self.tab2.pack(fill=BOTH)

        webcam_setting_frame = LabelFrame(self.tab2, text='Webcam Setting', padx=5, pady=5)
        webcam_setting_frame.pack(fill=X)

        Label(webcam_setting_frame, text='Position:').pack(anchor=W)

        webcam_pos_layout_frame = LabelFrame(webcam_setting_frame, padx=5, pady=5)
        webcam_pos_layout_frame.pack(anchor=W)
        webcam_pos_layout_frame.grid_columnconfigure(0, minsize=75)
        webcam_pos_layout_frame.grid_columnconfigure(1, minsize=75)
        webcam_pos_layout_frame.grid_rowconfigure(1, minsize=50)

        webcam_pos_nw_radio = Radiobutton(webcam_pos_layout_frame, highlightthickness=0, variable=self.selected_webcam_layout, value='NW', command=self.change_webcam_pos)
        webcam_pos_nw_radio.grid(row=0, column=0, sticky=W)
        webcam_pos_ne_radio = Radiobutton(webcam_pos_layout_frame, variable=self.selected_webcam_layout, value='NE', command=self.change_webcam_pos)
        webcam_pos_ne_radio.grid(row=0, column=1, sticky=E)
        webcam_pos_sw_radio = Radiobutton(webcam_pos_layout_frame, variable=self.selected_webcam_layout, value='SW', command=self.change_webcam_pos)
        Label(webcam_pos_layout_frame).grid(row=1)
        webcam_pos_sw_radio.grid(row=2, column=0, sticky=W)
        webcam_pos_se_radio = Radiobutton(webcam_pos_layout_frame, variable=self.selected_webcam_layout, value='SE', command=self.change_webcam_pos)
        webcam_pos_se_radio.grid(row=2, column=1, sticky=E)

    def change_webcam_pos(self):
        selected_pos = self.selected_webcam_layout.get()
        capture.instance.change_webcam_pos(selected_pos)

    def createWidgets(self):
        self.dirLocator = self.createDirLocator()
        if capture.instance.hasCam():
            self.webcamCheckbox = self.createWebcamCheckbox()
        Label(self.tab1).pack()
        self.intervalTimer = self.createIntervalTimer()
        self.startButton = self.createStartButton()
        self.createVideoButton = self.createCreateVideoButton()

    def createDirLocator(self):
        dirLocator = Frame(self.tab1)

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
        len_output = len(output)
        if len_output > 0:
            self.savedir.set(output)
            capture.instance.savedir = output

    def createWebcamCheckbox(self):
        frame = Frame(self.tab1)

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
        intervalTimer = Frame(self.tab1)

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
        button = Button(self.tab1, command=self.handleCapture, textvariable=self.startbtntext)
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
        frame = Frame(self.tab1)

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
        len_out = len(out)
        if len_out > 0:
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
