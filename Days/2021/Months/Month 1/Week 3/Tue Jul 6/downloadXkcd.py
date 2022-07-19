#! python3
# Start
# downloadXkcd.py - Downloads every single XKCD comic.
# Modules
import requests, bs4, os


url = 'http://xkcd.com'                 # Starting URL
os.makedirs('xkcd', exist_ok=True)      # Store comics in ./xkcd


while not url.endswith('#'):
    # Download the page.
    try:
        print(f'Downloading page {url}...')
        res = requests.get(url)
        res.raise_for_status()

    except Exception as exc:
        print('The site does not exists!\n[Error 404]')

    else:
        soup = bs4.BeautifulSoup(res.text)
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
        
        # Download the image.
        
        print(f'Downloading image {comicUrl}...')
        try:
            res = requests.get(comicUrl)
            res.raise_for_status()
        
        except Exception as exc:
            print('Site does not exists!\n[Error 404]')
        
        else:
            # Save the image to ./xkcd.
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
                imageFile.close()

            # Get the Prev button's url.
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prevLink.get('href')

print('done')
# End