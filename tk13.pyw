import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
lb = tk.Label(text='this is a label. This is a label. This is a label.')

ms = tk.Message(text='This is a message. This is a Message. This is a Message.')
[widget.pack() for widget in (lb, ms)]
root.mainloop()