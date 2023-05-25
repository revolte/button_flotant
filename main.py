import tkinter as tk

root = tk.Tk()

# create a button and position it at (0, 0)
stop_button = tk.Button(root, text="Stop", bg="red", command=root.quit)
stop_button.grid(row=0, column=0)

# make the window a floating widget and remove borders
root.overrideredirect(True)

# set the window to be always on top
root.wm_attributes("-topmost", True)

root.mainloop()
