# Ex 21: Write to a File

import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Get output file name
print("Let's get the New York Times headlines!")
print("The headlines will be saved to a .txt file.")
file_name = input("What would you like the file to be called? ")

# Make sure file has .txt extension
if file_name[-4:] != '.txt':
    file_name = file_name + '.txt'

# Set up request
url = 'https://www.nytimes.com'
response = requests.get(url)

# Parse HTML text with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Open output file
output_file = open(file_name, 'w', encoding='utf-8')

# Get page title
title = soup.find('title').string
title = title + '\n'

# Output page title & date/time to file
output_file.write(title)
date_string = datetime.now().strftime("%B %d, %y %H:%M %p") + '\n\n'
output_file.write(date_string)

# Get headlines & output to file
stories = soup.find_all(class_='story-wrapper')
headline_separator = "--------------\n"

for story in stories:
    headline = story.find('h3')
    if not headline:
        continue
    else:
        output_file.write(headline_separator)
        headline = headline.get_text() + '\n'
        output_file.write(headline)

output_file.close()
