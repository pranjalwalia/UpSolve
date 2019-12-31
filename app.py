import sys
import os
from selenium import webdriver
from time import sleep
import time
import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


#for chrome
driver = webdriver.Chrome()
#chrome end

#for firefox
# driver = webdriver.Firefox()
#firefox end

'''
while(1):
    print('select your browser: ')
    print('1. Chrome')
    print('2. Firefox')

    x = int(input())

    if(x==1):
        driver = webdriver.Chrome()
        break

    elif(x==2):
        driver = webdriver.Firefox()
        break

    else:
        print('Invalid Input, try again...')
'''

driver.get("https://www.hackerrank.com/login")
window_before = driver.window_handles[0]



Username = str(input('Enter Username: '))
Password = getpass.getpass('Enter the Password: ')

user = driver.find_element_by_xpath('//*[@id="input-1"]')
user.send_keys(Username)
passw = driver.find_element_by_xpath('//*[@id="input-2"]')
passw.send_keys(Password)

time.sleep(1)

buttons = driver.find_elements_by_tag_name('button')
for button in buttons:
    if(button.text == 'Log In'):
        button.click()

time.sleep(3)

check_login = driver.find_elements_by_xpath("//*[contains(text(), 'Invalid login or password. Please try again.')]")

if(check_login):
    print('Sorry,Invalid login!, Launch Again')
    time.sleep(2)
    driver.quit()
    sys.exit()



url = 'https://www.hackerrank.com/domains/algorithms?badge_type=problem-solving'
driver.execute_script("window.open('%s')" % url)

#get the window opened in the new tab
window_after = driver.window_handles[1]

prob_name = str(input("Enter the problem name: "))
    #attr = data[str(prob_name)]


#switch on to new child window
driver.switch_to.window(window_after)

body = driver.find_element_by_css_selector('body')

# try:
#    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-attr1='%s']" % attr))).click()
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, '%s' % prob_name))).click()
# except:
#     driver.quit()
#     sys.exit("Sorry, can't seem to find the solution!")

i=0
print('Searching...')

try:
    while(1):    
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            element = driver.find_element_by_partial_link_text(prob_name)
            if(element):
                element.click()
                break
        except:
            pass
        i+=1

        time.sleep(2)

        if(i>=50):
            driver.quit()
            sys.exit("Sorry, can't seem to find the solution!")
        
    time.sleep(3)

    print('Done!')

except:
    print('..Search terminated..')
    sys.exit('Exiting..')


#get the window handle that has opened in the new tab
board = driver.window_handles[1]
#switch on to new child window
driver.switch_to.window(board)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-attr1='topscorers']"))).click()

time.sleep(2)
#but = driver.find_element_by_xpath("//span[@class = 'Select-arrow-zone']")
but = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class = 'Select-arrow-zone']")))
but.click()

time.sleep(3)

but1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label = '100']")))
print('Listing the Top 100 Submissions')
but1.click()

time.sleep(3)

lang = ''       #cannot be empty

'''
Available Options for lang are, just copy and paste any one according to your language preference:

cpp 
python3
python
java
java8
csharp
javascript
ruby
'''

try:
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-attr2='%s']" % lang))).click()

    except:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-attr2='cpp']"))).click()


except:
    conf = driver.find_elements_by_tag_name('button')
    for button in conf:
        if(button.text == 'Reveal solutions'):
            button.click()

    time.sleep(2)
    
    conf2 = driver.find_elements_by_tag_name('button')
    for button in conf2:
        if(button.text == 'Yes'):
            button.click()
            try:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-attr2='%s']" % lang))).click()
            except:
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-attr2='cpp']"))).click()

finally:
    time.sleep(2)
    code = driver.window_handles[2]
    driver.switch_to.window(code)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/pre")))
    element = driver.find_element_by_css_selector('body')
    time.sleep(3)
    element.send_keys(Keys.CONTROL + 'a')

    filename = "code/%s_%s.txt" % (prob_name , lang)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(element.text)
        f.close()


    sys.exit("Borat: Great Success!!")


