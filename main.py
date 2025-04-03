import speech_recognition as sr
import os
import win32com.client
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import openai
import datetime


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(f" {text}")

def take_command():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query
    except Exception as e:
        print("Error")

if __name__ == '__main__':
    say('hii javaris')

    try:
        while True:
            query = take_command()
            # say(text)
            sites = [['youtube','https://www.youtube.com'],[ 'google','https://www.google.co.in/'],[ 'facebook','https://www.facebook.com'],['instagram','https://www.instagram.com'],['whatsapp web','https://web.whatsapp.com/']]
            for site in sites:
                if f'open {site[0]}'.lower() in query.lower():
                    if site[0] == 'instagram':
                        say(f'opening {site[0]}')
                        # webbrowser.open(site[1])
                        driver_path = "C://Program Files (x86)//Microsoft//Edge//Application//msedge.exe"
                        driver = webdriver.Edge(driver_path)
                        driver = webdriver.Edge()
                        driver.get("https://www.instagram.com/accounts/login/")
                        print("Browser opened")


                        # Find the username and password input fields
                        time.sleep(5)
                        username_input = driver.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[1]/div/label/input")
                        password_input = driver.find_element(By.NAME, "password")

                        username_input.send_keys("YOUR username")
                        password_input.send_keys("YOUR PASSWORD")

                        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
                        login_button.click()

                        # Wait for the login process to complete
                        time.sleep(10)
                        save_inp = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div/div")
                        save_inp.click()



                    else :
                        say(f'opening {site[0]}')
                        webbrowser.open(site[1])

            if 'open time' in query.lower():
                time = datetime.datetime.now().strftime('%I:%M %p')
                say(f'The time is {time}')

    except Exception as e:
        print("Error occured")
        print(e)
