import moviepy.editor
"""this library is used here to write audio file from an video"""
from tkinter import *
"""Tkinter is  GuiProgramming toolkit for Python"""
from tkinter import filedialog
"""used in this program to get the path of the folder and files"""
import pyperclip
"""used to copy the url"""
import pyshorteners
"""used to shorten the link """
import pytube
"""used to download youtube video"""
import speech_recognition as sr
"""used to recognize audio and convert to text"""

root = Tk()

# VARIABLE SECTION

url = StringVar()
a = StringVar()
link1 = StringVar()
b = StringVar()


def second_page():
    """this is basically the front page . it displays various button which take us to desired location . here the button defined are
    short_url which takes u to link shortner ,youtube_download- which takes u to a youtube video downloader ,vid_aud- takes you
     to audio extractor(extracts audio from video and give output in .wav codec) and aud_txt - recognises the audio and
      and make it to text and give output in .txt file"""

    global short_url
    global youtube_download
    global vid_aud
    global aud_txt

    # all the buttons are defined below
    # The Button widget is used to add buttons in a Python application. These buttons can display
    # text or images that convey the purpose of the buttons. You can attach a function or a method
    # to a button which is called automatically when you click the button

    short_url = Button(root, text='SHORTEN YOUR URL', width=60, height=9, bg='paleTurquoise4',
                       activebackground='lavender', command=shorterner_button)
    youtube_download = Button(root, text='DOWNLOAD YOUTUBE VIDEO', width=60, height=9, bg='paleTurquoise3',
                              activebackground='lavender', command=youtube_button)
    vid_aud = Button(root, text='VIDEO TO AUDIO', width=60, height=9, bg='paleTurquoise2', activebackground='lavender',
                     command=vid_audioButton)
    aud_txt = Button(root, text='AUDIO TO TEXT', width=60, height=9, bg='paleTurquoise1', activebackground='lavender',
                     command=audio_to_text)

    # The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split
    # into a number of rows and columns, and each “cell” in the resulting table can hold a widget

    short_url.grid(row=1, column=0)
    youtube_download.grid(row=2, column=0)
    vid_aud.grid(row=3, column=0)
    aud_txt.grid(row=4, column=0)


def pagedel():
    """this function basically clears all the buttons displayed from the second_page() function . this enables us to show
     the wigets like lables , buttons ,entry ,etc... which are invoked by clicking respective buttons on the same tab"""

    global short_url
    global youtube_download
    global vid_aud
    global aud_txt

    # If we want to unmap any widget from the screen or toplevel then forget() method is used. There
    # are two types of forget method forget_pack() ( similar to forget() ) and forget_grid() which are
    # used with pack() and grid() method respectively.

    short_url.grid_forget()
    youtube_download.grid_forget()
    vid_aud.grid_forget()
    aud_txt.grid_forget()
    aud_txt.grid_forget()


def shorterner_button():
    """this function is used in the command of short_url button defined in the second_page() function.
    it gets the link from user and displays the shortened  """
    # the shorterning process is done by other function called show() .

    pagedel()
    root.configure(bg='#12a4d9')

    global label_short
    global label_short2
    global entry_short
    global button_short
    global entry_short2
    global button_short2
    global backwaybutton

    # Lable section

    label_short = Label(root, text="ARE YOU TIRED OF USING LONG LINKS ?", font=("Phosphate", 35), fg="Black",
                        bg="#12a4d9")
    label_short2 = Label(root, text="DON'T WORRY WE HAVE A SOLUTION ""PASTE LINK BELOW TO SHOTEN", font=('Skia', 17),
                         bg="#12a4d9", fg="#d9138a")

    # entry section

    entry_short = Entry(root, width=50, bg='snow2')
    entry_short2 = Entry(root, bg='snow2')

    # buttons section

    button_short = Button(text='click here', fg="black", bg='#e2d810', font=('Helvetica', 9, 'bold'), height=2, width=9,
                          command=show)
    button_short2 = Button(root, text='COPY', font=('Helvetica', 10, 'bold'), height=2, width=7, fg='black',
                           bg='#e2d810', command=easycopy)
    backwaybutton = Button(root, text=">>", command=short_del)

    # The Grid geometry manager puts the widgets in a 2-dimensional table. The master widget is split
    # into a number of rows and columns, and each “cell” in the resulting table can hold a widget

    label_short.grid(row=0, column=0, columnspan=2, pady=6)
    label_short2.grid(row=1, column=0, columnspan=2, pady=6)
    entry_short.grid(row=2, column=0, columnspan=2, pady=6)
    button_short.grid(row=3, column=0, columnspan=2, pady=6)
    entry_short2.grid(row=4, column=0, columnspan=2, pady=6)
    button_short2.grid(row=5, column=0, columnspan=2, pady=6)
    backwaybutton.grid(row=6, column=2)


