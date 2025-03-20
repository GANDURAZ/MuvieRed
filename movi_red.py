from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from moviepy.video.fx.all import speedx
from tkinter import *
from tkinter import filedialog as fd
import threading
from tkinter import messagebox

def process_video_async(func, *args):
    def wrapper():
        try:
            func(*args)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")
    thread = threading.Thread(target=wrapper)
    thread.start()
    return thread

def rezka():
    def rez_get():
        start_time = float(start_time_Entry.get())
        end_time = float(end_time_Entry.get())
        name_file = fd.askopenfilename()
        process_video_async(ffmpeg_extract_subclip, name_file, start_time, end_time)
        rezkan.destroy()
    rezkan = Toplevel(root)
    rezkan.title("Окно нарезки")
    rezkan.geometry("800x800")
    start_time_Label = Label(rezkan, text="Введите время начала:")
    start_time_Label.grid(row=0, column=0)
    start_time_Entry = Entry(rezkan, width=30)
    start_time_Entry.grid(row=0, column=1)
    end_time_Label = Label(rezkan, text="Введите время конца:")
    end_time_Label.grid(row=1, column=0)
    end_time_Entry = Entry(rezkan, width=30)
    end_time_Entry.grid(row=1, column=1)    
    btm_file = Button(rezkan, text="Выбрать файл", command=lambda: rez_get())
    btm_file.grid(row=2, column=0)

def speedest():
    def speed_get():
        speed = float(speeds_Entry.get())
        video_dir = fd.askopenfilename()
        video = VideoFileClip(video_dir)
        video_fast = video.fx(speedx, speed)
        process_video_async(video_fast.write_videofile, "E:/fast_video.mp4")
        speeedest.destroy()
    speeedest = Toplevel(root)
    speeedest.title("Окно ускорения")
    speeedest.geometry("800x800")
    speeds_label = Label(speeedest, text="Введите X ускорения:")
    speeds_label.grid(row=0, column=0)
    speeds_Entry = Entry(speeedest, width=30)
    speeds_Entry.grid(row=0, column=1)
    btm_vidfile = Button(speeedest, text="Выбрать файл", command=lambda: speed_get())
    btm_vidfile.grid(row=1, column=0)

def comb():
    def combik_final():
        clips =[]
        collfile = int(combik_Entry.get())
        for i in range(collfile):
            combik_dir = fd.askopenfilename()
            clicks = VideoFileClip(combik_dir)
            clips.append(clicks)
        final = concatenate_videoclips(clips)
        process_video_async(final.write_videofile, "E:/comp_vid.mp4")
        combik.destroy()
    combik = Toplevel(root)
    combik.title("Окно соединения")
    combik.geometry("800x800")
    combik_label = Label(combik, text="Введите колличество файлов:")
    combik_label.grid(row=0, column=0)
    combik_Entry = Entry(combik, width=30)
    combik_Entry.grid(row=0, column=1)
    btm_combikfile = Button(combik, text="Выбрать файл", command=lambda: combik_final())
    btm_combikfile.grid(row=1, column=0)

root = Tk()
root.title("Редактор видосов")
root.geometry('800x600')
button1 = Button(root, text="Нарезка", command=rezka)
button1.grid(row=0, column=0)
button2 = Button(root, text="Ускорение", command=speedest)
button2.grid(row=0, column=1)
button3 = Button(root, text="Склеивание", command=comb)
button3.grid(row=0, column=2)
root.mainloop()
