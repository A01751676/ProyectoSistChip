from tkinter import Button, Label,Tk,filedialog, ttk, Frame, PhotoImage
from SongRI import *
# a
# Start Tkinter for the interface
root = Tk()

# Principal window
root.title('Carrito')     # Define title
root.iconbitmap('icono.ico')
root.geometry('800x300')  # configure sice of screen
root.config(bg = 'black')
root.resizable(0,0)  

pygame.mixer.init()
pygame.mixer.init(frequency = 44100)
actual_song = ''
direction = ''

def open_file():
    global direction, pos, n, actual_song
    pos = 0
    n = 0
    direction = filedialog.askopenfilenames(initialdir = '/', title = 'Choose the song', filetype = (('mp3 files', '*.mp3'),('All files', '*.*')))

    n = len(direction)
    actual_song = direction[pos]

    song_name = actual_song.split('/')
    song_name = song_name[-1]

lista = []
for i in range (50,200,10):
    lista.append(i)

def start_playback():
    global actual_song, direction, pos, n, actualizar 
    bar1['value'] = random.choice(lista)
    bar2['value'] = random.choice(lista)
    bar3['value'] = random.choice(lista)
    bar4['value'] = random.choice(lista)
    bar5['value'] = random.choice(lista)
    bar6['value'] = random.choice(lista)
    bar7['value'] = random.choice(lista)
    bar8['value'] = random.choice(lista)
    bar9['value'] = random.choice(lista)
    bar10['value'] = random.choice(lista)
    bar11['value'] = random.choice(lista)
    bar12['value'] = random.choice(lista)
    bar13['value'] = random.choice(lista)
    bar14['value'] = random.choice(lista)
    bar15['value'] = random.choice(lista)
    bar16['value'] = random.choice(lista)
    bar17['value'] = random.choice(lista)
    bar18['value'] = random.choice(lista)
    bar19['value'] = random.choice(lista)
    bar20['value'] = random.choice(lista)

    actual_song = direction[pos]
    song_name = actual_song.split('/')
    song_name = song_name[-1]
    name['text'] = song_name

    time = pygame.mixer.music.get_pos()
    x = int(int(time)*0.001)
    tiempo['value'] = x

    y = float(int(volumen.get())*0.1)
    pygame.mixer.music.set_volume(y)
    level['text'] = int(y*100)

    audio = mutagen.File(actual_song)
    log = audio.info.length
    minutes, seconds = divmod(log, 60)

    minutes, seconds = int(minutes), int (seconds)
    tt = minutes * 60 + seconds
    tiempo['maximum'] = tt      # time of song
    texto['text'] = str(minutes) + ":" + str(seconds)

    actualizar = root.after(100, start_playback)

    if (x == tt):
        root.after_cancel(actualizar)
        texto['text'] = "00:00"
        stop_effect()

        if (pos != n):
            pos = pos + 1
            root.after(100, start_playback)
            pygame.mixer.music.play()

        if (pos == n):
            pos = 0   


def start():
    global actual_song

    pygame.mixer.music.load(actual_song)
    pygame.mixer.music.play()
    start_playback()

def backward():
    global pos, n

    if (pos > 0):
        pos = pos - 1
    else:
        pos = 0

    amount['text'] = str(pos) + '/' + str(n)

def forward():
    global pos, n

    if (pos == n - 1):
        pos = 0
    else: 
        pos = pos + 1
    
    amount['text'] = str(pos) + '/' + str(n)

def stop_effect():
    bar1['value'] = 50
    bar2['value'] = 60
    bar3['value'] = 70
    bar4['value'] = 80
    bar5['value'] = 90
    bar6['value'] = 100
    bar7['value'] = 90
    bar8['value'] = 80
    bar9['value'] = 70
    bar10['value'] = 60
    bar11['value'] = 60
    bar12['value'] = 70
    bar13['value'] = 80
    bar14['value'] = 90
    bar15['value'] = 100
    bar16['value'] = 90
    bar17['value'] = 80
    bar18['value'] = 70
    bar19['value'] = 60
    bar20['value'] = 50

def stop():
    global actualizar
    pygame.mixer.music.stop()
    root.after_cancel(actualizar)
    stop_effect()

def pause():
    global actualizar
    pygame.mixer.music.pause()
    root.after_cancel(actualizar)
    stop_effect()

def continuar():
    pygame.mixer.music.unpause()
    root.after(100, start_playback)

# Colores aleatorios
color1 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color2 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color3 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
color4 = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]

# estyle
estilo = ttk.Style()
estilo.theme_use('clam')
estilo.configure("Vertical.TProgressbar", foreground = color1, background = color2,troughcolor = 'black', bordercolor = 'black', lightcolor = color3, darkcolor = color4)

# Bar Frames
frame1 = Frame(root, bg = 'black', width = 600, height = 350)
frame1.grid(column = 0, row = 0, sticky = 'nsew')
frame2 = Frame(root, bg = 'black', width = 600, height = 50)
frame2.grid(column = 0, row = 1, sticky = 'nsew')

