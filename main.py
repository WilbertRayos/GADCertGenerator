import tkinter as tk

from view.main_gui import MainGui



#----------------------------------------------------------------------
if __name__ == "__main__":
    app = tk.Tk()
    app.title("GAD Certificate Generator")
    MainGui(app)
    app.mainloop()