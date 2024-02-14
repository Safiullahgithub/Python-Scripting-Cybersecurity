
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin


def download_images(url, folder_path):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all image tags in the HTML
    img_tags = soup.find_all('img')

    # Create a folder to save the images
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Download and save each image locally
    for img_tag in img_tags:
        img_url = urljoin(url, img_tag['src'])
        img_name = img_url.split('/')[-1]
        img_path = os.path.join(folder_path, img_name)
        with open(img_path, 'wb') as img_file:
            img_file.write(requests.get(img_url).content)
        print(f"Downloaded: {img_name}")


# Ask the user for the URL and folder path
url = input("Enter the URL of the web page: ")
folder_path = input("Enter the folder path to save the images: ")

download_images(url, folder_path)
