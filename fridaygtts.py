import pyttsx3
import datetime
import subprocess
import webbrowser
import requests
import psutil
import wikipediaapi
import pywhatkit
import pyjokes
import os
import pyautogui
import speech_recognition as sr
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet user
def greet_user():
    speak("Hello! How can I assist you today?")

# Function to tell current time and date
def tell_time_date():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    print(f"Current time: {current_time}")
    print(f"Current date: {current_date}")
    speak(f"Current time is {current_time} and today's date is {current_date}")

# Function to launch applications/software
def launch_application(app_name):
    try:
        subprocess.Popen(app_name)
        speak(f"{app_name} launched successfully!")
    except FileNotFoundError:
        speak(f"Sorry, I couldn't find {app_name} on your system.")

# Function to open any website
def open_website(domain):
    url = f"http://{domain}"  # Prepend http:// to the domain
    webbrowser.open(url)
    speak(f"Browsing to {domain} now.")


# Function to get weather using Tomorrow.io API
def get_weather(city_name):
    TOMORROW_IO_API_KEY = 'YOUR_TOMORROW_IO_API_KEY'  # Replace with your actual Tomorrow.io API key
    geolocator = Nominatim(user_agent="geoapiExercises")
    
    try:
        location = geolocator.geocode(city_name)
        
        if location:
            latitude = location.latitude
            longitude = location.longitude
            print(f"Geolocation for {city_name}: Latitude {latitude}, Longitude {longitude}")
            
            weather_url = f"https://api.tomorrow.io/v4/timelines?location={latitude},{longitude}&fields=temperature&units=metric&apikey={TOMORROW_IO_API_KEY}"
            response = requests.get(weather_url)
            print(f"Weather API Response Status Code: {response.status_code}")
            print(f"Weather API Response: {response.text}")  # Print full response text for debugging
            
            if response.status_code == 200:
                data = response.json()
                if "data" in data and "timelines" in data["data"] and len(data["data"]["timelines"]) > 0:
                    temperature = data["data"]["timelines"][0]["intervals"][0]["values"]["temperature"]
                    
                    print(f"Temperature: {temperature}°C")
                    speak(f"The current temperature in {city_name} is {temperature} degrees Celsius.")
                else:
                    speak("Weather data not found in response.")
            else:
                speak("Error with weather API response. Please check the API status.")
        else:
            speak(f"City '{city_name}' not found. Please check the city name.")
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        speak("There was an error fetching the weather data.")

# Function to get location and distance between places
def get_location_distance(place):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(place)
    user_location = geolocator.geocode("Your_City")  # Replace with your city or current location

    if location and user_location:
        place_coords = (location.latitude, location.longitude)
        user_coords = (user_location.latitude, user_location.longitude)

        distance = geodesic(user_coords, place_coords).kilometers
        print(f"The distance between {user_location} and {place} is {distance} km.")
        speak(f"The distance between your location and {place} is approximately {distance:.2f} kilometers.")
    else:
        speak("I couldn't determine the location.")

# Function to get current system status
def get_system_status():
    battery = psutil.sensors_battery()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()

    print(f"Battery: {battery.percent}%")
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory.percent}%")
    speak(f"Your system's battery is at {battery.percent} percent, CPU usage is at {cpu_usage} percent, and memory usage is at {memory.percent} percent.")

# Function to tell about any person (via Wikipedia)
def tell_about_person(person_name):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page = wiki_wiki.page(person_name)
    if page.exists():
        print(f"Title: {page.title}")
        print(f"Summary: {page.summary[:500]}...")  # Limit summary to 500 characters
        speak(f"Here is a summary of {person_name}: {page.summary[:500]}...")
    else:
        speak("Person not found.")

# Function to search anything on Google
def google_search(query):
    pywhatkit.search(query)
    speak(f"Searching {query} on Google...")

# Function to play any song on YouTube
def play_song_on_youtube(song_name):
    pywhatkit.playonyt(song_name)
    speak(f"Playing {song_name} on YouTube...")

# Function to tell a random joke
def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

# Function to get your IP address
def get_ip_address():
    ip = requests.get('https://api.ipify.org').text
    print(f"Your IP address is: {ip}")
    speak(f"Your IP address is {ip}")

# Function to take a screenshot and save it with a custom filename
def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    speak(f"Screenshot saved as {filename}")

# Function to hide all files in a folder and make them visible again
def hide_files(folder_path):
    os.system(f'attrib +h {folder_path}\\* /s /d')
    speak("Files hidden.")

