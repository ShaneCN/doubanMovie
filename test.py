from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options=Options()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)

browser.get('https://movie.douban.com/subject/1292052/')

score = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong').text
/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong
print(score)
