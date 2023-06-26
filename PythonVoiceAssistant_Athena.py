import pyttsx3 # Text-to-speech library
import datetime
import pyaudio # Audio I/O library
import speech_recognition as sr # Speech recognition library
import wikipedia # Wikipedia API wrapper
import webbrowser # Web browser controller
import os
import smtplib # Simple Mail Transfer Protocol library
import psutil # System monitoring library
import pyjokes # Jokes library
import pyautogui # GUI automation library
import random
import requests  # HTTP library
from pprint import pprint  # Pretty print library

#User's name
User = "Aryan"

# Initializing pyttsx3 text-to-speech engine
print("Athena is activated")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speech(audio):
    # Function to convert text to speech
    engine.say(audio)
    engine.runAndWait()

def time():
    # Function to get and speak the current time
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speech('The current time is')
    speech(Time)

def date():
    # Function to get and speak today's date
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speech('Today\'s date is')
    speech(date)
    speech(month)
    speech(year)
 
def greeting_authentication():
    # Function to prompt the user for password authentication
    speech("Please speak out your password clearly")

def fetch_user_command_authentication():
    # Function to listen to user's voice and recognize the command for password authentication
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-UK')
        print(f"User said- {query}\n")
    except Exception as e:
        print(e)
        speech("Please try again.")
        return "None"

    return query

def greeting():
   # Function to greet the user based on the time of day
   speech("Welcome back!")
   time()
   date()
   hour = datetime.datetime.now().hour
   if hour >= 0 and hour<12:
       speech("Good morning" + User)
   elif hour >=12 and hour<18:
        speech("Good afternoon" + User)
   elif hour >=18 and hour <24:
        speech("Good evening" + User)
   else:
        speech("Good night" + User)
   speech("Athena is at your beck and call. Tell me how I may assist you, please.")

def fetch_user_command():
    # Function to listen to user's voice and recognize the command
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-UK')
        print(f"User said- {query}\n")
    except Exception as e:
        print(e)
        speech("Please say that once again.")
        return "None"

    return query

def send_email(recipient, message):
    # Function to send an email
    server = smtplib.SMTP('smtp.gmail.com', 587) # The port is 587, which is the standard port used for secure email communication with SMTP.
    server.ehlo()
    server.starttls()
    server.login('personal_email@gmail.com', 'personal_email_password')
    server.sendmail("sender@gmail.com", recipient, message)
    server.close()

def get_cpu_usage():
    # Function to get and speak the current CPU usage
    usage = str(psutil.cpu_percent())
    speech('CPU is at ' + usage)

def get_battery_status():
    # Call the function to get and speak the battery information
    battery = psutil.sensors_battery()
    speech('Battery is at ' + str(battery.percent) + ' percent.')

def joke():
    # Function to tell a random joke
    speech(pyjokes.get_joke())

def take_screenshot():
    # Function to take a screenshot and save it
    system_screenshot = pyautogui.screenshot()
    system_screenshot.save(r'C:\Users\aryan\Pictures\Screenshots\Screenshot_Athena.png')

    #You are using a normal string as a path. Just put r before your normal string. It converts a normal string to a raw string

def my_identity():
    # Function to speak the user's identity
     speech('You are ' + User + ', a brilliant person. Have a nice day :)!')

def origin():
    # Function to speak about Athena's origin
    speech('I was created on a lazy Sunday at my developer' + User + 's univeristy as a Python project.')

def generic_response():
    # Function to give a generic response
    speech('I am fine, thank you. How may I assist you today?')

# The below check ensures that the code inside the if block is only executed when the script is run directly as the main module, 
# and not when it is imported as a module in another script.

