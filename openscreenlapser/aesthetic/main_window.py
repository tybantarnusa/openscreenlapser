from Tkinter import *
import tkFileDialog
from logic import capture

class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, padx=10, pady=10)

        self.savedir = StringVar()
        self.savedir.set(capture.instance.savedir)

        self.startbtntext = StringVar()

        self.intervaltime = IntVar()
        self.intervaltime.set(60)

        self.isCapturing = False

        self.master.title('OpenScreenLapser')
        self.master.minsize(width=400, height=100)
        self.master.resizable(False, False)
        self.pack(fill=BOTH)
        self.createWidgets()

    def createWidgets(self):
        self.dirLocator = self.createDirLocator()
        self.intervalTimer = self.createIntervalTimer()
        self.startButton = self.createStartButton()

    def createDirLocator(self):
        dirLocator = Frame(self)

        label = Label(dirLocator, text='Output screenshots folder:')
        label.grid(row=0, column=0)

        entry = Entry(dirLocator, textvariable=self.savedir)
        entry.grid(row=0, column=1)
        self.pathEntry = entry

        btn = Button(dirLocator, text='...', command=self.locateSaveDir)
        btn.grid(row=0, column=2, padx=5)

        dirLocator.pack(fill=X)
        return dirLocator

    def locateSaveDir(self):
        output = tkFileDialog.askdirectory(parent=self, initialdir=capture.instance.savedir, title='Output screenshots directory...')
        if len(output) > 0:
            self.savedir.set(output)
            capture.instance.savedir = output

    def createIntervalTimer(self):
        Label(self).pack()
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
            capture.instance.intervaltime = self.intervaltime.get()
            self.startButton.configure(activebackground='red3', bg='red2')
            self.pathEntry.config(state='disabled')
            self.intervalEntry.config(state='disabled')
            capture.instance.start()
        else:
            self.isCapturing = False
            self.startbtntext.set('Start Capturing!')
            self.startButton.configure(activebackground=self.ori_abg, bg=self.ori_bg)
            self.pathEntry.config(state='normal')
            self.intervalEntry.config(state='normal')
            capture.instance.stop()

    def createCreateVideoButton(self):
        pass

    def showCreateVideoButton(self):
        pass

    def handleCreateVideo(self):