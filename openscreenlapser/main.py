from aesthetic import main_window
from logic import capture

app = main_window.MainWindow()
app.after(1000, capture.instance.logicLoop, app)
app.mainloop()