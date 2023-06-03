from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import time

# Function to retrieve Twitter data
def twitter(username, password, topic):
    browser = webdriver.Chrome()
    browser.get("https://twitter.com/i/flow/login")
    time.sleep(5)

    try:
        # Find the login input field and click on it
        login_input = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login_input.click()
    except:
        browser = webdriver.Chrome()
        browser.get("https://twitter.com/i/flow/login")
        time.sleep(4)
        login_input = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        login_input.click()

    time.sleep(2)
    login_input.send_keys(username)

    next_button = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
    next_button.click()
    time.sleep(2)

    try:
        password_input = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.click()
    except:
        error_label["text"] = "Error: Login field not found."
        browser.quit()
        return
    time.sleep(2)

    password_input.send_keys(password)
    time.sleep(2)

    login_button = browser.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
    login_button.click()
    time.sleep(8)

    search_area = browser.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
    search_area.click()
    time.sleep(2)
    search_area.send_keys(topic, Keys.ENTER)
    time.sleep(2)

    len_of_page = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while(match == False):
        last_count = len_of_page
        time.sleep(3)
        len_of_page = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if last_count == len_of_page:
            match = True
    time.sleep(5)

    tweets = []

    for element in browser.find_elements(By.XPATH, '//div[@data-testid="tweetText"]'):
        print("********************************************************************")
        print(element.text)
        tweets.append(element.text)

        tweet_count = 1
        textFile = str(topic)+".txt"
    with open(textFile, "w", encoding="UTF-8") as file:
        for tweet in tweets:
            file.write(str(tweet_count) + ".\n" + tweet + ".\n")
            file.write("********************************************************************\n")
            tweet_count += 1

    browser.back()
    
    time.sleep(5)
    browser.close()

# Function to get user credentials from input fields
def get_credentials():
    username = username_entry.get()
    password = password_entry.get()
    # Here, you can use the username and password as you desire
    print("Username:", username)
    print("Password:", password)

window = tk.Tk()
window.title("Twitter Data Extraction Program")
window.geometry("400x200")
window.resizable(width=False, height=False)

background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

username_label = tk.Label(window, text="Username:", bg="#1B9DF0")
username_label.pack()

username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:", bg="#1B9DF0")
password_label.pack()

password_entry = tk.Entry(window, show="*")
password_entry.pack()

topic_frame = tk.Frame(window, bg="#1B9DF0")
topic_frame.pack()

topic_label = tk.Label(topic_frame, text="Topic:", bg="#1B9DF0")
topic_label.pack()

topic_entry = tk.Entry(topic_frame)
topic_entry.pack()

error_label = tk.Label(window, fg="red", bg="#1B9DF0")
error_label.pack()

start_button = tk.Button(window, text="Extract Data", command=lambda: twitter(username_entry.get(), password_entry.get(), topic_entry.get()))
start_button.pack()

window.mainloop()
