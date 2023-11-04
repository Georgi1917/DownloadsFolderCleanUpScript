from tkinter import *
import download_clean_up
import threading


def set_time_3600():
    download_clean_up.set_time(3600)


def set_time_21600():
    download_clean_up.set_time(21600)


def set_time_1():
    download_clean_up.set_time(1)


def start_background_process():
    background_process = threading.Thread(target=download_clean_up.run_program)
    background_process.start()


window = Tk()
window.title("Python exe")
window.configure(width=300, height=300)

window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
position_right = int(window.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(window.winfo_screenheight() / 2 - window_height / 2)
window.geometry("+{}+{}".format(position_right, position_down))

var = IntVar()

label1 = Label(text="How do you want to run your code?")
label1.pack()
first_option = Radiobutton(window, text="Once per hour", variable=var, value=3600, command=set_time_3600)
second_option = Radiobutton(window, text="Once per six hours", variable=var, value=21600, command=set_time_21600)
third_option = Radiobutton(window, text="Only once", variable=var, value=1, command=set_time_1)
first_option.pack()
second_option.pack()
third_option.pack()

run_button = Button(window, text="Run", command=start_background_process)
run_button.pack()

window.mainloop()
