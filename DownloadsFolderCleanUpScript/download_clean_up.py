import os
import shutil
import time


def set_target_directory(source):
    global target_dir
    target_dir = source


def set_exit_directory(exit_source):
    global exit_dir
    exit_dir = exit_source


def set_time(input_from_user):
    global time_input
    time_input = input_from_user


def move_files(name_of_new_dir, name_of_file):
    source = os.path.join(os.getcwd(), name_of_file)
    new_dir_path = os.path.join(exit_dir, name_of_new_dir)

    if not os.path.exists(new_dir_path):
        os.mkdir(new_dir_path)
    try:
        if os.path.exists(os.path.join(new_dir_path, name_of_file)):
            os.remove(source)
        else:
            shutil.move(source, new_dir_path)
    except FileNotFoundError:
        return


def run_program():
    os.chdir(target_dir)
    while True:
        all_files = os.listdir()

        for filename in all_files:
            file_extension = os.path.splitext(filename)[-1]

            if file_extension in compressed_files_extensions:
                move_files('compressed_files', filename)

            elif file_extension in torrent_and_sub_files_extensions:
                move_files('torrent_and_sub_files', filename)

            elif file_extension in ms_files_extensions:
                move_files('ms_files', filename)

            elif file_extension in installations_extensions:
                move_files('installations_files', filename)

            elif file_extension in images_extensions:
                move_files('image_files', filename)

            elif file_extension in coding_and_hardware_extensions:
                move_files('coding_and_hardware_files', filename)

        if time_input == 1:
            break

        time.sleep(time_input)


target_dir = "C:\\Users\\user\\Downloads"  # directory to clean, default downloads
exit_dir = "C:\\Users\\user\\Desktop"  # directory to place cleaned files, default desktop

compressed_files_extensions = ['.zip', '.rar', '.pk3']
torrent_and_sub_files_extensions = ['.torrent', '.srt']
ms_files_extensions = ['.pdf', '.docx', '.doc']
installations_extensions = ['.exe']
images_extensions = ['.jpg', '.png']
coding_and_hardware_extensions = ['.sql', '.py', '.ini', '.msi']

time_input = 0

