
import requests
from bs4 import BeautifulSoup
import os

def download_images(url, folder_name):
    # Create a folder to save images
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Send a request to the URL with user-agent information
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags
    img_tags = soup.find_all('img')

    # Download each image
    for img in img_tags:
        img_url = img['src']
        if img_url.startswith('https://'):
            img_response = requests.get(img_url, headers=headers)
            img_name = os.path.join(folder_name, img_url.split('/')[-1])
            with open(img_name, 'wb') as f:
                f.write(img_response.content)
            print(f'Downloaded {img_name}')

# URL of the page to download images from
url = "https://site.douban.com/289672/widget/notes/192936282/note/616633488/"
# Folder to save images
folder_name = "downloaded_images"

# Download images
download_images(url, folder_name)
