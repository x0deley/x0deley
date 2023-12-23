import sys
import os
import tkinter as tk
import webbrowser
import shutil
import subprocess
import threading
from pathlib import Path
from tkinter import ttk
from PIL import Image, ImageTk
import ctypes

def copy_config_to_data():
    # Указываем путь к файлу конфигурации на C:
    config_source_path = Path("C:/x0deley/GameUserSettings.ini")

    # Копируем файл в папку data внутри приложения
    data_folder_path = Path("data")
    data_folder_path.mkdir(parents=True, exist_ok=True)
    config_dest_path = data_folder_path / "GameUserSettings.ini"
    shutil.copy(config_source_path, config_dest_path)

def create_folder_on_c_drive(folder_name):
    c_drive_path = Path("C:/", folder_name)
    if not c_drive_path.is_dir():
        c_drive_path.mkdir(parents=True, exist_ok=True)
        # Copy necessary files to the created folder
        source_folder = Path(sys._MEIPASS) if getattr(sys, 'frozen', False) else Path('.')
        files_to_copy = ["Strip.bat", "msi.exe", "remove.bat", "1.bat", "2.bat","Performance.cmd","Hibernate.cmd","CFG.bat","TimerResolution.exe","PowerX.pow","PowerX.bat"]
        for file_to_copy in files_to_copy:
            source_file = source_folder / "data" / file_to_copy
            destination_file = c_drive_path / file_to_copy
            shutil.copy(source_file, destination_file)
    return c_drive_path

if getattr(sys, 'frozen', False):
    resource_path = Path(sys._MEIPASS)
    icon_path = Path(resource_path, "data", "images", "icon.ico")
else:
    resource_path = Path('.')
    icon_path = Path(resource_path, "data", "images", "icon.ico")

def run_as_admin(command):
    try:
        if os.name == 'nt' and sys.platform.startswith('win'):
            # Запуск программы от имени администратора
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(command), None, 1)
        else:
            raise Exception("Unsupported platform for running as admin")
    except Exception as e:
        print(f"Error running as admin: {e}")

