import sounddevice as sd
import numpy as np
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
from playsound import playsound
import os

# Convert the sounddevice audio data to AudioData format
def record_audio(duration=5, samplerate=16000):
    print("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    return audio_data.flatten()

def takecommand():
    recognizer = sr.Recognizer()
    try:
        audio_data = record_audio()
        audio = sr.AudioData(audio_data.tobytes(), 16000, 2)
        print("Recognizing.....")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"The User said: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError as e:
        print(f"Sorry, there was an issue with the request: {e}")
        return "None"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "None"

def destination_language():
    print("Enter the language in which you want to convert: Ex. Hindi, English, etc.")
    to_lang = takecommand()
    while to_lang == "None":
        to_lang = takecommand()
    return to_lang.lower()

# List of supported languages (you can add more)
dic = {
    "hindi": "hi",
    "english": "en",
    "french": "fr",
    "spanish": "es",
    "german": "de",
}

# Capture initial voice command
query = takecommand()
while query == "None":
    query = takecommand()

# Get the target language
to_lang = destination_language()

# Validate the target language
while to_lang not in dic:
    print("Language in which you are trying to convert is currently not available, please input some other language")
    to_lang = destination_language()

# Get language code
to_lang = dic[to_lang]

# Initialize Translator
translator = GoogleTranslator()

# Translate the text
translated_text = translator.translate(query, target_lang=to_lang)
text = translated_text

# Convert translated text to speech
speak = gTTS(text=text, lang=to_lang, slow=False)
audio_file = "/tmp/captured_voice.mp3"  # Use a temporary file path for macOS
speak.save(audio_file)

# Play the translated speech
playsound(audio_file)
os.remove(audio_file)  # Clean up the file after playing

# Print the output
print(text)




dic=('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 
	'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az', 
'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian', 
	'bs', 'bulgarian', 'bg', 'catalan', 'ca', 
'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)', 
	'zh-cn', 'chinese (traditional)', 'zh-tw', 
'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish', 
	'da', 'dutch', 'nl', 'english', 'en', 'esperanto', 
'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi', 
	'french', 'fr', 'frisian', 'fy', 'galician', 'gl', 
'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati', 
	'gu', 'haitian creole', 'ht', 'hausa', 'ha', 
'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong', 
	'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo', 
'ig', 'indonesian', 'id', 'irish', 'ga', 'italian', 'it', 
	'japanese', 'ja', 'javanese', 'jw', 'kannada', 'kn', 
'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko', 'kurdish (kurmanji)', 
	'ku', 'kyrgyz', 'ky', 'lao', 'lo', 
'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish', 
	'lb', 'macedonian', 'mk', 'malagasy', 
'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori', 
	'mi', 'marathi', 'mr', 'mongolian', 'mn', 
'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no', 
	'odia', 'or', 'pashto', 'ps', 'persian', 
'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa', 
	'romanian', 'ro', 'russian', 'ru', 'samoan', 
'sm', 'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho', 
	'st', 'shona', 'sn', 'sindhi', 'sd', 'sinhala', 
'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so', 
	'spanish', 'es', 'sundanese', 'su', 
'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil', 
	'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr', 
'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek', 
	'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh', 
'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu')
