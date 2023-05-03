#Infoscraper

import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.common.keys import Keys

global person_name
person_name = input('Enter the name of the person you want to search: ')

def askperplexity1():
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
    edge_options.add_argument("--disable-dev-shm-usage")
    #edge_options.add_argument("--headless")  


    driver_path = "C:\\Users\\kisha\\OneDrive\\Kishan All\\Documents\\msedgedriver.exe"

    driver = Edge(executable_path=driver_path, options=edge_options)
    driver.get("https://bard.google.com/")

def confirmbard1():
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
    edge_options.add_argument("--disable-dev-shm-usage")
    #edge_options.add_argument("--headless")  


    driver_path = "C:\\Users\\kisha\\OneDrive\\Kishan All\\Documents\\msedgedriver.exe"

    driver = Edge(executable_path=driver_path, options=edge_options)
    driver.get("https://bard.google.com/")

def twitter_followers_scraper():
    global twitter_followers
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
    edge_options.add_argument("--disable-dev-shm-usage")
    #edge_options.add_argument("--headless")  

    driver_path = "C:\\Users\\kisha\\OneDrive\\Kishan All\\Documents\\msedgedriver.exe"
    driver = Edge(executable_path=driver_path, options=edge_options)
    driver.get("https://twitter.com/search?q="+person_name+"&src=typed_query")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]')))
    driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[3]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]').click()
    time.sleep(1)
    twitter_person_name = driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span/span[1]')
    final_twitter_name = twitter_person_name.text
    time.sleep(1) 
    twitter_followers = driver.find_element("xpath", '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[5]/div[2]/a')
    final_twitter_followers = twitter_followers.text
    print(final_twitter_name, 'has', final_twitter_followers, 'on Twitter')
    driver.quit()

def instagram_followers_scraper():
    global twitter_followers
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
    edge_options.add_argument("--disable-dev-shm-usage")
    #edge_options.add_argument("--headless")  

    driver_path = "C:\\Users\\kisha\\OneDrive\\Kishan All\\Documents\\msedgedriver.exe"
    driver = Edge(executable_path=driver_path, options=edge_options)
    driver.get("https://www.instagram.com/explore/")
    wait = WebDriverWait(driver, 10)
    time.sleep(3)
    driver.find_element_by_xpath("//button[text()='Search']").click()
    input_box = driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input')
    input_box.send_keys(person_name)
    input_box.send_keys(Keys.RETURN)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/a/div/div/div/div[2]/div/div/span[1]/span/div/span')))
    driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/a/div/div/div/div[2]/div/div/span[1]/span/div/span').click()
    time.sleep(1)
    instagram_person_name = driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/div[1]/a/h2')
    final_instagram_name = instagram_person_name.text
    time.sleep(1) 
    instagram_followers = driver.find_element("xpath", '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
    final_instagram_followers = instagram_followers.text
    print(final_instagram_name, 'has', final_instagram_followers, 'on Instagram')
    driver.quit()

def youtube_followers_scraper():
    global youtube_followers
    edge_options = EdgeOptions()
    edge_options.use_chromium = True
    edge_options.add_argument("user-data-dir=C:\\Users\\kisha\\AppData\\Local\\Microsoft\\Edge\\ud1")
    edge_options.add_argument("--disable-dev-shm-usage")
    #edge_options.add_argument("--headless")  

    driver_path = "C:\\Users\\kisha\\OneDrive\\Kishan All\\Documents\\msedgedriver.exe"
    driver = Edge(executable_path=driver_path, options=edge_options)
    driver.get("https://www.youtube.com/results?search_query="+person_name)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[2]')))
    driver.find_element("xpath", '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[2]').click()
    time.sleep(3)
    youtube_person_name = driver.find_element("xpath", '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a')
    final_youtube_name = youtube_person_name.text
    time.sleep(1) 
    youtube_followers = driver.find_element("xpath", '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/yt-formatted-string')
    final_youtube_followers = youtube_followers.text
    print(final_youtube_name, 'has', final_youtube_followers, 'on youtube')
    driver.quit()


def main():
    #twitter_followers_scraper()
    #instagram_followers_scraper()
    youtube_followers_scraper()



if __name__ == "__main__":
    main()