import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("400x450")
root.configure(bg='light gray')
root.title("CACHE SIMULATION PROJECT")

label = tk.Label(root, text="8-WAY BSA + LRU", font='helvetica 18 bold underline')
label.grid(padx=10, pady=10, row=0, columnspan=5)
label.configure(bg='light gray')

label = tk.Label(root, width=20, text="Number of cache blocks:", font='Arial 14 bold')
label.grid(row=1, column=0, columnspan=2, pady=15)
label.configure(bg='light gray')

textbox = tk.Text(root, width=8, height=1, font='Arial 14')
textbox.grid(row=1, column=2, columnspan=2)

# define testcases
# call case 1
# call case 2
# call case 3


# test cases
testcases = [
    "Sequential Sequence",
    "Random Sequence",
    "Mid-repeat Blocks"
]

label = tk.Label(root, width=20, text="Select a test case:", font='Arial 14 bold')
label.grid(row=3, column=0, columnspan=1)
label.configure(bg='light gray')

# drop down box
test_combo = ttk.Combobox(root, values=testcases)
test_combo.current()
test_combo.grid(row=3, column=2, pady=20)


def done_message():
    popup_done = tk.Toplevel()
    popup_done.geometry("150x150")
    # popup_snap.title("*WINDOW MSG HERE")
    popup_done.config(bg='light gray')
    msg = tk.Label(popup_done, text='DONE SIMULATION!', bg='light gray')
    msg.pack(padx=20, pady=20)
    button_close = tk.Button(popup_done, text='OK', command=popup_done.destroy)
    button_close.configure(bg='green', fg='white')
    button_close.pack(pady=10)


def text_log(filename, content):
    try:
        with open(filename, 'w') as f:
            f.write(content)
        print(f"File '{filename}' created successfully")
    except Exception as e:
        print(f"An error occurred: {e}")


filename = "Cache Simulation Log File.txt"
content = "test"  # snapshot goes here


# text_log(filename, content)


def show_snapshot():
    popup_snap = tk.Toplevel()
    popup_snap.geometry("400x250")
    popup_snap.title("CACHE MEMORY SNAPSHOT")
    popup_snap.config(bg='light gray')
    msg = tk.Label(popup_snap, text='*SNAPSHOT GOES HERE*', bg='light gray')
    msg.pack(padx=20, pady=20)
    button_print = tk.Button(popup_snap, text='Print', command=text_log(filename, content))
    button_print.configure(bg='green', fg='white')
    button_print.pack(padx=20, pady=20)
    button_close = tk.Button(popup_snap, text='Close', command=popup_snap.destroy)
    button_close.configure(bg='green', fg='white')
    button_close.pack(padx=20, pady=50)


def show_statistics():
    popup_stat = tk.Toplevel()
    popup_stat.geometry("250x400")
    popup_stat.title("CACHE MEMORY STATISTICS")
    popup_stat.config(bg='light gray')
    msg = tk.Label(popup_stat, text='*STATISTICS GOES HERE*', bg='light gray')
    msg.pack(padx=20, pady=20)
    button_close = tk.Button(popup_stat, text='Close', command=popup_stat.destroy)
    button_close.configure(bg='green', fg='white')
    button_close.pack(padx=20, pady=50)
    # add option to write out a txt file


SimulateButton = tk.Button(root, width=10, text="Simulate!", font='Arial 14 bold', command=done_message)
SimulateButton.grid(row=5, columnspan=5, pady=20)
SimulateButton.configure(bg='green', fg='white')

ResultButton = tk.Button(root, width=20, text="Cache Memory Snapshot", font='Arial 14 bold', command=show_snapshot)
ResultButton.grid(row=6, columnspan=5, pady=20)
ResultButton.configure(bg='green', fg='white')

StatButton = tk.Button(root, width=20, text="Cache Memory Statistics", font='Arial 14 bold', command=show_statistics)
StatButton.grid(row=7, columnspan=5, pady=20)
StatButton.configure(bg='green', fg='white')

root.mainloop()
