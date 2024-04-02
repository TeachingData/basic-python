# Sample for Networking class: will increase complexity and look at other sites incrementantly
from selenium import webdriver
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # Start webdriver to automate Edge
    driver = webdriver.Edge() #or Chrome(), Firefox(), ... don't use Safari
    driver.get("https://millikin.edu/academics/performance-learning")

    # Walk through all elements and keep any (list) that are an "Article" tag
    for element in driver.find_elements(By.TAG_NAME, "article"):
        # element has text, 
        print(element.text)

    driver.close()
