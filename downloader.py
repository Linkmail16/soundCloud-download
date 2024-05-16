from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import subprocess

chrome_options = Options()
chrome_options.add_argument('--headless') 
chrome_options.add_argument('--disable-dev-shm-usage')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


url = "https://soundcloud.com/user-210816084-450778884/travis-scott-ft-swae-lee-chief-keef-nightcrawler-instrumental-slowed-reverb"
driver.get(url)


for request in driver.requests:
    if "m3u8" in request.url:
        print(f"URL encontrada: {request.url} (Solicitada por el script: {request.path} )")
        subprocess.run(['ffmpeg', '-i', request.url, 'MUSICA2.mp3', '-y'])

driver.quit()
