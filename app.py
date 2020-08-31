from tkinter import *
from PIL import ImageTk, Image
import json, pyttsx3
from difflib import get_close_matches
import speech_recognition as sr 

# Functions

def clear_result():
    txt_result.config(state=NORMAL)
    txt_result.delete(1.0, END)
    txt_result.config(state=DISABLED)
    e_search.delete(0, END)

def search_similar(dict, query):
    if len(get_close_matches(query,dict.keys(),cutoff=0.7)) > 0:
        txt = "You Mean : \n"
        for word in get_close_matches(query,dict.keys(),cutoff=0.7):
            txt += f"- {word}\n"
        return txt
    else:
        return "Word Not Found!"

def search_value():
    dict = read_dictionary()
    query = e_search.get().lower()
    if query in dict.keys():
        txt_result.config(state=NORMAL)
        txt_result.delete(1.0, END)
        txt_result.insert(INSERT, str(dict[query]))
        txt_result.config(state=DISABLED)
    else:
        txt_result.config(state=NORMAL)
        txt_result.delete(1.0, END)
        txt = search_similar(dict, query)
        txt_result.insert(INSERT, txt)
        txt_result.config(state=DISABLED)

def read_dictionary():
    with open('WebstersEnglishDictionary.json') as f:
        return json.load(f)

def read_text():
    # print(txt_result.get(1.0, END))
    engine = pyttsx3.init()
    engine.say(txt_result.get(1.0, END))
    engine.setProperty('rate',120)  #120 words per minute
    engine.setProperty('volume',0.9) 
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    engine.runAndWait()

def listen_audio():
    r = sr.Recognizer() 
    try: 
        # use the microphone as source for input. 
        with sr.Microphone() as source2: 
            r.adjust_for_ambient_noise(source2, duration=0.2) 	
            #listens for the user's input 
            audio2 = r.listen(source2) 			
            # Using google to recognize audio 
            MyText = r.recognize_google(audio2) 
            MyText = MyText.lower() 
            print("Did you say "+MyText) 
            e_search.insert(0, MyText)	
            search_value()		
    except sr.RequestError as e: 
        txt_result.insert(INSERT, "Could not request results; {0}".format(e))
        print("Could not request results; {0}".format(e)) 		
    except sr.UnknownValueError: 
        txt_result.insert(INSERT, "unknown error occured")
        print("unknown error occured")


root = Tk()
# Dscription
root.title("Dictionary")
root.iconbitmap('images\\favicon.ico')

# App Label 
lbl_apptitle = Label(root, text="DICTIONARY", font=("Helvetica", 28, "bold"))
lbl_apptitle.grid(row=0, column=0, columnspan=5, pady=10, sticky=W+E)

# Search Box
e_search = Entry(root, font=("Helvetica", 16))
e_search.focus()
e_search.grid(row=1, column=0, columnspan=3, padx=4)
root.bind('<Escape>', lambda event: e_search.focus())

# Mic Button
img_mic = PhotoImage(file=r'./images/mic.png')
btn_mic = Button(root, image=img_mic, compound=LEFT, command=listen_audio)
btn_mic.grid(row=1, column=3, padx=4, ipadx=5)

# Search Button
img_search = PhotoImage(file=r'./images/search.png')
btn_search = Button(root, image=img_search, compound=LEFT, command=search_value)
btn_search.grid(row=1, column=4, padx=4, ipadx=5)
root.bind('<Return>', lambda event: search_value())

# Result Box 
txt_result = Text(root, width=40, height=10, state=DISABLED, relief='groove')
txt_result.grid(row=2, column=0, columnspan=5, padx=4, pady=10, sticky=W+E)

# Bottom Buttons - Speaker
img_speak = PhotoImage(file=r'./images/speaker.png')
btn_speak = Button(root, text=" Read ", image=img_speak, compound=LEFT, command=read_text)
btn_speak.grid(row=3, column=1, padx=4, pady=(0,10))

# Bottom Buttons - Reload
img_clear = PhotoImage(file=r'./images/reload.png')
btn_clear = Button(root, text=" Clear ", image=img_clear, compound=LEFT, command=clear_result)
btn_clear.grid(row=3, column=2, padx=4, pady=(0,10))
root.bind('<Control-r>', lambda event: clear_result())

# Bottom Buttons - Close
img_close = PhotoImage(file=r'./images/close.png')
btn_close = Button(root, text=" Close ", image=img_close, compound=LEFT, command=root.quit)
btn_close.grid(row=3, column=3, padx=4, pady=(0,10))
root.bind('<Control-w>', lambda event: root.quit())



root.mainloop()






