#this project its a wikipedia scrapper that prints the title and 2 first paragraph

import requests
from bs4 import BeautifulSoup

# specify the Wikipedia page to scrape
wikipedia_url = input("Enter a Wikipedia url: ")

# send an HTTP request to the Wikipedia page and retrieve the HTML content
response = requests.get(wikipedia_url)
html = response.content

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# extract the title and first paragraph of the Wikipedia page
title = soup.find("h1", {"id": "firstHeading"}).text

# get all the paragraphs
paragraphs = soup.find_all("p")

# Get the second paragraph
first_paragraph = paragraphs[0].text
second_paragraph = paragraphs[1].text

# print the title and the 2 first paragraph
print("Title:", title)
print("First paragraph:", first_paragraph)
print("Second paragraph:", second_paragraph)