if __name__ == "__main__":

    authentication_key = "password" 
    greeting_authentication()
    query_authentication = fetch_user_command_authentication().lower()

    if query_authentication ==  authentication_key:
        greeting()
        while True:
            query = fetch_user_command().lower()

            if 'time' in query:
                time()

            elif 'date' in query:
                date()

            elif 'who am i' in query:
                my_identity()

            elif 'where is your birth place' in query:
                origin()

            elif 'where were you born' in query:
                origin()

            elif 'how are you' in query:
                generic_response()

            elif 'how have you been' in query:
                generic_response()

            elif 'wikipedia' in query.lower():
                speech('Now searching Wikipedia...')
                query = query.replace("wikipedia", "") #Replacing occurrences of wikipedia with an empty string
                results = wikipedia.summary(query, sentences=5)
                speech('According to Wikipedia...')
                print(results)
                speech(results)

            elif 'send an email' in query.lower():
                try:
                    speech('What message should I send...')
                    message = fetch_user_command()
                    speech('Who is the recipient?')
                    receiver = input("Enter the receiver's email :")
                    recipient = receiver
                    send_email(recipient, message)
                    speech('Email sent Successfuly')

                except Exception as e:
                    print(e)
                    speech('Unable to send an email')

            elif 'search using google chrome' in query.lower():
                speech('What should I search?')
                search_term = fetch_user_command().lower()
                speech('Now searching...')
                url = 'google.com'
                chrome_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
                webbrowser.open('https://www.google.com/search?q='+search_term)

            elif 'search youtube' in query:
                speech('What should I search?')
                search_term = fetch_user_command().lower()
                speech("Opening YouTube now...")
                webbrowser.open('https://www.youtube.com/results?search_query='+search_term)

            elif 'weather details' in query: #openweather API
                speech('Which city\'s weather details are you looking for?')
                weather_update = fetch_user_command().lower()
                speech('Getting the current weather ppdate for '+ weather_update)
                url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={API KEY}&units=metric'.format(weather_update)

                resi = requests.get(url)
                data = resi.json()
                temp = data['main']['temp'],
                wind_speed = data['wind']['speed'],
                latitude = data['coord']['lat'],
                longitude = data['coord']['lon'],
                description = data['weather'][0]['description']

                speech('Temperature is at: {} degree celcius'.format(temp))
                speech('Wind speed is at: {} Micro Seconds'.format(wind_speed))
                speech('Latitude is : {}'.format(latitude))
                speech('Longitude is : {}'.format(longitude))
                speech('Clouds status is : {}'.format(description))

            elif 'open google' in query:
                speech('What should I search?')
                search_term = fetch_user_command().lower()
                speech('Now searching...')
                url = 'google.com'
                chrome_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
                webbrowser.open('https://www.google.com/search?q='+search_term)

            elif 'open github' in query:
                speech('Opening GitHub...')
                search_term = fetch_user_command().lower()
                speech('Your account is opening now!')
                url = 'github.com'
                webbrowser.open('https://www.github.com/kapooraryan')

            elif 'cpu' in query:
                get_cpu_usage()

            elif 'battery' in query:
                get_battery_status()

            elif 'joke' in query:
                joke()

            elif 'go offline' in query:
                speech('Athena is shutting down.')
                quit()

            elif 'quit' in query:
                speech('Athena is shutting down.')
                quit()

            elif 'shutdown' in query:
                speech('Athena is shutting down.')
                quit()

            elif 'open word' in query:
                speech('Opening MS Word....')
                MS_Word = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk'
                os.startfile(MS_Word)

            elif 'open downloads' in query:
                speech('Opening Downloads....')
                Downloads = r'C:\Users\aryan\Downloads'
                os.startfile(Downloads)

            elif 'open python' in query:
                speech('Opening PyCharm....')
                PyCharm = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2021.3.3.lnk'
                os.startfile(PyCharm)

            elif 'open java' in query:
                speech('Opening IntelliJ....')
                IntelliJ = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\IntelliJ IDEA Community Edition 2022.2.lnk'
                os.startfile(IntelliJ)

            elif 'open visual code' in query:
                speech('Opening Visual Studio Code....')
                VS_Code = r'C:\Users\aryan\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk'
                os.startfile(VS_Code)

            elif 'write a note' in query:
                speech("What should I write")
                notes = fetch_user_command()
                file = open('user_notes.txt','w')
                speech("Should I note down the date and time as well?")
                ans = fetch_user_command()
                if 'yes' in ans or 'sure' in ans:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    file.write(strTime)
                    file.write(':-')
                    file.write(notes)
                    speech("Done taking notes.")
                else:
                    file.write(notes)

            elif 'show notes' in query:
                speech('Showing you your notes')
                file = open('user_notes.txt','r')
                print(file.read())
                speech(file.read())

            elif 'screenshot' in query:
                take_screenshot()

            elif 'play music' in query:
                songs_dir = r'C:\Users\aryan\Downloads\Music'
                music = os.listdir(songs_dir)
                speech('What song should I play?')
                speech('Select a number...')
                answer = fetch_user_command().lower()
                while('number' not in answer and answer != 'random' and answer != 'you choose'):
                    speech('I could not understand you. Please repeat yourself once more.')
                    answer = fetch_user_command().lower()
                if 'number' in answer:
                    no = int(answer.replace('number',''))
                elif 'random' or 'you choose' in answer:
                    no  = random.randint(1,100)
                os.startfile(os.path.join(songs_dir,music[no]))

            elif 'who are you' in query:
                speech("I'm Athena, Aryan's intelligent voice assistant, and I was created to assist him with his daily activities and simplify his life.")
    else:
        speech("Please try again.")