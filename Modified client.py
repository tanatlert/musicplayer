import tkinter.messagebox

import tkinter
from tkinter.ttk import Progressbar
import customtkinter
import pygame
from PIL import Image, ImageTk
from threading import *
import time
import math

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#golbal 
clicktime = 0
n = 0
list_of_songs =[]
list_of_covers =[]


class App(customtkinter.CTk):

    WIDTH = 500
    HEIGHT = 530

    def __init__(self):
        super().__init__()
        global list_of_songs
        global list_of_covers

        self.title("Music Player with copyright-free musics")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=100)  # empty row as spacing
        #self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Player",
                                              text_font=("Roboto Medium", -16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        


        statustext = "Play/Pause"

      
        pygame.mixer.init()

        list_of_songs1 = [ 'playlist1\K6Y and CHUNWEN - ตอนเช้า.wav','playlist1\Mints - Lovephobia.wav','playlist1\Sunkissed - Urworld.wav']
        list_of_covers1 = [ 'playlist1\K6Y and CHUNWEN - ตอนเช้า.png','playlist1\Mints - Lovephobia.png','playlist1\Sunkissed - Urworld.png']

        list_of_songs2 = [ 'playlist2\Cartoon - On and on.wav','playlist2\Cartoon - Why we lose.wav','playlist2\Lostsky -Where we stand.wav']
        list_of_covers2 = [ 'playlist2\Cartoon - On and on.png','playlist2\Cartoon - Why we lose.png','playlist2\Lostsky -Where we stand.png']
        
        list_of_songs3 = [ 'playlist3\Bugs -Duft Pank.wav','playlist3\Dior - Jaykar.wav','playlist3\Syncole -Gizmo.wav']
        list_of_covers3 = [ 'playlist3\Bugs -Duft Pank.png','playlist3\Dior - Jaykar.png','playlist3\Syncole -Gizmo.png']

        #preset
        list_of_songs = list_of_songs1
        list_of_covers = list_of_covers1

 
        def get_album_cover(song_name, n):
            global list_of_covers
         
            image1 = Image.open(list_of_covers[n])
            image2=image1.resize((300, 300))
            load = ImageTk.PhotoImage(image2)
            self.label1 = tkinter.Label(master=self.frame_left, image=load)
            self.label1.image = load
            self.label1.grid(row=3, column=0, pady=10, padx=0)

            #stripped_string = song_name[6:-4]
            
            self.labelname = customtkinter.CTkLabel(master=self.frame_left,
                                                   text="Playing: "+currentsong() ,
                                                   height=20,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
            self.labelname.grid(column=0, row=4, sticky="nwe", padx=30, pady=10)

            self.label_info_1 = customtkinter.CTkLabel(master=self.frame_left,
                                                   text="Next: "+nextsong() ,
                                                   height=20,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
            self.label_info_1.grid(column=0, row=8, sticky="nwe", padx=30, pady=20)

            


        def progress():
            global list_of_songs
            a = pygame.mixer.Sound(f'{list_of_songs[n]}')
            song_len = a.get_length() * 3
            for i in range(0, math.ceil(song_len)):
                time.sleep(.3)
                self.progressbar.set(pygame.mixer.music.get_pos() / 200000)

        def threading():
            t1 = Thread(target=progress)
            t1.start()

        def play_music(list_of_songs):
    
            threading()
            global n 
            current_song = n
            # if n > 2:
            #     n = 0
            song_name = list_of_songs[n]
            pygame.mixer.music.load(song_name)
            pygame.mixer.music.play(loops=0)
            pygame.mixer.music.set_volume(.5)
            get_album_cover(song_name, n)
            # print('PLAY')
            

        def currentsong():
            threading()
            global n 
            current_song = n
            # if n < 0:
            #     n = 2
            nextsong = list_of_songs[n]
            return nextsong[10:-3]
 
        #get next song name
        def nextsong():
            threading()
            global n 
            current_song = n
            if n >= 2:
                n = -1
            nextsong = list_of_songs[n+1]
            
            return nextsong[10:-3]

        #play playlist1
        def play1():
            global list_of_songs
            global list_of_covers
            list_of_covers = list_of_covers1
            list_of_songs = list_of_songs1
            play_music(list_of_songs1)
        def play2():
            global list_of_songs
            global list_of_covers
            list_of_covers = list_of_covers2
            list_of_songs = list_of_songs2
            play_music(list_of_songs2)
        def play3():
            global list_of_songs
            global list_of_covers
            list_of_covers = list_of_covers3
            list_of_songs = list_of_songs3
            play_music(list_of_songs3)

        #add pause option
        def play_status():
            global clicktime
            global list_of_songs
            if clicktime == 0:
                clicktime += 1
                print(clicktime)
                return play_music(list_of_songs)
            elif clicktime == 1:
                clicktime +=1
                print(clicktime)
                return pygame.mixer.music.pause()
            elif clicktime == 2:
                clicktime = 1
                print(clicktime)
                return pygame.mixer.music.unpause()


        def skip_forward():
            global list_of_songs
            global n
            n += 1
            if n > 2:
                n=-1
        
            play_music(list_of_songs)

        def skip_back():
            global list_of_songs
            global n
            n -= 1
            if n < -2:
                n=0
          
            play_music(list_of_songs)

        def volume(value):
            #print(value)
            pygame.mixer.music.set_volume(value)


        #add default status


        # Buttons
        self.play_button = customtkinter.CTkButton(master=self.frame_left, text=statustext, command=play_status)
        self.play_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

        self.skip_f = customtkinter.CTkButton(master=self.frame_left, text='>', command=skip_forward, width=2)
        self.skip_f.place(relx=0.85, rely=0.7, anchor=tkinter.CENTER)

        self.skip_b = customtkinter.CTkButton(master=self.frame_left, text='<', command=skip_back, width=2)
        self.skip_b.place(relx=0.15, rely=0.7, anchor=tkinter.CENTER)
        
        self.slider = customtkinter.CTkSlider(master=self.frame_left, from_= 0, to=1, command=volume, width=210)
        self.slider.grid(row=6,column=0, pady=10, padx=20)

        self.progressbar = customtkinter.CTkProgressBar(master=self.frame_left, progress_color='#32a85a', width=250)
        self.progressbar.grid(row=7,column=0, pady=10, padx=20)

        # self.playlist_button = customtkinter.CTkButton(master=self.frame_left, text="All Playlist", command=play_status)
        # self.playlist_button.grid(row=8,column=0, pady=10, padx=20)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_left,
                                                   text="Next: "+nextsong() ,
                                                   height=20,
                                                   fg_color=("white", "gray38"),  # <- custom tuple-color
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=8, sticky="nwe", padx=30, pady=20)
        
        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2), weight=1)
        #self.frame_right.rowconfigure(3, weight=0)
        self.frame_right.columnconfigure((0), weight=1)
        #self.frame_right.columnconfigure(2, weight=0)

        

        # ============ frame_info ============



        
        banner1 = Image.open(list_of_covers1[n])
        banner11=banner1.resize((175, 175))
        load = ImageTk.PhotoImage(banner11)
        self.bannerlabel1 = tkinter.Label(master=self.frame_right, image=load)
        self.bannerlabel1.image = load
        self.bannerlabel1.grid(row=0, column=0, pady=15, padx=15)

        self.playlist1 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Thai POP",
                                                         border_width=1,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=play1)
        self.playlist1.grid(row=0, column=0, pady=20, padx=20, sticky="swe")
        

        banner2 = Image.open(list_of_covers2[n])
        banner22=banner2.resize((175, 175))
        load = ImageTk.PhotoImage(banner22)
        self.bannerlabel2 = tkinter.Label(master=self.frame_right, image=load)
        self.bannerlabel2.image = load
        self.bannerlabel2.grid(row=1, column=0, pady=0, padx=15)

    
        self.playlist1 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="EDM",
                                                         border_width=1,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=play2)
        self.playlist1.grid(row=1, column=0, pady=20, padx=20, sticky="swe")
   
        banner3 = Image.open(list_of_covers3[n])
        banner33=banner3.resize((175, 175))
        load = ImageTk.PhotoImage(banner33)
        self.bannerlabel3 = tkinter.Label(master=self.frame_right, image=load)
        self.bannerlabel3.image = load
        self.bannerlabel3.grid(row=2, column=0, pady=15, padx=15)

        
        self.playlist1 = customtkinter.CTkButton(master=self.frame_right,
                                                         height=25,
                                                         text="Electronics",
                                                         border_width=1,   # <- custom border_width
                                                         fg_color=None,   # <- no fg_color
                                                         command=play3)
        self.playlist1.grid(row=2, column=0, pady=20, padx=20, sticky="swe")
        
    def button_event(self):
        print("Button pressed")

    

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()

