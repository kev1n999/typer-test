from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from config.constants import URL 

driver = webdriver.Chrome()

def open(url: str) -> None:
  driver.get(url)
  assert "typing" in driver.title.lower(), "An error ocurred to open!"

if __name__ == "__main__":
  open(URL)