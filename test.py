from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.set_headless(headless=True)
driver = webdriver.Firefox(firefox_options=options, executable_path='/home/ubuntu/Line-scrap-aws/geckodriver')
driver.get("http://www.imdb.com/title/tt3783958/")
elem = driver.find_element_by_css_selector('strong span')
print("Rating: {}".format(elem.text))
elem = driver.find_elements_by_css_selector('.subtext .itemprop')
for e in elem:
  print("- {}".format(e.text))
driver.quit()