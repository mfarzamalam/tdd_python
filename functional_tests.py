from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

    # alex has heard about the new cool to-do app
    # he decided to visits its homepage by clicking on the url
browser.get('http://localhost:8000')


    # he notice the website title has a word To-Do 
assert 'To-Do' in browser.title, "Title is: "+"'"+ browser.title +"'"


    # when his work is complete he close the browser
browser.quit()