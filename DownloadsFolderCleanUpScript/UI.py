from tkinter import *
import download_clean_up
import threading


def get_text_target_dir():
    target_dir = target_directory.get("1.0", "end-1c")

    return target_dir


def get_text_exit_dir():
    exit_dir = exit_directory.get("1.0", "end-1c")

    return exit_dir


def set_target_dir(directory_name):
    download_clean_up.set_target_directory(directory_name)


def set_exit_dir(directory_name):
    download_clean_up.set_exit_directory(directory_name)


def set_time_3600():
    download_clean_up.set_time(3600)


def set_time_21600():
    download_clean_up.set_time(21600)


def set_time_1():
    download_clean_up.set_time(1)


def start_background_process():
    background_process = threading.Thread(target=download_clean_up.run_program)
    background_process.start()


# window size
w_width = 500
w_height = 400

# creating window
window = Tk()
window.title("CleanUpApp")
window.geometry(f"{w_width}x{w_height}")

# setting up text field frame
frame_text = Frame(window, width=500, height=100)
frame_text.pack()

# setting up label frame
frame_label = Frame(window, width=500, height=50)
frame_label.pack()

# setting up button frame
frame_buttons = Frame(window, width=500, height=250)
frame_buttons.pack()

# centering window
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
position_right = int(window.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(window.winfo_screenheight() / 2 - window_height / 2)
window.geometry("+{}+{}".format(position_right, position_down))

var = IntVar()

# creating text fields
target_directory = Text(frame_text)
exit_directory = Text(frame_text)
target_directory.place(x=90, y=0, width=250, height=20)
exit_directory.place(x=90, y=40, width=250, height=20)
target_label = Label(frame_text, text="target dir:")
exit_label = Label(frame_text, text="exit dir:")
target_label.place(x=10, y=0)
exit_label.place(x=10, y=40)

# creating buttons for text fields
first_add_button = Button(frame_text, text="ADD", command=lambda: set_target_dir(get_text_target_dir()))
second_add_button = Button(frame_text, text="ADD", command=lambda: set_exit_dir(get_text_exit_dir()))
first_add_button.place(x=370, y=0, width=30, height=20)
second_add_button.place(x=370, y=40, width=30, height=20)

# creating label
label1 = Label(frame_label, text="How do you want to run your code?", background="gray", font=("Times new roman", 17))
label1.place(x=0, y=0, width=500, height=50)

# creating buttons
first_option = Radiobutton(frame_buttons, text="Once per hour", variable=var, value=3600, command=set_time_3600)
second_option = Radiobutton(frame_buttons, text="Once per six hours", variable=var, value=21600, command=set_time_21600)
third_option = Radiobutton(frame_buttons, text="Only once", variable=var, value=1, command=set_time_1)
first_option.pack()
second_option.pack()
third_option.pack()

# creating run button
run_button = Button(window, text="Run", command=start_background_process)
run_button.pack()

window.mainloop()
