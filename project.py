import moviepy.editor
from tkinter import *
from tkinter import filedialog
import pyperclip  # to copy url
import pyshorteners  # this library is used to shorten the link
import pytube  # for downloading youtube video
import speech_recognition as sr

root=Tk()
#VARIABLE SECTION

url = StringVar()
a = StringVar()
link1 = StringVar()

def short_del():
    global label_short
    global label_short2
    global entry_short
    global button_short
    global entry_short2
    global button_short2
    global backwaybutton
    label_short.grid_forget()
    label_short2.grid_forget()
    entry_short.grid_forget()
    button_short.grid_forget()
    entry_short2.grid_forget()
    button_short2.grid_forget()
    backwaybutton.grid_forget()
    second_page()


def shorterner_button():
    pagedel()
    global label_short
    global label_short2
    global entry_short
    global button_short
    global entry_short2
    global button_short2
    global backwaybutton
    label_short = Label(root, text="ARE YOU TIED OF USING LONG LINKS ?", font=("Phosphate", 50), fg="Black", bg="yellow")
    label_short2 = Label(root, text="DON'T WORRY WE HAVE A SOLUTION ""PASTE LINK BELOW TO SHOTEN", font=('Skia', 20), bg="Cyan",fg="white")
    entry_short =  Entry(root, textvariable=a, width=50)
    # to get input and store in a
    button_short = Button(text='click here', command=show, fg="pink", font=("Marker Felt", 15), height=3, width=10)  # a button which would trigger show() function
    entry_short2 =Entry(root, textvariable=link1)  # diaplays the shortened url
    button_short2 = Button(root, command=easycopy, text='COPY', font=('Marker Felt', 10), height=3, width=10, ) # button to copy the shortened url
    backwaybutton = Button(root ,text =">>" ,command = short_del)
    label_short.grid(row = 0 ,column = 0 ,columnspan = 2)
    label_short2.grid(row = 1 ,column = 0 ,columnspan = 2)
    entry_short.grid(row = 2 ,column = 0 ,columnspan = 2)
    button_short.grid(row = 3 ,column = 0 ,columnspan = 2)
    entry_short2.grid(row = 4 ,column = 0 ,columnspan = 2)
    button_short2.grid(row = 5 ,column = 0 ,columnspan = 2)
    backwaybutton.grid(row = 6 ,column = 1 ,columnspan = 2)



def show():  # this function isto shorten the link
    short = a.get()  # gets the variable a
    linkS = pyshorteners.Shortener().tinyurl.short(short)  # shorten the url using a thirdparty "tinyurl"
    link1.set(linkS)


def easycopy():  # function to copy the shorten url
    linkS = link1.get()
    pyperclip.copy(linkS)  # code to copy

def text():
    AUD = filedialog.askopenfilename()
    r = sr.Recognizer()
    with sr.AudioFile(AUD) as source:
        audio = r.record(source)  # read the entire audio file
    print("converting..............")
    print(r.recognize_google(audio))



def aud_txt_del():
    global label_aud_txt
    global aud_txt_covbutton
    global aud_txt_back

    label_aud_txt.grid_forget()
    aud_txt_covbutton.grid_forget()
    aud_txt_back.grid_forget()
    second_page()

def audio_to_text():
    pagedel()

    global label_aud_txt
    global aud_txt_covbutton
    global aud_txt_back
    label_aud_txt = Label(text="click the button below to convert")
    aud_txt_covbutton = Button(text="browse...", font=("Herculanum",), command=text )
    aud_txt_back = Button(root , text = ">>" , command = aud_txt_del)
    label_aud_txt.grid(row = 0 ,column =0)
    aud_txt_covbutton.grid(row = 1,column =0)
    aud_txt_back.grid(row =2 , column = 1)

def pagedel ():
    global short_url
    global youtube_download
    global vid_aud
    global aud_txt

    short_url.grid_forget()
    youtube_download.grid_forget()
    vid_aud.grid_forget()
    aud_txt.grid_forget()
    aud_txt.grid_forget()



def path_folder():
    root.filename = filedialog.askopenfilename()
    video = moviepy.editor.VideoFileClip(root.filename )
    audio = video.audio
    audio.write_audiofile('audio.wav')

