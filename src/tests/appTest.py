from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the WebDriver (make sure the WebDriver executable is in your PATH)
driver = webdriver.Chrome()

# Open the web page where your AI is hosted
driver.get("http://localhost:8000")  # Update the URL as needed

try:
    # Find the input field for the prompt
    prompt_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "prompt"))
    )

    # Enter the prompt "who is LeBron James" into the input field
    prompt_input.send_keys("who is LeBron James")
    prompt_input.send_keys(Keys.RETURN)

    # Wait for the response to appear
    response_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "response"))
    )

    # Get the text of the response
    response_text = response_element.text
    print("Response:", response_text)

    # Optionally, you can add assertions to verify the response
    assert response_text.strip() != "", "Response should not be empty"

finally:
    # Close the browser window
    driver.quit()