def short_del():
    '''this fucntion clears all the wigets present in the shorterner_button() function and calls back second_page()  '''
    # this function is used in the command backwaybutton present in shorterner_button()
    global label_short
    global label_short2
    global entry_short
    global button_short
    global entry_short2
    global button_short2
    global backwaybutton

    # unmap any widget from the screen or toplevel

    label_short.grid_forget()
    label_short2.grid_forget()
    entry_short.grid_forget()
    button_short.grid_forget()
    entry_short2.grid_forget()
    button_short2.grid_forget()
    backwaybutton.grid_forget()
    second_page()


def show():
    """shortens the url and return the shortened url"""

    short = a.get()  # gets the variable a
    linkS = pyshorteners.Shortener().tinyurl.short(short)  # shorten the url using a thirdparty "tinyurl"
    link1.set(linkS)


def easycopy():
    """function to copy the shortened url"""

    linkS = link1.get()
    pyperclip.copy(linkS)  # code to copy


def youtube_button():
    """this function gets the link of the youtube video that you want to download """
    # used in the command of youtube_download Button in the second_page() function

    pagedel()

    global text_ytdownload1
    global text_ytdownload2
    global yt_entry
    global download_button
    global go_back
    global fact1
    global fact

    # label section

    go_back = Button(root, text=">>", command=yt_del, bg="red")
    fact1 = Label(root, text='500 hours of video are uploaded to YouTube every minute', font=('Normal', 17))
    fact = Label(root, text='YOUTUBE', fg='white', bg='#c4302b', font=("Bold", 30))
    text_ytdownload1 = Label(root, text="WANT TO DOWNLOAD YOUTUBE VIDEO?", font=("Phosphate", 30), bg='#c4302b',
                             fg='white')
    text_ytdownload2 = Label(root, text="PASTE YOUR LINK HERE", bg="thistle3", font=("Zapfino", 15))

    # entry section

    yt_entry = Entry(root, width=50, textvariable=url, bg="thistle1")

    # button section

    download_button = Button(root, text="download", height=3, width=12, bg="thistle2", command=download)

    #  puts the widgets in a 2-dimensional table

    text_ytdownload1.grid(row=0, column=0, padx=8, pady=21)
    text_ytdownload2.grid(row=1, column=0, pady=5)
    yt_entry.grid(row=2, column=0, pady=5)
    download_button.grid(row=3, column=0, pady=5)
    fact.grid(row=4, column=0, padx=3)
    fact1.grid(row=5, column=0)
    go_back.grid(row=6, column=1)


def download():
    """downloads the youtube video and also gets the path of the folder where you want to save the downloaded video"""

    location = filedialog.askdirectory()
    video_url = url.get()

    # When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
    # These exceptions can be handled using the try statement Since the try block raises an error, the except block will be executed.
    # Without the try block, the program will crash and raise an error

    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download(location)

    except Exception as e:
        print(e)


def yt_del():
    """this function will clear all the wigets in the screen which is present after calling  youtube_download() .
     it also also calls the second_page function so we return back to the initial page"""

    global text_ytdownload1
    global text_ytdownload2
    global yt_entry
    global download_button
    global go_back
    global fact1
    global fact

    # unmap any widget from the screen or toplevel

    text_ytdownload1.grid_forget()
    text_ytdownload2.grid_forget()
    yt_entry.grid_forget()
    download_button.grid_forget()
    go_back.grid_forget()
    fact.grid_forget()
    fact1.grid_forget()

    second_page()