def open_main_window():
    root = tk.Tk()
    root.title("x0deley")
    root.resizable(width=False, height=False)

    canvas = tk.Canvas(root, width=900, height=600)
    canvas.pack()

    bg_image_path = Path(os.path.join(resource_path, "data", "images", "2.png"))

    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((900, 600), resample=Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(canvas, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    class DraggableFrame(tk.Frame):
        def __init__(self, master=None, **kwargs):
            super().__init__(master, **kwargs)
            self.bind("<B1-Motion>", self.drag)
            self.bind("<ButtonPress-1>", self.click)
            self.start_x = 0
            self.start_y = 0

        def drag(self, event):
            x = self.winfo_pointerx() - self.start_x
            y = self.winfo_pointery() - self.start_y
            self.master.geometry(f"{self.winfo_reqwidth()}x{self.winfo_reqheight()}+{x}+{y}")

        def click(self, event):
            self.start_x = event.x
            self.start_y = event.y

    def open_best_driver():
        webbrowser.open_new("https://drive.google.com/file/d/1I2ZIWTAkBKENDSrk02thti9oVOZCs4bK/view?usp=sharing")

    def append_to_console(message, tag=None):
        console_text.config(state=tk.NORMAL)
        if tag:
            console_text.insert(tk.END, message + "\n", tag)
        else:
            console_text.insert(tk.END, message + "\n")
        console_text.see(tk.END)
        console_text.config(state=tk.DISABLED)

    def run_batch_file_background(batch_file_name, target_folder):
        print(f"Trying to copy {batch_file_name} to {target_folder}")
        batch_file_path = Path(target_folder, batch_file_name)

        try:
            # Запуск программы от имени администратора
            print(f"Running {batch_file_name} as admin")

            # Попробуйте использовать subprocess для запуска программы от имени администратора
            subprocess.run([str(batch_file_path)], shell=True, check=True)

            root.after(0, append_to_console, f"Использовали {os.path.splitext(batch_file_name)[0]}", "info")
        except Exception as e:
            print(f"Error: {e}")
            root.after(0, append_to_console, f"Ошибка выполнения {e}", "error")

    def run_batch_file(batch_file_name, target_folder):
        threading.Thread(target=run_batch_file_background, args=(batch_file_name, target_folder)).start()

    button_color = "#000000"

    buttons_data = [
        {"text": "Fortnite Strip", "batch_file": "Strip.bat"},
        {"text": "Optimize GPU", "batch_file": "msi.exe"},
        {"text": "Delete Apps", "batch_file": "remove.bat"},
        {"text": "Clear Temp 1", "batch_file": "1.bat"},
        {"text": "Clear Temp 2", "batch_file": "2.bat"},
    ]

    frame_main = DraggableFrame(root, padx=10, pady=10, bg="#000000")
    frame_main.place(relx=0.1, rely=0.45, anchor=tk.W)

    target_folder = create_folder_on_c_drive("x0deley")
    for data in buttons_data:
        button = tk.Button(frame_main, text=data["text"], command=lambda data=data: run_batch_file(data["batch_file"], target_folder), cursor="hand2",
                           takefocus=False, bg=button_color, fg="#ffffff", width=15, height=2)
        button.pack(side=tk.TOP, pady=10)

    best_driver_button = tk.Button(frame_main, text="Best Driver(NVIDIA)", command=open_best_driver, cursor="hand2",
                                   takefocus=False, bg=button_color, fg="#ffffff", width=15, height=2)
    best_driver_button.pack(side=tk.TOP, pady=10)

    # Добавим дополнительные кнопки справа от основных кнопок
    frame_additional_buttons = tk.Frame(root, padx=10, pady=10, bg="#000000")
    frame_additional_buttons.place(relx=0.3, rely=0.45, anchor=tk.W)

    buttons_data_additional = [
        {"text": "Perfomance", "batch_file": "Performance.cmd"},
        {"text": "Hibernate", "batch_file": "Hibernate.cmd"},
        {"text": "Best CFG", "batch_file": "CFG.bat"},
        {"text": "TimerResolution", "batch_file": "TimerResolution.exe"},
        {"text": "Best PowerPlan", "batch_file": "PowerX.bat"},
    ]

    for data in buttons_data_additional:
        button = tk.Button(frame_additional_buttons, text=data["text"], command=lambda data=data: run_batch_file(data["batch_file"], target_folder), cursor="hand2",
                           takefocus=False, bg=button_color, fg="#ffffff", width=15, height=2)
        button.pack(side=tk.TOP, pady=10)

    close_button = tk.Button(root, text="ВЫХОД", font=("Arial", 8), bg="#000000", fg="#FFFFFF", bd=0, command=root.destroy)
    close_button.place(relx=0.98, rely=0.02, anchor=tk.NE)

    console_frame = tk.Frame(root, bg="#000000")
    console_frame.place(relx=0.9, rely=0.02, anchor=tk.NE)

    global console_text
    console_text = tk.Text(console_frame, wrap=tk.WORD, width=50, height=30, bg="#000000", fg="#FFFFFF", font=("Aviar", 10),
                           state=tk.DISABLED)
    console_text.pack()

    append_to_console("OPTIMIZATION by Miny X ", tag="optimization")

    append_to_console(" • Внимание!!! Если будете использовать Optimization GPU, то ищите там свою видеокарту. Например, она"
                      " будет называться вот так (Nvidia GeForce RTX 3060). У всех по-разному!")
    append_to_console(" • Если будете использовать Strip Fortnite, то знайте, что если у вас фортнайт не на C диске, то у"
                      " вас ничего не произойдет!")
    append_to_console("Спасибо, что выбрали нас!!!")

    icon = Image.open(icon_path)
    icon = icon.resize((16, 16), Image.LANCZOS if hasattr(Image, 'LANCZOS') else Image.BICUBIC)
    icon_photo = ImageTk.PhotoImage(icon)

    root.iconphoto(True, icon_photo)

    root.mainloop()

if __name__ == "__main__":
    open_main_window()
