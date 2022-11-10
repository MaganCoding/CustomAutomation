from bs4 import BeautifulSoup
import requests
import lxml
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


CHROME_DRIVER_PATH = "C:\\Users\\magan\\Downloads\\chromedriver_win32\\chromedriver.exe"
EMAIL = 'maganmaxamad@gmail.com'
PASSWORD = '\/ENOMSTRIK3'


headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US;q=0.5"
}

response = requests.get('https://screenrant.com/november-2022-movies-theaters-release-dates/')

screenrant_page = response.text
soup = BeautifulSoup(screenrant_page, "html.parser")

movies = []


movie_1 = soup.find(id='next-exit-ndash-november-4').text
movies.append(movie_1)
movie_2 = soup.find(id='bardo-ndash-november-4').text
movies.append(movie_2)
movie_3 = soup.find(id='black-panther-wakanda-forever-ndash-november-11').text
movies.append(movie_3)
movie_4 = soup.find(id='she-said-ndash-november-18').text
movies.append(movie_4)
movie_5 = soup.find(id='the-menu-ndash-november-18').text
movies.append(movie_5)









driver = webdriver.Chrome(CHROME_DRIVER_PATH)
count = 0
num = 1
all_links = []
for _ in range(5):
    name = movies[count]
    driver.get(f'https://www.youtube.com/results?search_query={name} trailer')
    time.sleep(5)
    video = driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string')
    video.click()
    time.sleep(5)

    video_url = driver.current_url
    all_links.append(video_url)
    time.sleep(2)
    count += 1


driver.get('https://docs.google.com/forms/d/e/1FAIpQLSfKgl4PcgNYXMt8EC4DzJHffQOwtanze6BltAe-TrsabbuBlg/viewform?vc=0&c=0&w=1&flr=0')
for _ in range(5):
    time.sleep(2)

    field = driver.find_element(By.XPATH, f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{num}]/div/div/div[2]/div/div[1]/div/div[1]/input')
    field.send_keys(f'Movie Name & Date: {movies[num - 1]}. Link: {all_links[num - 1]}')
    time.sleep(1)

    time.sleep(1)
    num += 1
submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit_button.click()
time.sleep(120)



















#New way
#driver.find_element(By.XPATH,
#driver.find_element(By.CSS_SELECTOR,