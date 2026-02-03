from selenium import webdriver
from config.constants import URL 
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_routes = {
  1:"/1-minute",
  2: "/3-minute",
  3: "/5-minute",
  4: "/1-page",
  5: "/2-page",
  6: "/3-page",
}

def open(driver: webdriver.Chrome, url: str) -> None:
  driver.get(url)
  assert "typing" in driver.title.lower(), "An error ocurred to open!"

def characters_parser(driver: webdriver.Chrome) -> List[str]:
  try:
    content_container = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CLASS_NAME, "green-card")) 
    )

    content = content_container.text
    print(content)
  except:
    raise Exception("Content container not found!")

def get_test_route() -> str:
  print("[1] => 1 minute\n[2] 3 minutes\n[3] 5 minutes")
  print("[4] => 1 page\n[5] => 2 pages\n[6] => 3 pages") 

  option = int(input("\n[choice a option] _: "))

  return test_routes.get(option)

if __name__ == "__main__":
  test_route = get_test_route()
  driver = webdriver.Chrome()
  open(driver, URL + test_route)
  characters_parser(driver)