""" 1) I want my code to search through myanimelist.com based on input of character names

    2 ) I then want it to download the picture of said character from MAL

    3 ) I also want it to to assign a number value based on a strict criteria from MAL
    A) The working critrea is as follows:
      *) all characters start with a value of 1
        *) +1 for all characters that are considered by the website a main character
        *) +1 for all characters that have between 150-300 favorites*
      *) +2 for all characters that have between 300-700 favorites*
      *) +3 for all charcters that have between 700 or more favorites*
      *) +1 for any show in the top 100 of MAL*

    4) Outputs the picture along with the value of the characters on particular side of screen

    5) repeat till each player has a team between 3-5 characters

    6) Possibly have a button to declear a winner*

    7) Have a reset button to start the next game. """

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

site_url = 'https://myanimelist.net/search/all?type=character&keyword='
#single_search_url = 'https://myanimelist.net/character/152127/Kaho_Hinata'
save_path = 'C:\\Users\\Hawkesee\\Desktop\\Webbies\\DaImage.png'

# Ready the browser
if __name__ == '__main__':
    browser = webdriver.Chrome()

# Get a single search result page, the logic for which Future Joe shall pen
browser.get(site_url)

# Wait for 5 seconds
time.sleep(5)

## Click through the pop up, if it's there
elem_button = browser.find_element_by_tag_name('button')
elem_button.click()

# Wait for 5 seconds
time.sleep(5)

## Find the search box
elem = browser.find_element_by_id('topSearchText')
elem.send_keys('Kaho Hinata' + Keys.RETURN)

# Wait for 5 seconds
time.sleep(5)

# Find and download the character's picture (second img on the page)
page_images = browser.find_elements_by_tag_name('img')
prof_pic = page_images[1]

# Save the image
prof_pic.screenshot(save_path)

# Grab all other desired metadata from the page
# Name
# Rank
# Etc...

# Joe comment / uncomment the line below as you will...
browser.quit()
