from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org')
# This finds shrubbery only within an event-widget
# Find the specific event widget and its menu
event_widget = driver.find_element(By.CLASS_NAME, "event-widget")
events_menu = event_widget.find_element(By.CSS_SELECTOR, "div.shrubbery ul.menu")

# Get all list items
event_items = events_menu.find_elements(By.TAG_NAME, "li")

# Get the events from this specific location
events = {}
for n, item in enumerate(event_items):
    time = item.find_element(By.TAG_NAME, value='time')
    link = item.find_element(By.TAG_NAME, value="a")
    date = time.text
    event_name = link.text
    events[n] = {
        'time': date,
        'name': event_name,
    }

print(events)
driver.quit()