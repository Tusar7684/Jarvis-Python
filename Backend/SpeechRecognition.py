from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# Path to your Voice.html file (replace with the actual path)
link = r'E:\OneDrive\Desktop\Jarvis Python\Backend\Voice.html'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--use-fake-device-for-media-stream")  # Enable fake device
chrome_options.add_argument("--use-fake-ui-for-media-stream")    # Enable fake UI

# Proper instantiation of Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(link)
sleep(2)  # Wait for the page to load

def speech_recognition():
    try:
        start_button = driver.find_element(By.ID, "start")
        start_button.click()
        print("Listening...")

        while True:
            output_element = driver.find_element(By.ID, "output")
            text = output_element.text
            if text:
                driver.find_element(By.ID, "end").click()
                return text
            else:
                sleep(0.222)  # Adjust polling interval as needed
    except Exception as e:
        print(f"Error during speech recognition: {e}")
        # Handle potential errors gracefully (e.g., retry, log to file)

while True:
    recognized_text = speech_recognition()
    if recognized_text:
        print(recognized_text)
        # Process or handle the recognized text here
    else:
        print("No speech detected")
