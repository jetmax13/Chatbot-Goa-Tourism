from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="",database="alphius")
mycursor=mydb.cursor()
import os
def main_screen():                                 
    global screen
    global login_button
    global register_button
    screen=Tk()
    screen.title("Login/Register")
    screen.geometry("550x550")
    Label(screen,text="Login Page").pack()
    Label(screen,text="").pack()
    login_button=Button(screen,text="Login",width=20,height=2,command=login).pack()
    Label(screen,text="").pack()

    register_button=Button(screen,text="Register",width=20,height=2,command=register).pack()

    
def login():                                     
    global screen1
    global loginusername
    global loginpassword
    global submit_login
    global usernameentryl
    global passwordentryl
    loginusername=StringVar()
    loginpassword=StringVar()
    
    
    screen1=Toplevel(screen)
    screen1.title("Login")
    screen1.geometry("550x550")
    

    Label(screen1,text="Enter the details").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username").pack()
    usernameentryl=Entry(screen1,textvariable=loginusername)
    usernameentryl.pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Password").pack()
    passwordentryl=Entry(screen1,textvariable=loginpassword,show="*")
    passwordentryl.pack()
    
    Label(screen1,text="").pack()
    submit_login=Button(screen1,text="Submit",command=loginsubmit).pack()

        
def register():
    global screen2
    global registerusername
    global registerpassword
    global usernameentryr
    global passwordentryr
    global submit_register
    registerusername=StringVar()
    registerpassword=StringVar()
    
       
    screen2=Toplevel(screen)
    screen2.title("Register")
    screen2.geometry("550x550")
    
    Label(screen2,text="Enter the details").pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Username").pack()
    usernameentryr=Entry(screen2,textvariable=registerusername)
    usernameentryr.pack()
    Label(screen2,text="").pack()
    Label(screen2,text="Password").pack()
    passwordentryr=Entry(screen2,textvariable=registerpassword,show="*")
    passwordentryr.pack()
    Label(screen2,text="").pack()
    submit_register=Button(screen2,text="Submit",command=registersubmit).pack()
    
def loginsubmit():
    usernamel=loginusername.get()
    passwordl=loginpassword.get()
    usernameentryl.delete(0,END)
    passwordentryl.delete(0,END)
    
    
    path = os.getcwd()
    f = os.listdir(path)
    corrected=usernamel+".txt"
    if corrected in f:
        filel=open(corrected,"r")
        verify=filel.read().splitlines()
        if passwordl in verify:
            Label(screen1,text="Login successful",fg="green").pack()
            mainscreen()
        else:
            Label(screen1,text="Incorrect password",fg="red").pack()
    else:
        Label(screen1,text="Incorrect username",fg="red").pack()
        
    
    
def registersubmit():
    usernamer=registerusername.get()
    passwordr=registerpassword.get()
    file=open(usernamer+".txt","w")
    file.write(usernamer+"\n")
    file.write(passwordr)
    file.close()
    usernameentryr.delete(0,END)
    passwordentryr.delete(0,END)
    Label(screen2,text="Registration successful",fg="green").pack()
