import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from test_failure_llm.analyzer import CustomAIAnalyzer

def run_failing_test():
    print("--- 1. Setting up Selenium Test ---")
    # Setup Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # Run headless for smoother execution
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    screenshot_path = os.path.abspath("google_failure.png")
    source_path = os.path.abspath("google_source.html")
    error_msg = ""

    try:
        print("--- 2. Navigating to Google ---")
        driver.get("https://www.google.com")
        
        # Search for "Workforce" to populate the DOM with the text (so the LLM finds it in Source)
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Workforce automation")
        search_box.send_keys(Keys.RETURN)
        time.sleep(2) # Wait for results
        
        print("--- 3. Triggering Intentional Failure ---")
        # Intentional Failure: Trying to find a specific div with text 'Workforce' 
        # that likely doesn't exist exactly as requested or is hidden/structured differently.
        # This matches the pattern we trained the LLM on.
        target_xpath = "//div[text()='automatio']"
        driver.find_element(By.XPATH, target_xpath)

    except Exception as e:
        print(f"!!! Test Failed as expected !!!")
        error_msg = str(e).split("\n")[0] # Keep it brief for the demo
        
        # Capture Artifacts
        driver.save_screenshot(screenshot_path)
        with open(source_path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
            
        print(f"Captured Screenshot: {screenshot_path}")
        print(f"Captured Source: {source_path}")
        
    finally:
        driver.quit()

    if error_msg:
        print("\n--- 4. invoking Custom LLM for Analysis ---")
        
        # Initialize our custom tool
        analyzer = CustomAIAnalyzer()
        
        # Run analysis
        report = analyzer.generate_analysis(
            error_msg=error_msg,
            page_source=open(source_path, "r", encoding="utf-8").read(),
            screenshot_path=screenshot_path
        )
        
        print("\n" + "#"*60)
        print("      LLM ANALYSIS REPORT      ")
        print("#"*60)
        print(report)
        print("#"*60)
        
        # Save HTML Report
        analyzer.save_html_report(report, error_msg, screenshot_path, "google_failure_report.html")
    else:
        print("Test unexpectedly passed. Please adjust the failing locator.")

if __name__ == "__main__":
    run_failing_test()
