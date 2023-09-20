import requests
import pandas as pd
import os
import kaggle
import json
import yaml
from bs4 import BeautifulSoup

# using the Kaggle API to generate candidate downloads
# authentication is handled automatically by the kaggle package
# you will need to go to the kaggle website and create an API token
# see https://github.com/Kaggle/kaggle-api under 'API Credentials'

# fetch list of datasets - default sort is 'hottest' so this will fetch datasets of current interest/activity
dataset_list = kaggle.api.dataset_list()
for dataset in dataset_list[0:3]:
    # print(dataset)
    # print(vars(dataset))
    print("Downloading from " + dataset.ref)
    download_path = "datasets/kaggle" + dataset.ref
    kaggle.api.dataset_download_files(dataset.ref, path=download_path,unzip=True)
    

# list using search
# need try/except block because will error if no records returned
datasets_searched = kaggle.api.datasets_list(search="air quality")

# Define the URL of the webpage you want to scrape
url = "https://example.com/datasets"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using Beautiful Soup
soup = BeautifulSoup(response.text, 'html.parser')

# Find links to datasets on the page
dataset_links = []
for link in soup.find_all('a'):
    if 'dataset' in link.get('href'):
        dataset_links.append(link.get('href'))

# Print the dataset links
for link in dataset_links:
    print(link)