def mainscreen():
    global window
    global scrollbar
    global logo
    window=Toplevel(screen)
    window.geometry("600x600")
    window.title("Chatbot")
    question = StringVar()
    title_label = Label(window, bd=3, relief=RAISED, width=730, compound=LEFT,
                        text="GOA TOURISM", font=("arial", 23, "bold"), bg="white", fg="green")
    title_label.pack()
    Label(window, text="").pack()
    logo = Image.open("goa.png")
    logo = logo.resize((250, 100), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(logo)
    Label(window, image=logo).pack()
    Label(window, text="Alphius: Hello!I am Alphius,your robot assistant").pack()
    Label(window, text="Alphius: I will be assisting and solving queries!").pack()
    Label(window, text="").pack()
    places = Button(window, text="Places to visit", width=20,
                    height=2, command=placescommand).pack()
    Label(window, text="").pack()
    hotels = Button(window, text="Hotels", width=20, height=2,
                    command=hotelscommand).pack()
    Label(window, text="").pack()
    transport = Button(window, text="How to reach", width=20,
                       height=2, command=transportcommand).pack()
    Label(window, text="").pack()
    restaurants = Button(window, text="Restaurants", width=20,
                         height=2, command=restaurantcommand).pack()
    Label(window, text="").pack()
    emergency = Button(window, text="Healthcare", width=20,
                       height=2, command=emergencycommand).pack()
    Label(window, text="").pack()
    feedback = Button(window, text="Feedback", width=20,
                         height=2, command=feedbackcommand).pack()
    

def placescommand():
    global texta
    global questionentrya
    global a
    global questiona
    global scrollbara
    global submita
    global yscrollcommand
    
    a = Toplevel(window)
    a.geometry("550x550")
    a.title("Places to Visit")
    questiona = StringVar()
    scrollbara = ttk.Scrollbar(a, orient='vertical')
    yscrollcommanda = scrollbara.set
    scrollbara.pack(side=RIGHT, fill=Y)
    Label(a, text="Type Something", font=("normal", 10)).place(x=10, y=500)
    questionentrya = Entry(a, textvariable=questiona, width=50)
    questionentrya.place(x=120, y=500)
    submita = Button(a, text="Submit", width=10, height=1,
                     command=submitcommanda).place(x=430, y=500)
    texta = Text(a, width=65, height=20, bd=4, relief=RAISED,
                 font=("normal", 12), yscrollcommand=scrollbara.set)
    scrollbara.pack(side=RIGHT, fill=Y)
    texta.pack()
    texta.insert(
        END, '\nAlphius: What type of destination would you like to visit?(Beach/Monument/Waterfall/Island)')
    
    
def submitcommanda():
    global senta
    senta = ("You: "+questionentrya.get())
    texta.insert(END, '\n\n'+senta)
    texta.yview(END)
    if (questionentrya.get() == ''):
        Label(a, text="").pack()
        Label(a, text="").pack()
        Label(a, text="No input", fg="red").pack()
    elif (questionentrya.get() == 'beach' or questionentrya.get() == 'Beach'):
        texta.insert(
            END, '\n\nAlphius: Calangute Beach\nBaga Beach\nCandolim Beach\nVagator Beach\nAnjuna Beach\nEnter the place name to get rating out of 5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'calangute' or questionentrya.get() == 'Calangute Beach'):
        texta.insert(END, '\n\nAlphius: 4.5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'baga' or questionentrya.get() == 'Baga Beach'):
        texta.insert(END, '\n\nAlphius: 4')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'candolim' or questionentrya.get() == 'Candolim Beach'):
        texta.insert(END, '\n\nAlphius: 4')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'vagator' or questionentrya.get() == 'Vagator Beach'):
        texta.insert(END, '\n\nAlphius: 3.5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'anjuna' or questionentrya.get() == 'Anjuna Beach'):
        texta.insert(END, '\n\nAlphius: 4')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'monument' or questionentrya.get() == 'Monument'):
        texta.insert(
            END, '\n\nAlphius: Fort Aguada\nBasilica de Bom Jesus\nSinquerim Fort\nEnter the place name to get rating out of 5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Fort Aguada'):
        texta.insert(END, '\n\nAlphius: 4.5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Basilica de Bom Jesus'):
        texta.insert(END, '\n\nAlphius: 4')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Sinquerim Fort'):
        texta.insert(END, '\n\nAlphius: 3.5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Island' or questionentrya.get() == 'island'):
        texta.insert(
            END, '\n\nAlphius: Divar Island\nGrand Island\nMalvan Island\nEnter the place name to get rating out of 5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Divar Island' or questionentrya.get() == 'divar'):
        texta.insert(END, '\n\nAlphius: 4.5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Grand Island' or questionentrya.get() == 'grand'):
        texta.insert(END, '\n\nAlphius: 4')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Malvan Island' or questionentrya.get() == 'malvan'):
        texta.insert(END, '\n\nAlphius: 3.5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'waterfall' or questionentrya.get() == 'Waterfall'):
        texta.insert(
            END, '\n\nAlphius: Dudhsagar Falls\nNetravali Falls\nHivre Falls\nEnter the place name to get rating out of 5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Dudhsagar Falls' or questionentrya.get() == 'dudhsagar'):
        texta.insert(END, '\n\nAlphius: 4.5')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Netravali Falls' or questionentrya.get() == 'netravali'):
        texta.insert(END, '\n\nAlphius: 4')
        questionentrya.delete(0, END)
    elif (questionentrya.get() == 'Hivre Falls' or questionentrya.get() == 'hivre'):
        texta.insert(END, '\n\nAlphius: 3.5')
        questionentrya.delete(0, END)
    else:
        texta.insert(END, '\n\nAlphius: Please enter valid details')
        questionentrya.delete(0, END)
    def get_input():
        value=texta.get("1.0",END)
        file=open("Places.txt","a")
        file.write(value+"\n")
    get_input()
    
def hotelscommand():

    global textb
    global questionentryb
    global b
    global questionb
    global scrollbarb
    global submitb
    global yscrollcommandb
    b = Toplevel(window)
    b.geometry("550x550")
    b.title("Hotels")
    questionb = StringVar()
    scrollbarb = ttk.Scrollbar(b, orient='vertical')
    yscrollcommandb = scrollbarb.set
    scrollbarb.pack(side=RIGHT, fill=Y)
    Label(b, text="Type Something", font=("normal", 10)).place(x=10, y=500)
    questionentryb = Entry(b, textvariable=questionb, width=50)
    questionentryb.place(x=120, y=500)
    submitb = Button(b, text="Submit", width=10, height=1,
                     command=submitcommandb).place(x=430, y=500)
    textb = Text(b, width=65, height=20, bd=4, relief=RAISED,
                 font=("normal", 12), yscrollcommand=scrollbarb.set)
    scrollbarb.pack(side=RIGHT, fill=Y)
    textb.pack()
    textb.insert(END, '\nAlphius: In which area would you like to get hotel?(Calangute/Candolim/Panaji/Margao/Sinquerim)')
    
    
    
def submitcommandb():
    global sentb
    sentb = ("You: "+questionentryb.get())
    textb.insert(END, '\n\n'+sentb)
    textb.yview(END)
    if (questionentryb.get() == ''):
        Label(b, text="").pack()
        Label(b, text="").pack()
        Label(b, text="No input", fg="red").pack()
    elif (questionentryb.get() == 'calangute' or questionentryb.get() == 'Calangute'):
        textb.insert(
            END, '\n\nAlphius: Fabhotel Casa De Baga\nCalanguta Residency\nShining Sand Beach Hotel\nTreebo Trend Dona Eliza\nEnter the hotel name to get price range for one night.')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Fabhotel Casa De Baga'):
        textb.insert(END, '\n\nAlphius: 2,000/- to 5,000/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Calanguta' or questionentryb.get() == 'Calanguta Residency'):
        textb.insert(END, '\n\nAlphius: 1,000/- to 4,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Shining Sand Beach Hotel' or questionentryb.get() == 'Shining Sand Beach'):
        textb.insert(END, '\n\nAlphius: 4,000/- to 9,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Treebo Trend Dona Eliza'):
        textb.insert(END, '\n\nAlphius: 3,000/- to 7,000/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Candolim' or questionentryb.get() == 'candolim'):
        textb.insert(END, '\n\nAlphius: Seasons in the Sun\nThe Postcard Moira\nRed Crab Eco Resort\nAgonda Beach villa\nEnter the hotel name to get price range for one night.')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Seasons in the Sun'):
        textb.insert(END, '\n\nAlphius: 1,000/- to 4,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'The Postcard Moira'):
        textb.insert(END, '\n\nAlphius: 2,000/- to 5,000/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Red Crab Eco Resort'):
        textb.insert(END, '\n\nAlphius: 1,000/- to 4,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Agonda Beach villa'):
        textb.insert(END, '\n\nAlphius: 4,000/- to 9,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Panaji' or questionentryb.get() == 'panaji'):
        textb.insert(
            END, '\n\nAlphius: Novotel Nia\nHyatt Centric\nStyles Goa\nEnter the hotel name to get price range for one night.')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Novotel Nia'):
        textb.insert(END, '\n\nAlphius: 1,000/- to 4,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Hyatt Centric'):
        textb.insert(END, '\n\nAlphius: 2,000/- to 5,000/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Styles Goa'):
        textb.insert(END, '\n\nAlphius: 4,000/- to 9,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Margao' or questionentryb.get() == 'margao'):
        textb.insert(
            END, '\n\nAlphius: Caravela Beach Resort\nFairfield by Marriott Goa\nEnter the hotel name to get price range for one night.')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Caravela Beach Resort'):
        textb.insert(END, '\n\nAlphius: 3,000/- to 7,000/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Fairfield by Marriott Goa'):
        textb.insert(END, '\n\nAlphius: 1,000/- to 4,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Sinquerim' or questionentryb.get() == 'sinquerim'):
        textb.insert(
            END, '\n\nAlphius: Vivanta Goa\nGrand Hyatt\nDoubletree by Hilton\nEnter the hotel name to get price range for one night.')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Vivanta Goa'):
        textb.insert(END, '\n\nAlphius: 1,000/- to 4,500/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Grand Hyatt'):
        textb.insert(END, '\n\nAlphius: 3,000/- to 7,000/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Doubletree by Hilton'):
        textb.insert(END, '\n\nAlphius: 2,000/- to 5,000/-')
        questionentryb.delete(0, END)    
    elif (questionentryb.get() == 'Vagator' or questionentryb.get() == 'vagator'):
        textb.insert(
            END, '\n\nAlphius: The Crown Goa\nCountry Inn by Radisson\nEnter the hotel name to get price range for one night.')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'The Crown Goa'):
        textb.insert(END, '\n\nAlphius: 3,000/- to 7,000/-')
        questionentryb.delete(0, END)
    elif (questionentryb.get() == 'Country Inn by Radisson'):
        textb.insert(END, '\n\nAlphius: 4,000/- to 9,500/-')
        questionentryb.delete(0, END)
    else:
        textb.insert(END, '\n\nAlphius: Please enter valid details')
        questionentryb.delete(0, END)
    def get_input():
        value=textb.get("1.0",END)
        file=open("Hotels.txt","a")
        file.write(value+"\n")
        
        
    get_input()

def transportcommand():

    global textc
    global questionentryc
    global c
    global questionc
    global scrollbarc
    global submitc
    global yscrollcommandc
    c = Toplevel(window)
    c.geometry("550x550")
    c.title("How to Reach")
    questionc = StringVar()
    scrollbarc = ttk.Scrollbar(c, orient='vertical')
    yscrollcommandc = scrollbarc.set
    scrollbarc.pack(side=RIGHT, fill=Y)
    Label(c, text="Type Something", font=("normal", 10)).place(x=10, y=500)
    questionentryc = Entry(c, textvariable=questionc, width=50)
    questionentryc.place(x=120, y=500)
    submitc = Button(c, text="Submit", width=10, height=1,
                     command=submitcommandc).place(x=430, y=500)
    textc = Text(c, width=65, height=20, bd=4, relief=RAISED,
                 font=("normal", 12), yscrollcommand=scrollbarc.set)
    scrollbarc.pack(side=RIGHT, fill=Y)
    textc.pack()
    textc.insert(
        END, '\nAlphius: Which mode of transport will you prefer?(Flight/Train/Bus)')
    

def submitcommandc():
    
    
    global sentc
    sentc=("You:"+questionentryc.get())
    textc.insert(END,'\n'+sentc)
    textc.yview(END)
    if(questionentryc.get()==''):
        Label(c,text="").pack()
        Label(c,text="").pack()
        Label(c,text="No input",fg="red").pack()
    elif(questionentryc.get()=='Train' or questionentryc.get()=='train' ):
        textc.insert(END,'\n\nAlphius: From which junction would you like to come to Goa?(Ahmedabad,Bangalore,Kolkata,Mumbai,Delhi)')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Bus' or questionentryc.get()=='bus' ):
        textc.insert(END,'\n\nAlphius: From which bus depot would you like to come to Goa?(Ahmedabad,Bangalore,Kolkata,Mumbai,Delhi)')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Flight' or questionentryc.get()=='flight' ):
        textc.insert(END,'\n\nAlphius: From which airport would you like to come to Goa?(Ahmedabad,Bangalore,Kolkata,Mumbai,Delhi)')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Ahmedabad Junction' or questionentryc.get()=='ahmedabad junction' ):
        textc.insert(END,'\n\nAlphius: Jamnagar-Tirunelveli Express\nDeparture: Ahmedabad\nDestination: Madgaon\nDay: Sat-Sun\nTimings: 03:15-22:20')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Ahmedabad Airport' or questionentryc.get()=='ahmedabadflight' ):
        textc.insert(END,'\n\nAlphius: Ahmedabad-Goa\nFlight: SpiceJet\nDay: Tue\nTimings: 13:40-14:45')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Ahmedabad Bus Depot' or questionentryc.get()=='ahmedabad bus depot' ):
        textc.insert(END,'\n\nAlphius: Ahmedabad-Madgaon Roadways\nDeparture: Ahmedabad\nDestination: Madgaon\nDay: Mon,Tue\nTimings: 20:45-07:00')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Bangalore Junction' or questionentryc.get()=='bangalore junction' ):
        textc.insert(END,'\n\nAlphius: Yeswantpur-Vasco Express\nDeparture: Bangalore\nDestination: Madgaon\nDay: Wed\nTimings: 11:58-01:30')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Bangalore Airport' or questionentryc.get()=='bangalore flight' ):
        textc.insert(END,'\n\nAlphius: Bangalore-Goa\nFlight: Indigo\nDay: Wed\nTimings: 04:30-17:45')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Bangalore Bus Depot' or questionentryc.get()=='bangalore bus depot' ):
        textc.insert(END,'\n\n Alphius: Bangalore-panaji Roadways\nDeparture: Bangalore\nDestination: Panji\nDay: Mon,Tue\nTimings: 18:15-07:30')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Kolkata Junction' or questionentryc.get()=='kolkata junction' ):
        textc.insert(END,'\n\nAlphius: Shalimar-Amaravati Express\nDeparture: Kolkata\nDestination: Madgaon\nDay: Mon,Tue,Thu,Sat\nTimings: 23:20-14:20')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Kolkata Airport' or questionentryc.get()=='kolkata flight' ):
        textc.insert(END,'\n\Kolkata-Goa\nFlight: GoFirst\nDay: Wed\nTimings: 09:40-16:30')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Kolkata Bus Depot' or questionentryc.get()=='kolkata bus depot' ):
        textc.insert(END,'\n\n Alphius: Kolkata-Goa Roadways\nDeparture: Kolkata\nDestination: Madgaon\nDay: All Days\nTimings: 20:45-07:00')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Mumbai Junction' or questionentryc.get()=='mumbai junction' ):
        textc.insert(END,'\n\nAlphius: Mumbai LTT-Madgaon Express\nDeparture: LTT\nDestination: Madgaon\nDay: Tue,Fri,Wed,Sat,Sun\nTimings: 00:45-11:30')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Mumbai Airport' or questionentryc.get()=='mumbai flight' ):
        textc.insert(END,'\n\nAlphius: Mumbai-Goa\nFlight: Jet Airways\nDay: Thu\nTimings: 15:20-16:40')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Mumbai Bus Depot' or questionentryc.get()=='mumbai bus depot' ):
        textc.insert(END,'\n\n Alphius: KTCL Mumbai-Goa Roadways\nDeparture: Mumbai\nDestination: Goa\nDay: All days\nTimings: 17:05-06:00')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Delhi Junction' or questionentryc.get()=='delhi junction' ):
        textc.insert(END,'\n\nAlphius: Hazarat Nizamuddin Express\nDeparture: Delhi\nDestination: Madgaon\nDay: All days\nTimings: 05:00-12:05')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Delhi Airport' or questionentryc.get()=='delhi flight' ):
        textc.insert(END,'\n\nAlphius: Delhi-Goa\nFlight: Air India\nDay: Thu\nTimings: 08:30-00:05')
        questionentryc.delete(0,END)
    elif(questionentryc.get()=='Delhi Bus Depot' or questionentryc.get()=='delhi bus depot' ):
        textc.insert(END,'\n\n Alphius: KTCL Delhi-Madgaon Roadways\nDeparture: Delhi\nDestination: Madgaon\nDay: Thu,Fri\nTimings: 18:20-02:00')
        questionentryc.delete(0,END)
    else:
        textc.insert(END, '\n\nAlphius: Please enter valid details')
        questionentryc.delete(0, END)
    def get_input():
        value=textc.get("1.0",END)
        file=open("How to Reach.txt","a")
        file.write(value+"\n")
        
        
    get_input()
        


def restaurantcommand():
    global textd
    global questionentryd
    global d
    global questiond
    global scrollbard
    global submitd
    global yscrollcommandd
    d = Toplevel(window)
    d.geometry("550x550")
    d.title("Restaurant")
    questiond = StringVar()
    scrollbard = ttk.Scrollbar(d, orient='vertical')
    yscrollcommandd = scrollbard.set
    scrollbard.pack(side=RIGHT, fill=Y)
    Label(d, text="Type Something", font=("normal", 10)).place(x=10, y=500)
    questionentryd = Entry(d, textvariable=questiond, width=50)
    questionentryd.place(x=120, y=500)
    submitd = Button(d, text="Submit", width=10, height=1,
                     command=submitcommandd).place(x=430, y=500)
    textd = Text(d, width=65, height=20, bd=4, relief=RAISED,
                 font=("normal", 12), yscrollcommand=scrollbard.set)
    scrollbard.pack(side=RIGHT, fill=Y)
    textd.pack()
    textd.insert(
        END, '\nAlphius: In which area would you like to get restaurant?(Calangute/Candolim/Panaji/Margao/Sinquerim)')
    

def submitcommandd():
    
    global sentd
    sentd = ("You: "+questionentryd.get())
    textd.insert(END, '\n\n'+sentd)
    textd.yview(END)
    if (questionentryd.get() == ''):
        Label(d, text="").pack()
        Label(d, text="").pack()
        Label(d, text="No input", fg="red").pack()
    elif (questionentryd.get() == 'calangute' or questionentryd.get() == 'Calangute'):
        textd.insert(
            END, '\n\nAlphius: Redonda Restaurant\nSouza lobo\nAggie'+"'" +'s Cafe\nChelesa Beach Shack\nEnter the Restaurant name to get rating out of 5.')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Redonda Restaurant'):
        textd.insert(END, '\n\nAlphius: 4.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Calanguta'):
        textd.insert(END, '\n\nAlphius: 3.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Aggie'+"'" +'s Cafe'):
        textd.insert(END, '\n\nAlphius: 4.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Chelesa Beach Shack'):
        textd.insert(END, '\n\nAlphius: 4')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Candolim' or questionentryd.get() == 'candolim'):
        textd.insert(END, '\n\nAlphius: Wok and Roll\nMomagato Aguada\nAdelaide Restaurant\nVishal' + "'" + 's Goan Food\nEnter the restaurant name to get rating out of 5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Wok and Roll'):
        textd.insert(END, '\n\nAlphius: 3.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Momagato Aguada'):
        textd.insert(END, '\n\nAlphius: 4.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Adelaide Restaurant'):
        textd.insert(END, '\n\nAlphius: 4')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Vishal' + "'" + 's Goan Food'):
        textd.insert(END, '\n\nAlphius: 4.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Panaji' or questionentryd.get() == 'panaji'):
        textd.insert(
            END, '\n\nAlphius: River Lounge Restaurant\nBoat Shack\nCapricorn Goa\nThe Pier\nEnter the restaurant name to get rating out of 5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'River Lounge Restaurant'):
        textd.insert(END, '\n\nAlphius: 3.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Boat Shack'):
        textd.insert(END, '\n\nAlphius: 4.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Capricorn Goa'):
        textd.insert(END, '\n\nAlphius: 5')
    elif (questionentryd.get() == 'The Pier'):
        textd.insert(END, '\n\nAlphius: 4')
        questionentryd.delete(0, END) 
    elif (questionentryd.get() == 'Margao' or questionentryd.get() == 'margao'):
        textd.insert(
            END, '\n\nAlphius: Akshay Café\nChhaya Restaurant\nJungle Book Café\nEnter the restaurant name to get rating out of 5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Akshay Café'):
        textd.insert(END, '\n\nAlphius: 4')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Chhaya Restaurant'):
        textd.insert(END, '\n\nAlphius: 4.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Sinquerin' or questionentryd.get() == 'sinquerin'):
        textd.insert(
            END, '\n\nAlphius: Baskin Robbins\nRatnasagar Family Restaurant \nBig Fun Restaurant\nEnter the restaurant name to get rating out of 5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Baskin Robbins'):
        textd.insert(END, '\n\nAlphius: 3.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Ratnasagar Family Restaurant'):
        textd.insert(END, '\n\nAlphius: 4.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Big Fun Restaurant'):
        textd.insert(END, '\n\nAlphius: 4')
        questionentryd.delete(0, END)    
    elif (questionentryd.get() == 'Vagator' or questionentryd.get() == 'vagator'):
        textd.insert(
            END, '\n\nAlphius: Avnish Restaurant\nBradlee Restaurant\nEnter the restaurant name to get rating out of 5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Avnish Restaurant'):
        textd.insert(END, '\n\nAlphius: 4.5')
        questionentryd.delete(0, END)
    elif (questionentryd.get() == 'Bradlee Restaurant'):
        textd.insert(END, '\n\nAlphius: 4')
        questionentryd.delete(0, END)
    else:
        textd.insert(END, '\n\nAlphius: Please enter valid details')
        questionentryd.delete(0, END)
    def get_input():
        value=textd.get("1.0",END)
        file=open("Restaurants.txt","a")
        file.write(value+"\n")
        
        
    get_input()

def emergencycommand():

    global texte
    global questionentrye
    global e
    global questione
    global scrollbare
    global submite
    global yscrollcommande
    e = Toplevel(window)
    e.geometry("550x550")
    e.title("Healthcare")
    questione = StringVar()
    scrollbare = ttk.Scrollbar(e, orient='vertical')
    yscrollcommande = scrollbare.set
    scrollbare.pack(side=RIGHT, fill=Y)
    Label(e, text="Type Something", font=("normal", 10)).place(x=10, y=500)
    questionentrye = Entry(e, textvariable=questione, width=50)
    questionentrye.place(x=120, y=500)
    submite = Button(e, text="Submit", width=10, height=1,
                     command=submitcommande).place(x=430, y=500)
    texte = Text(e, width=65, height=20, bd=4, relief=RAISED,
                 font=("normal", 12), yscrollcommand=scrollbare.set)
    scrollbare.pack(side=RIGHT, fill=Y)
    texte.pack()
    texte.insert(END, '\nAlphius: For which location you need healthcare?(Calangute/Candolim/Panaji/Margao/Sinquerim)')
    

def submitcommande():
    global sente
    sente=("You:"+questionentrye.get())
    texte.insert(END,'\n'+sente)
    texte.yview(END)
    if(questionentrye.get()==''):
        Label(e,text="").pack()
        Label(e,text="").pack()
        Label(e,text="No input",fg="red").pack()
    elif(questionentrye.get()=='Calangute' or questionentrye.get()=='calangute' ):
        texte.insert(END,'\n\nAlphius: Hospitals Nearby:\nBosio Hospital\nMathew Braganza Hospital\nShriram Hospital\nEnter the hospital name to get its Contact Info.')
        questionentrye.delete(0,END)
    elif(questionentrye.get()=='Candolim' or questionentrye.get()=='candolim' ):
        texte.insert(END,'\n\nAlphius: Hospitals Nearby:\nPrimary Health Center\nNavjeevan Nursing Home\nNeural Hospital\nEnter the hospital name to get its Contact Info.')
        questionentrye.delete(0,END)
    elif(questionentrye.get()=='Panaji' or questionentrye.get()=='panaji' ):
        texte.insert(END,'\n\nAlphius: Hospitals Nearby:\nAster Hospital\nESI Hospital\nBlue Shield Medical Center\nEnter the hospital name to get its Contact Info.')
        questionentrye.delete(0,END)
    elif(questionentrye.get()=='Margao' or questionentrye.get()=='margao' ):
        texte.insert(END,'\n\nAlphius: Hospitals Nearby:\nValpoi Manipal Center\nSonu Kamat Hospital\nCommunity Health Center\nEnter the hospital name to get its Contact Info.')
        questionentrye.delete(0,END)
    elif(questionentrye.get()=='Sinquerim' or questionentrye.get()=='sinquerim' ):
        texte.insert(END,'\n\nAlphius: Hospitals Nearby:\nSaud EMS Hosptal\nHealthway Hospital\nGovt Medical Emergency Hospital\nEnter the hospital name to get its Contact Info.')
        questionentrye.delete(0,END)
    elif(questionentrye.get()=='Vagator' or questionentrye.get()=='vagator' ):
        texte.insert(END,'\n\nAlphius: Hospitals Nearby:\nNew Vrundavan Hospital\nTrinity Healthcare and research institute\nShriram Hospital\nEnter the hospital name to get its Contact Info.')
        questionentrye.delete(0,END)
        
    elif(questionentrye.get()=='Bosio Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-8457824897')
        questionentrye.delete(0,END)
    elif(questionentrye.get()=='Mathew Braganza Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-7489574851')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Shriram Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-8957482154')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Primary Health Center'):
        texte.insert(END,'\n\nAlphius: Contact Number-9784547851')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Navjeevan Nursing Home'):
        texte.insert(END,'\n\nAlphius: Contact Number-8794578421')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Neural Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-8490480098')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Aster Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-9874584125')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='ESI Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-9784587415')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Blue Shield Medical Center'):
        texte.insert(END,'\n\nAlphius: Contact Number-9048789524')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Valpoi Manipal Center'):
        texte.insert(END,'\n\nAlphius: Contact Number-7848521408')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Sonu Kamat Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-9874851005')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Community Health Center'):
        texte.insert(END,'\n\nAlphius: Contact Number-9874581028')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Saud EMS Hosptal'):
        texte.insert(END,'\n\nAlphius: Contact Number-7418972587')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Healthway Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-8458745184')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Govt Medical Emergency Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-7845187957')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='New Vrundavan Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-9719938566')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Trinity Healthcare and research institute'):
        texte.insert(END,'\n\nAlphius: Contact Number-7017662797')
        questionentrye.delete(0,END)    
    elif(questionentrye.get()=='Shriram Hospital'):
        texte.insert(END,'\n\nAlphius: Contact Number-8476936766')
        questionentrye.delete(0,END)
    else:
        texte.insert(END, '\n\nAlphius: Please enter valid details')
        questionentrye.delete(0, END)
    def get_input():
        value=texte.get("1.0",END)
        file=open("Healthcare.txt","a")
        file.write(value+"\n")
        
        
    get_input()
   

def feedbackcommand():
    global f
    global namef
    global feedbackf
    global submitfeedback
    feedbackname=StringVar()
    feedbackfeedback=StringVar()
    f=Toplevel(window)
    f.title("Feedback")
    f.geometry("550x550")
    Label(f,text="Enter the details").pack()
    Label(f,text="").pack()
    Label(f,text="Name").pack()
    namef=Entry(f,textvariable=feedbackname)
    namef.pack()
    Label(f,text="").pack()
    Label(f,text="Feedback").pack()
    feedbackf=Entry(f,textvariable=feedbackfeedback)
    feedbackf.pack()
    Label(f,text="").pack()
    submitfeedback=Button(f,text="Submit",command=submitcommandf).pack()

def submitcommandf():
    
    nameff=namef.get()
    feedbackff=feedbackf.get()
    sqlformula1=("insert into feedback values(%s, %s)")
    responses=[(nameff,feedbackff)]
    mycursor.executemany(sqlformula1,responses)
    mydb.commit()
    namef.delete(0,END)
    feedbackf.delete(0,END)
    Label(f,text="").pack()
    Label(f,text="Feedback Submitted",fg="green").pack()
main_screen()
screen.mainloop()