def vid_aud_del():
    global vdotoaud
    global convert_button
    global vid_auidiobac
    vdotoaud.grid_forget()
    convert_button.grid_forget()
    vid_auidiobac.grid_forget()
    second_page()


def vid_audioButton ():

    pagedel()
    global vdotoaud
    global convert_button
    global vid_auidiobac
    vdotoaud= Label(root , text ="VIDEO TO AUDIO CONVERTER")
    convert_button = Button(root ,text = "Browse..." ,command = path_folder)
    vid_auidiobac = Button(root , text =">>" , command = vid_aud_del )
    vdotoaud.grid(row = 0 , column = 0)
    convert_button.grid(row = 1 , column = 0)
    vid_auidiobac.grid(row =2 ,column = 1)




def yt_del() :

    global text_ytdownload1
    global text_ytdownload2
    global yt_entry
    global download_button
    global go_back
    global  fact1
    global fact

    text_ytdownload1.grid_forget()
    text_ytdownload2.grid_forget()
    yt_entry.grid_forget()
    download_button.grid_forget()
    go_back.grid_forget()
    fact.grid_forget()
    fact1.grid_forget()

    second_page()



def second_page():
    global short_url
    global youtube_download
    global vid_aud
    global aud_txt
    start_button.grid_forget()
    names.grid_forget()
    short_url=Button(root,text='SHORTEN YOUR URL',width=60,height=9,bg='paleTurquoise4',activebackground='lavender' ,command = shorterner_button)
    youtube_download =Button(root,text='DOWNLOAD YOUTUBE VIDEO',width=60,height=9,bg='paleTurquoise3',activebackground='lavender' ,command = youtube_button)
    vid_aud=Button(root,text='VIDEO TO AUDIO',width=60,height=9,bg='paleTurquoise2',activebackground='lavender' ,command= vid_audioButton)
    aud_txt=Button(root,text='AUDIO TO TEXT',width=60,height=9,bg='paleTurquoise1',activebackground='lavender' ,command = audio_to_text)

    short_url.grid(row=1,column=0)
    youtube_download.grid(row=2,column=0)
    vid_aud.grid(row=3,column=0)
    aud_txt.grid(row=4,column=0)


# YOUTUBE VIDEO DOWNLOAD SECTION

def download():
    location = filedialog.askdirectory()
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download(location)

    except Exception as e:
        print(e)
def youtube_button():

    pagedel()

    global text_ytdownload1
    global text_ytdownload2
    global yt_entry
    global download_button
    global go_back
    global  fact1
    global fact
    go_back = Button(root , text =">>", command = yt_del , bg = "red")
    go_back.grid(row =6,column =1)
    fact1 = Label(root, text='500 hours of video are uploaded to YouTube every minute', font=('Normal', 17))
    fact = Label(root, text='YOUTUBE', fg='white', bg='#c4302b', font=("Bold", 30))
    text_ytdownload1 = Label(root, text="WANT TO DOWNLOAD YOUTUBE VIDEO?", font=("Phosphate", 30), bg='#c4302b',fg='white')
    text_ytdownload2 = Label(root, text="PASTE YOUR LINK HERE", bg="thistle3", font=("Zapfino", 15))
    yt_entry = Entry(root, width=50, textvariable=url, bg="thistle1")
    download_button = Button(root, text="download", height=3, width=12, bg="thistle2" ,command = download)
    text_ytdownload1.grid(row=0, column=0, padx=8, pady=21)
    text_ytdownload2.grid(row=1, column=0, pady=5)
    yt_entry.grid(row=2, column=0, pady=5)
    download_button.grid(row=3, column=0, pady=5)
    fact.grid(row = 4 ,column = 0 , padx = 3)
    fact1.grid(row = 5,column=0)


names =Label(root,text='SIDDHARTH\nSAI SUJEETH\nHEMANTH')
root.title('CS PROJECT')
start_button=Button(root,text='click me to start',command=second_page)

names.grid(row=0,column=0,padx=60,pady=36)
start_button.grid(row=1,column=0,padx=60,pady=36)
root.mainloop()
