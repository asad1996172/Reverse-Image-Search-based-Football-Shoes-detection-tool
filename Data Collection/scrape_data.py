from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.chrome.options import Options
import os
import urllib.request

# set some parameters for chrome driver
chrome_options = Options()
chrome_options.add_argument("--headless")

# initialize chrome driver instance
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.footballbootsdb.com/boot/")

# click on "Load More" button to load images at once
for i in range(5):
    print("Clicking time : ", i+1)
    driver.find_element_by_css_selector('.button-subtle.ajax-loader').click()
    time.sleep(3)

# collect data and store in a pandas dataframe
print("Collecting Data Now...")
shoe_data = pd.DataFrame(columns=["Name", "Image URL", "Image Name"])
if not os.path.exists("Football Shoes Images"):
    os.makedirs("Football Shoes Images")

parent_element = driver.find_element_by_class_name("player-list")
shoes = parent_element.find_elements_by_tag_name("a")

counter = 0
for shoe in shoes:
    image = shoe.find_element_by_tag_name("img")
    img_src = image.get_attribute("src")

    shoe_name = shoe.find_element_by_class_name("player-name")
    shoe_name = shoe.text

    urllib.request.urlretrieve(img_src, "Football Shoes Images/" + str(counter+1) + ".jpg")

    shoe_data = shoe_data.append({
         "Name": shoe_name,
         "Image URL":  img_src,
         "Image Name": "Football Shoes Images/" + str(counter+1) + ".jpg"
          }, ignore_index=True)
    print("Shoes Collected : ", counter+1)
    counter+=1

shoe_data.to_csv("raw_data.csv", index=False)