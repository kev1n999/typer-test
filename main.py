import time
import pyautogui
from selenium import webdriver
from config.constants import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
  assert "minute" in url or "page" in url, "Invalid page!"
  assert "typing" in driver.title.lower(), "An error ocurred to open!"

def fetch_words(driver: webdriver.Chrome) -> None:
  class_name = "screenBasic-word"
  current_word = ""

  try:
    content_container = WebDriverWait(driver, 10).until(
      EC.presence_of_all_elements_located((By.CLASS_NAME, class_name))
    )
  except TimeoutException as timeout_err:
    raise TimeoutException(f"content_container not found!\n{timeout_err}")

  for word in content_container:
    current_word += word.text

  for _ in range(len(current_word)):
    try:
      active = WebDriverWait(driver, 10).until(lambda d: d.find_element(By.CSS_SELECTOR, ".letter.is-active"))

      letter = active.text
      if letter.isspace():
        pyautogui.press(["space"])
        time.sleep(1)
        # A bug after that (The first letter of the next word doesn't works)

      pyautogui.press(letter)
      print(letter, end=" ")
    except Exception as err:
      print(f"An error ocurred to try typing: {err}")

def get_test_route() -> str:
  print("[1] => 1 minute\n[2] 3 minutes\n[3] 5 minutes")
  print("[4] => 1 page\n[5] => 2 pages\n[6] => 3 pages")

  option = int(input("\n[choice a option] _: "))

  return test_routes.get(option)

def start_test(driver: webdriver.Chrome) -> None:
  try:
    continue_button = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Continue']"))
    )

    if EC.element_to_be_clickable(continue_button):
      continue_button.click()
      print("You're in the test!")
  except:
    raise Exception("An error ocurred to start the test!")

if __name__ == "__main__":
  test_route = get_test_route()
  driver = webdriver.Chrome()
  open(driver, URL + test_route)
  start_test(driver)
  print(fetch_words(driver))