def vid_audioButton():
    """this function specifies the look of the tab once we click vid_audiobutton  """

    pagedel()
    root.configure(bg='royal blue')

    global vdotoaud
    global convert_button
    global vid_auidiobac
    global vid_aud

    # label section

    vdotoaud = Label(root, text="VIDEO TO AUDIO CONVERTER", font=('normal', 24), bg='royal blue', fg='black')
    vid_aud = Label(root,
                    text=' 79% OF CONSUMERS WOULD RATHER WATCH A VIDEO TO LEARN ABOUT\n A PRODUCT, THAN READ TEXT ON A PAGE.',
                    fg='peach puff', font=('bold', 12), bg='royal blue')

    # button section

    convert_button = Button(root, text="Browse...", bg='peach puff', fg='black', activebackground='paleTurquoise2',
                            width=10, height=2, font=('normal', 12), command=path_folder)
    vid_auidiobac = Button(root, text=">>", bg='peach puff', command=vid_aud_del)

    # The Grid geometry manager puts the widgets in a 2-dimensional table

    vdotoaud.grid(row=0, column=0, padx=74, pady=15)
    convert_button.grid(row=3, column=0)
    vid_aud.grid(row=4, column=0, pady=15)
    vid_auidiobac.grid(row=5, column=1)


def path_folder():
    """it gets the path of a video file and writes the audio file in .wav codec from a video """

    root.filename = filedialog.askopenfilename()
    video = moviepy.editor.VideoFileClip(root.filename)
    audio = video.audio
    audio.write_audiofile("audio.wav")


def vid_aud_del():
    """this function clears all the wigets which were invoked due to video_audiobutton() and
    calls the second_page() """

    global vdotoaud
    global convert_button
    global vid_auidiobac
    global vid_aud

    # unmap any widget from the screen or toplevel

    vdotoaud.grid_forget()
    convert_button.grid_forget()
    vid_auidiobac.grid_forget()
    vid_aud.grid_forget()

    second_page()


def audio_to_text():
    pagedel()
    root.configure(bg='light blue')

    global label_aud_txt
    global aud_txt_covbutton
    global aud_txt_back
    global aud_tex1
    global aud_tex2
    global name
    global Lable_name

    # entry section

    name = Entry(root, width=50, textvariable=b, bg="thistle1")

    # label section

    Lable_name = Label(root, text="enter the name of the text file in which you want to store the text ")
    aud_tex1 = Label(root, text='AUDIO TO TEXT', font=("Phosphate", 30), bg='light blue')
    aud_tex2 = Label(text='AUDIO RECORDING TECHNOLOGY WAS HIDDEN FROM REST OF THE WORLD FOR\n 15 YEARS BY NAZI REGIME',
                     font=('normal', 12), bg='light blue')
    label_aud_txt = Label(text="click the button below to convert", font=('normal', 26), bg='light blue')

    # button section

    aud_txt_covbutton = Button(text="browse...", font=("Herculanum",), activebackground='cornsilk2', command=text)
    aud_txt_back = Button(root, text=">>", command=aud_txt_del)

    # The Grid geometry manager puts the widgets in a 2-dimensional table

    name.grid(row=2, column=0, pady=5)
    Lable_name.grid(row=1, column=0)
    label_aud_txt.grid(row=3, column=0, padx=5)
    aud_txt_covbutton.grid(row=4, column=0, pady=20)
    aud_tex1.grid(row=0, column=0, padx=168, pady=25)
    aud_tex2.grid(row=5, column=0)
    aud_txt_back.grid(row=6, column=1)


def text():
    """get the path of the audio file and recognizes the audio and convert it to text and return in a .txt file"""

    global name

    AUD = filedialog.askopenfilename()
    r = sr.Recognizer()

    # with statement in Python is used in exception handling to make the code cleaner and much more readable.
    # It simplifies the management of common resources like file streams

    with sr.AudioFile(AUD) as source:
        audio = r.record(source)  # read the entire audio file
    print("converting..............")
    print(r.recognize_google(audio))
    file = open(b.get() + ".txt", 'w+')
    file.write(r.recognize_google(audio))
    file.close()


def aud_txt_del():
    """clears all the wigets which was invoked by the audio_to_text and calls back back second_page() function """

    global label_aud_txt
    global aud_txt_covbutton
    global aud_txt_back
    global aud_tex1
    global aud_tex2
    global name
    global Lable_name

    # unmap any widget from the screen or toplevel

    name.grid_forget()
    Lable_name.grid_forget()
    label_aud_txt.grid_forget()
    aud_txt_covbutton.grid_forget()
    aud_txt_back.grid_forget()
    aud_tex1.grid_forget()
    aud_tex2.grid_forget()
    second_page()


second_page()

root.mainloop()
