from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys
import time
import speech_recognition as sr
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pyttsx3

def main():
    # Create a recognizer
    recognizer = sr.Recognizer()

    # Adjust for ambient noise
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

    # Start listening
    while True:
        # Wait for the user to speak
        recognizer.pause_threshold = 0.5
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        # Try to recognize the speech
        try:
            # Get the recognized text
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            break
        except sr.UnknownValueError:
            print("I didn't understand what you said.")
            main()

        except sr.RequestError as e:
            print("Error:", e)
            main()
        # Check if the user has stopped speaking
        while True:
            audio = recognizer.listen(source)
            energy = recognizer.energy_threshold
            if energy < 400:
                print("You stopped speaking.")
                break


    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--headless")  # add this line to run Edge headless


    driver_path = "D:\\Pythonproj\\Tools\\msedgedriver.exe"

    driver = Edge(executable_path=driver_path, options=edge_options)
    driver.get("https://bard.google.com/")
    time.sleep(1)
    input_box = driver.find_element("xpath", '/html/body/chat-app/side-navigation/mat-sidenav-container/mat-sidenav-content/main/chat-window/div[1]/div[2]/input-area/div/mat-form-field/div[1]/div/div[2]/textarea')

    input_box.send_keys("In a max of 2 sentences,",text)
    input_box.send_keys(Keys.RETURN)
    # Create an instance of the WebDriverWait class
    wait = WebDriverWait(driver, 10)

    # Wait until the element is present
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/chat-app/side-navigation/mat-sidenav-container/mat-sidenav-content/main/chat-window/div[1]/div[1]/div/div/model-response/response-container/div/div[2]/div[2]/message-content')))

    # Find the element
    output_box = driver.find_element("xpath", '/html/body/chat-app/side-navigation/mat-sidenav-container/mat-sidenav-content/main/chat-window/div[1]/div[1]/div/div/model-response/response-container/div/div[2]/div[2]/message-content')

    generated_text = output_box.text
    print(generated_text)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', 'english_us')  # Use the first voice in the list
    engine.setProperty('rate', 150)
    engine.say(generated_text)
    engine.runAndWait()
    engine.stop()
    driver.quit()
    main()
main()