# Bars
bar1 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 300, style = 'Vertical.TProgressbar')
bar1. grid(column = 0, row = 0, rowspan = 3, padx = 1)
bar2 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 300, style = 'Vertical.TProgressbar')
bar2. grid(column = 1, row = 0, rowspan = 3, padx = 1)
bar3 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 300, style = 'Vertical.TProgressbar')
bar3. grid(column = 2, row = 0, rowspan = 3, padx = 1)
bar4 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar4. grid(column = 3, row = 0, rowspan = 3, padx = 1)
bar5 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar5. grid(column = 4, row = 0, rowspan = 3, padx = 1)
bar6 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar6. grid(column = 5, row = 0, rowspan = 3, padx = 1)
bar7 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar7. grid(column = 6, row = 0, rowspan = 3, padx = 1)
bar8 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar8. grid(column = 7, row = 0, rowspan = 3, padx = 1)
bar9 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar9. grid(column = 8, row = 0, rowspan = 3, padx = 1)
bar10 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar10. grid(column = 9, row = 0, rowspan = 3, padx = 1)
bar11 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar11. grid(column = 10, row = 0, rowspan = 3, padx = 1)
bar12 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar12. grid(column = 11, row = 0, rowspan = 3, padx = 1)
bar13 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar13. grid(column = 12, row = 0, rowspan = 3, padx = 1)
bar14 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar14. grid(column = 13, row = 0, rowspan = 3, padx = 1)
bar15 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar15. grid(column = 14, row = 0, rowspan = 3, padx = 1)
bar16 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar16. grid(column = 15, row = 0, rowspan = 3, padx = 1)
bar17 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar17. grid(column = 16, row = 0, rowspan = 3, padx = 1)
bar18 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar18. grid(column = 17, row = 0, rowspan = 3, padx = 1)
bar19 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar19. grid(column = 18, row = 0, rowspan = 3, padx = 1)
bar20 = ttk.Progressbar(frame1, orient = 'vertical', length = 200, maximum = 200, style = 'Vertical.TProgressbar')
bar20. grid(column = 19, row = 0, rowspan = 3, padx = 1)

# Song information 

style1 = ttk.Style()
style1.theme_use('clam')
style1.configure("Horizontal.TProgressbar", foreground = 'red', background = 'black', troughcolor = 'DarkOrchid1', bordercolor = '#970BD9', lightcolor = '#970BD9', darkcolor = 'black')

tiempo = ttk.Progressbar(frame2, orient = 'horizontal', length = 390, mode = 'determinate',style="Horizontal.TProgressbar")
tiempo.grid(row = 0, columnspan = 8, padx = 5)
texto = Label(frame2, bg ='black', fg ='green2', width = 5)
texto.grid(row = 0,column = 8)

name = Label(frame2, bg = 'black', fg = 'red', width = 55)
name.grid(column = 0, row = 1, columnspan = 8, padx = 5)
amount = Label(frame2, bg = 'black', fg = 'green2')
amount.grid(column = 8, row = 1)

image1 = PhotoImage(file = 'file.png')
image2 = PhotoImage(file = 'play.png')
image3 = PhotoImage(file = 'unpause.png')
image4 = PhotoImage(file = 'pause.png')
image5 = PhotoImage(file = 'continue.png')
image6 = PhotoImage(file = 'backward.png')
image7 = PhotoImage(file = 'forward.png')

Button_open_file = Button(frame2, image = image1, bg = color1, command = open_file)
Button_open_file.grid(column = 0, row = 2, pady = 10)
Button_start = Button(frame2, image = image2, bg = color2, command = start)
Button_start.grid(column = 1, row = 2, pady = 10)
Button_stop = Button(frame2, image = image3, bg = color3, command = stop)
Button_stop.grid(column = 2, row = 2, pady = 10)
Button_pause = Button(frame2, image = image4, bg = color4, command = pause)
Button_pause.grid(column = 3, row = 2, pady = 10)
Button_continue = Button(frame2, image = image5, bg = color3, command = continuar)
Button_continue.grid(column = 4, row = 2, pady = 10)
Button_backward = Button(frame2, image = image6, bg = color2, command = backward)
Button_backward.grid(column = 5, row = 2, pady = 10)
Button_forward = Button(frame2, image = image7, bg = color1, command = forward)
Button_forward.grid(column = 6, row = 2, pady = 10)

volumen = ttk.Scale(frame2, to = 10, from_ = 0, orient = 'horizontal', length = 90, style = 'Horizontal.TScale')
volumen.grid(column = 7, row = 2)

style = ttk.Style()
style.configure("Horizontal.TScale", bordercolor = 'green2', troughcolor = 'black', background = 'green2', foreground = 'green2', lightcolor = 'green2', darkcolor = 'black')

level = Label(frame2, bg = 'black', fg = 'green2', width = 3)
level.grid(column = 8, row = 2)



# Create an infinite loop
root.mainloop()