def unhide_files(folder_path):
    os.system(f'attrib -h {folder_path}\\* /s /d')
    speak("Files are visible again.")

# Function to listen for commands with timeout
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5)  # 5-second timeout for listening
            print("Recognizing...")
            command = recognizer.recognize_google(audio, language='en-in')
            print(f"You said: {command}\n")
        except sr.WaitTimeoutError:
            print("Listening timed out. Please try again.")
            return "None"
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Please try again.")
            return "None"
        except sr.RequestError:
            print("Sorry, my speech service is down. Please try again later.")
            return "None"

    return command.lower()

# Function to extract city name from command
def extract_city_name(command, keyword):
    if keyword in command:
        parts = command.split(keyword)
        if len(parts) > 1:
            city_name = parts[1].strip()
            return city_name
    return None

# Function to perform basic arithmetic calculations
def calculate(expression):
    # Replace words with symbols for basic arithmetic
    expression = expression.replace("plus", "+")
    expression = expression.replace("minus", "-")
    expression = expression.replace("times", "*")
    expression = expression.replace("divided by", "/")
    
    try:
        # Evaluate the basic arithmetic expression
        result = eval(expression, {"__builtins__": None})
        speak(f"The result of {expression} is {result}.")
    except Exception as e:
        print(f"Error evaluating expression: {e}")
        speak("There was an error in calculating the result. Please check the expression and try again.")

# Function to fetch Indian news headlines
def get_indian_news():
    NEWS_API_KEY = '492c7552c2ad42bb86b1d6d95af192e6'  # Replace with your NewsAPI.org key
    news_url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    
    try:
        response = requests.get(news_url)
        print(f"News API Response Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            articles = data["articles"]
            
            if articles:
                speak("Here are the top headlines from India:")
                for i, article in enumerate(articles[:5], 1):  # Limit to top 5 headlines
                    title = article["title"]
                    print(f"Headline {i}: {title}")
                    speak(f"Headline {i}: {title}")
            else:
                speak("No news articles found.")
        else:
            speak("Error fetching news. Please check the API status.")
    except Exception as e:
        print(f"Error fetching news: {e}")
        speak("There was an error fetching the news.")


# Main function to handle commands



def main():
    greet_user()
    
    while True:
        command = listen_command()

        if "friday" in command:
            if "browse" in command:
                domain = command.replace("friday", "").replace("browse", "").strip()
                open_website(domain)
            elif "website" in command:
                url = command.replace("friday", "").replace("open", "").replace("website", "").strip()
                open_website(url)
            elif "weather" in command:
                city_name = extract_city_name(command, "in")
                if city_name:
                    get_weather(city_name)
                else:
                    speak("Please specify the city for weather information.")
            elif "time" in command or "date" in command:
                tell_time_date()
            elif "launch" in command or "open" in command:
                app_name = command.replace("friday", "").replace("launch", "").replace("open", "").strip()
                launch_application(app_name)
            elif "distance" in command:
                place = command.replace("friday", "").replace("distance to", "").strip()
                get_location_distance(place)
            elif "system status" in command:
                get_system_status()
            elif "about" in command:
                person_name = command.replace("friday", "").replace("about", "").strip()
                tell_about_person(person_name)
            elif "search" in command:
                query = command.replace("friday", "").replace("search", "").strip()
                google_search(query)
            elif "play song" in command:
                song_name = command.replace("friday", "").replace("play song", "").strip()
                play_song_on_youtube(song_name)
            elif "joke" in command:
                tell_joke()
            elif "ip address" in command:
                get_ip_address()
            elif "screenshot" in command:
                filename = command.replace("friday", "").replace("screenshot", "").strip()
                take_screenshot(filename)
            elif "hide files" in command:
                folder_path = command.replace("friday", "").replace("hide files", "").strip()
                hide_files(folder_path)
            elif "unhide files" in command:
                folder_path = command.replace("friday", "").replace("unhide files", "").strip()
                unhide_files(folder_path)
            elif "calculate" in command:
                expression = command.replace("friday", "").replace("calculate", "").strip()
                calculate(expression)
            elif "news" in command:
                get_indian_news()
            elif "stop" in command or "exit" in command:
                speak("Goodbye!")
                break
            else:
                speak("I'm sorry, I didn't understand that command.")
        elif "jarvis stop" in command:
            speak("Stopping the system. Goodbye!")
            break

if __name__ == "__main__":
    main()

