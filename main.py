import aqgFunction
import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext 
from tkinter import INSERT
import speech_recognition as sr
from gtts import gTTS
import time
import playsound

def speak(text):
    filenum = time.strftime("%Y%m%d-%H%M%S")
    filename = f"voice{filenum}.mp3"
    tts = gTTS(text=text, lang="en")
    #filename= "voice.mp3"   
    tts.save(filename)
    playsound.playsound(filename)
   
def get_audio():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        try:
            said= r.recognize_google(audio)
            print(said)
        except Exception as e:
            print ("Exception: "+str(e))
    return said

# Main Function
def main():  
    window = tk.Tk()
    window.geometry("1920x1032")
    window.wm_title("Questions Module")
    #frames 
    frame_left = tk.Frame(window,width=640,height=1032,bd=2)
    frame_left.grid(row=0,column=0)
    
    frame_right = tk.Frame(window,width=1280,height=1032,bd=2)
    frame_right.grid(row=0,column=1)
    
    frame1 = tk.LabelFrame(frame_left,text="",width=600,height=800)
    frame1.grid(row=0,column=0)
    
    frame2 = tk.LabelFrame(frame_left,text="",width=600,height=200)
    frame2.grid(row=1,column=0)
    
    frame3 = tk.LabelFrame(frame_right,text="",width=600,height=800)
    frame3.grid(row=0,column=0)
    
    frame5 = tk.LabelFrame(frame_right,text="",width=600,height=200)
    frame5.grid(row=1,column=0)
    
    frame4 = tk.LabelFrame(frame_right,text="",width=600,height=800)
    frame4.grid(row=0,column=1)
    
    frame6 = tk.LabelFrame(frame_right,text="",width=600,height=200)
    frame6.grid(row=1,column=1)

    #frame1
    # Title Label 
    ttk.Label(frame1,  
              text = "Enter Text", 
              font = ("Footlight MT Light", 18),  
              foreground = "black").grid(column = 0,row = 0) 
      
    # Creating scrolled text  
    # area widget 
    text_area = scrolledtext.ScrolledText(frame1,  
                                          wrap = tk.WORD,  
                                          width = 46,  
                                          height = 24,  
                                          font = ("Times New Roman", 
                                                  15)) 
      
    text_area.grid(column = 0, pady = 10, padx = 10) 
    # Placing cursor in the text area 
    text_area.focus() 

    #frame2
    def soruUret():
        aqg = aqgFunction.AutomaticQuestionGenerator()
        global textAl
        textAl = text_area.get('1.0', tk.END)
        sorular = aqg.aqgParse(textAl)
        
        soruFormatindaSorular = aqg.display(sorular)
        #print("sorular1",soruFormatindaSorular)
        ayriSorular = soruFormatindaSorular.split("_")
        #print("sorular2",ayriSorular)
        
        for j in range(len(soruFormatindaSorular)):
            text_area2.insert(j+1,ayriSorular[j+1])
            print("\n")
        """
        uzunluk = len(sorular)
        uzunluk2= int((uzunluk-1)/3)
        global sample
        sample=[]
        i=0
        for j in range(uzunluk2):
            sample.append([])
            sample[j].append(sorular[i])
            sample[j].append(sorular[i+1])
            j+=1
            i=3*j   
            
        #print("Smple", sample)
        SadeceSoru = []
        uz = len(sample)
        uzint = int(uz)
        f = 0
        for i in range(uzint):
            SadeceSoru.append([])
            SadeceSoru[f].append(sample[i][0])
            SadeceSoru[f].append(i)
            i += 2
            f += 1
        for j in range(len(SadeceSoru)):
            text_area2.insert(j,SadeceSoru[j])
            #text_area2.yview(INSERT)
        """
    soru_uret_button = tk.Button(frame2,activeforeground = "red",foreground = "white",bg="red",bd=4,font = ("Footlight MT Light",15),activebackground="white",text="Generate Question",command = soruUret)
    soru_uret_button.place(relx=0.32,rely=0.28)
    
    tk.Label(frame3,  
              text = "Questions", 
              font = ("Footlight MT Light", 18),    
              foreground = "black").grid(column = 0, row = 0)   
    # Creating scrolled text  
    # area widget 
    text_area2 = tk.Listbox(frame3,
                            width = 59,
                            height = 30,  
                            font = ("Times New Roman", 12))
      
    text_area2.grid(column = 0, pady = 10, padx = 10) 
    var1 = tk.StringVar()
    questions = []
    def print_selection():
        value = text_area2.get(text_area2.curselection())  
        var1.set(value) 
        text_area3.insert(INSERT,value)
        text_area3.insert(INSERT,"\n")
        text_area2.delete(tk.ANCHOR)    
        questions.append(value)

    button_sec = tk.Button(frame5, text='Select Questions',activeforeground = "red",foreground = "white",bg="red",bd=4,font = ("Footlight MT Light",15),activebackground="white", command=print_selection)
    button_sec.place(relx=0.32,rely=0.28)
    
    #frame4
    tk.Label(frame4,  
              text = "Selected Questions", 
              font = ("Footlight MT Light", 18),    
              foreground = "black").grid(column = 0, row = 0) 
      
    # Creating scrolled text  
    # area widget 
    text_area3 = scrolledtext.ScrolledText(frame4,  
                                          wrap = tk.WORD,  
                                          width = 46,
                                          height = 24,  
                                          font = ("Times New Roman",15)) 
    
    text_area3.grid(column = 0, pady = 10, padx = 10)
    
    def SinavReading():
        speak("Reading exam is opening")
        windowReading = tk.Tk()
        windowReading.geometry("1920x1032")
        windowReading.wm_title("Reading Exam")
        
        frame_left_reading = tk.Frame(windowReading,width=640,height=1032,bd=2)
        frame_left_reading.grid(row=0,column=0)
    
        frame_right_reading = tk.Frame(windowReading,width=1280,height=1032,bd=2)
        frame_right_reading.grid(row=0,column=1)
        
        frame_reading1 = tk.LabelFrame(frame_left_reading,text="",width=600,height=1000)
        frame_reading1.grid(row=0,column=0)
        
        frame_reading3 = tk.LabelFrame(frame_right_reading,text="",width=600,height=800)
        frame_reading3.grid(row=0,column=0)
        
        frame_reading5 = tk.LabelFrame(frame_right_reading,text="",width=600,height=200)
        frame_reading5.grid(row=1,column=0)
        
        frame_reading4 = tk.LabelFrame(frame_right_reading,text="",width=600,height=800)
        frame_reading4.grid(row=0,column=1)
        
        frame_reading6 = tk.LabelFrame(frame_right_reading,text="",width=600,height=200)
        frame_reading6.grid(row=1,column=1)
        
        #frame_reading1
        # Title Label 
        ttk.Label(frame_reading1,  
                  text = "Text", 
                  font = ("Footlight MT Light", 18),  
                  foreground = "black").grid(column = 0,row = 0) 
          
        # Creating scrolled text  
        # area widget 
        text_area_reading = scrolledtext.ScrolledText(frame_reading1,  
                                                      wrap = tk.WORD,  
                                                      width = 46,  
                                                      height = 31,  
                                                      font = ("Times New Roman", 15)) 
          
        text_area_reading.insert(INSERT,textAl)
        text_area_reading.grid(column = 0, pady = 10, padx = 10) 
        # Placing cursor in the text area 
        text_area.focus() 
        #frame_reading3
        tk.Label(frame_reading3,  
              text = "Questions", 
              font = ("Footlight MT Light", 18),    
              foreground = "black").grid(column = 0, row = 0) 
        # Creating scrolled text  
        # area widget 
        text_area_reading_sorular = tk.Listbox(frame_reading3,
                                               width = 48,
                                               height = 23,  
                                               font = ("Times New Roman", 15))
        
        for j in range(len(questions)):
            text_area_reading_sorular.insert(j,questions[j])
        
        text_area_reading_sorular.grid(column = 0, pady = 10, padx = 10) 
        
        def print_selection_frame_reading3():
            value = text_area_reading_sorular.get(text_area_reading_sorular.curselection()) 
            answer_question=  value[1]
            answerquestion=sample[answer_question][1]
            print("value",sample)
            speak(value[0])
            konus =get_audio()
            print ("Konus", konus)
            text_area3.insert(INSERT,"Your answer:\n")  
            text_area3.insert(INSERT,konus )
            text_area3.insert(INSERT,"\nTrue answer is: \n")  
            text_area3.insert(INSERT,answerquestion[0])
            text_area3.insert(INSERT,"\n")
            answerquestion1=answerquestion[0]
            if konus in answerquestion1:
                text_area3.insert(INSERT,"Your answer is\n")  
                text_area3.insert(INSERT,"True \n")    
            if konus not in answerquestion1:
                text_area3.insert(INSERT,"Your answe is \n")  
                text_area3.insert(INSERT,"False\n")    

            text_area2.delete(tk.ANCHOR)        
 
        button_sec = tk.Button(frame_reading5,width = 15,height = 2, text='Answer',activeforeground = "red",foreground = "white",bg="red",bd=4,font = ("Footlight MT Light",15),activebackground="white", command=print_selection_frame_reading3)
        button_sec.place(relx=0.30,rely=0.24)
        
        #framereading4
        tk.Label(frame_reading4,  
                  text = "Answers", 
                  font = ("Footlight MT Light", 18),    
                  foreground = "black").grid(column = 0, row = 0) 
          
        # Creating scrolled text  
        # area widget 
        text_area3 = scrolledtext.ScrolledText(frame_reading4,  
                                              wrap = tk.WORD,  
                                              width = 46,
                                              height = 24,  
                                              font = ("Times New Roman",15)) 
        
        text_area3.grid(column = 0, pady = 10, padx = 10)
        
        def on_closing_listening():
            #if messagebox.askokcancel("Quit", "Do you want to quit?"):
                windowReading.destroy()

        windowReading.protocol("WM_DELETE_WINDOW", on_closing_listening)
        
        button_kapat = tk.Button(frame_reading6,bg="red",activebackground="white",foreground = "white",activeforeground = "red",bd=4,font = ("Footlight MT Light",15), text='Close', width=15, height=2, command=on_closing_listening)
        button_kapat.place(relx=0.30,rely=0.24)
        
        windowReading.mainloop()
        
    def SinavListening():
        speak("Listening exam is opening")
        windowListening = tk.Tk()
        windowListening.geometry("1920x1032")
        windowListening.wm_title("Listening Exam")
        
        frame_left_listening = tk.Frame(windowListening,width=640,height=1032,bd=2)
        frame_left_listening.grid(row=0,column=0)
    
        frame_right_listening = tk.Frame(windowListening,width=1280,height=1032,bd=2)
        frame_right_listening.grid(row=0,column=1)
        
        frame_listening1 = tk.LabelFrame(frame_left_listening,text="",width=640,height=970)
        frame_listening1.grid(row=0,column=0)
    
        frame_listening3 = tk.LabelFrame(frame_right_listening,text="",width=600,height=800)
        frame_listening3.grid(row=0,column=0)
        
        frame_listening5 = tk.LabelFrame(frame_right_listening,text="",width=600,height=200)
        frame_listening5.grid(row=1,column=0)
        
        frame_listening4 = tk.LabelFrame(frame_right_listening,text="",width=600,height=800)
        frame_listening4.grid(row=0,column=1)
        
        frame_listening6 = tk.LabelFrame(frame_right_listening,text="",width=600,height=200)
        frame_listening6.grid(row=1,column=1)
        
        #frame_listening2
        def seslendir():
            speak(textAl)
        
        seslendir_button = tk.Button(frame_listening1,bg="red",foreground = "white",activeforeground = "red",bd=4,font = ("Footlight MT Light",20),width = 20,height = 4,activebackground="white",text="Listen Text",command = seslendir)
        seslendir_button.place(relx=0.21,rely=0.35)
        
        #frame_listening3
        tk.Label(frame_listening3,  
              text = "Questions", 
              font = ("Footlight MT Light", 18),    
              foreground = "black").grid(column = 0, 
                                         row = 0) 
      
        # Creating scrolled text  
        # area widget 
        text_area_listening_sorular = tk.Listbox(frame_listening3,
                                width = 64,
                                height = 34,  
                                font = ("Times New Roman", 10)
                                )
        
        for j in range(len(questions)):
            text_area_listening_sorular.insert(j,questions[j])
        
        
        text_area_listening_sorular.grid(column = 0, pady = 10, padx = 10) 
        
        def print_selection_frame_listening():
            value = text_area_listening_sorular.get(text_area_listening_sorular.curselection()) 
            answer_question=  value[1]
            answerquestion=sample[answer_question][1]
            speak(value[0])
            konus2 =get_audio()
            text_area3.insert(INSERT,"Your answer:\n")  
            text_area3.insert(INSERT,konus2 )
            text_area3.insert(INSERT,"\nTrue answer is: \n")  
            text_area3.insert(INSERT,answerquestion[0])
            text_area3.insert(INSERT,"\n")
            answerquestion1=answerquestion[0]
            if konus2 in answerquestion1:
                text_area3.insert(INSERT,"Your answer is\n")  
                text_area3.insert(INSERT,"True \n")    
            if konus2 not in answerquestion1:
                text_area3.insert(INSERT,"Your answe is \n")  
                text_area3.insert(INSERT,"False\n")    

 
            text_area2.delete(tk.ANCHOR)
            
        button_sec = tk.Button(frame_listening5,bg="red",activebackground="white",foreground = "white",activeforeground = "red",bd=4,font = ("Footlight MT Light",15), text='Answer', width=15, height=2, command=print_selection_frame_listening)
        button_sec.place(relx=0.32,rely=0.24)
        
        #frame_listening4
        tk.Label(frame_listening4,  
                  text = "Answer", 
                  font = ("Footlight MT Light", 18),    
                  foreground = "black").grid(column = 0, 
                                             row = 0) 
          
        # Creating scrolled text  
        # area widget 
        text_area3 = scrolledtext.ScrolledText(frame_listening4,  
                                              wrap = tk.WORD,  
                                              width = 46,
                                              height = 24,  
                                              font = ("Times New Roman", 15)) 
        
        text_area3.grid(column = 0, pady = 10, padx = 10)
        
        def on_closing_listening():
            #if messagebox.askokcancel("Quit", "Do you want to quit?"):
                windowListening.destroy()

        windowListening.protocol("WM_DELETE_WINDOW", on_closing_listening)
        
        button_kapat = tk.Button(frame_listening6,bg="red",activebackground="white",foreground = "white",activeforeground = "red",bd=4,font = ("Footlight MT Light",15), text='Close', width=15, height=2, command=on_closing_listening)
        button_kapat.place(relx=0.32,rely=0.24)
        
        windowListening.mainloop()
    
    button_sinav = tk.Button(frame6, text='Reading Exam',activeforeground = "red",foreground = "white",bg="red",bd=4,font = ("Footlight MT Light",15),activebackground="white", command=SinavReading)
    button_sinav.place(relx=0.10,rely=0.28)
    
    button_sinav2 = tk.Button(frame6, text='Listening Exam', activeforeground = "red",foreground = "white",bg="red",bd=4,font = ("Footlight MT Light",15),activebackground="white", command=SinavListening)
    button_sinav2.place(relx=0.58,rely=0.29)
      
    
  
    window.mainloop()
    
    return 0
    

# Call Main Function
if __name__ == "__main__":
    main()

