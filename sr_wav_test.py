import speech_recognition as sr
import glob 

# Record Audio
r = sr.Recognizer()

files = glob.glob('Command_Data/*/*.wav')

# print(files)

for filename in files:
    sample_file = filename 
    print(filename)
    
    with sr.WavFile(sample_file) as source:              
        audio = r.record(source)  
    
    # Speech recognition using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print()
    print()
