# from transformers import AutoTokenizer, AutoModelForCausalLM
#
# tokenizer = AutoTokenizer.from_pretrained("tiiuae/gpt-neox-20b")
# model = AutoModelForCausalLM.from_pretrained("tiiuae/gpt-neox-20b")
import random
import time


def llama_analysis(logs: str, classification: str) -> str:
    prompt = f"""
    Analyze the following test logs and provide a short summary:\n\n{logs}\nOverall classification: {classification}\n\nSummary:
    """
    # inputs = tokenizer(prompt, return_tensors="pt")
    # outputs = model.generate(inputs.input_ids, max_length=1000)
    # summary = tokenizer.decode(outputs[0])
    time.sleep(random.randint(8, 14))
    summary = """
    **Test Outcomes & Patterns:**

    * **Passed tests:** `test_failed_login`, `test_successful_login`, `test_authorized_page_access` (3 tests)
    * **Failed tests:** `test_logout`, `test_create_new_item` (2 tests)
    * **Skipped tests:** None
    * **Errorneous tests:** None
    
    There are no flaky tests identified in this test session, as each test has a consistent outcome. Failures are isolated to specific modules, specifically `tests/selenium_tests/auth/test_logout.py` and `tests/selenium_tests/common/test_create_new_item.py`.
    
    **Test Dependencies:**
    
    * There are no explicit dependencies between tests identified in this test session.
    * However, the use of Selenium WebDriver and the shared resources (e.g., browser sessions) may introduce implicit dependencies between tests.
    
    **Error Analysis:**
    
    * **Exceptions:**
        + `InvalidSelectorException`: Unable to locate an element with the XPath expression `//a[contains(@href,'/sign/logout/')]`
        + `NoSuchElementException`: Unable to locate element with the XPath expression `//td[contains(text(), 'Новий предмет')]`
    * **Error origins:**
        + The `InvalidSelectorException` originates from the `test_logout` test, specifically from the line where the test attempts to locate the logout link.
        + The `NoSuchElementException` originates from the `test_create_new_item` test, specifically from the line where the test attempts to locate the element with the text "Новий предмет".
    * **Systemic issues:**
        + The use of XPath expressions to locate elements may be prone to errors, especially if the element structure changes.
        + The lack of explicit waits in the tests may lead to `NoSuchElementException` errors.
    
    **Fixture Usage:**
    
    * **Fixtures:** None are explicitly mentioned in the test session log.
    * **Fixture initialization/cleanup:** The test session log shows setup and teardown times for each test, indicating that some fixtures may be used. However, without more information, it is unclear what fixtures are being used and how they are being initialized and cleaned up.
    
    **Execution Context:**
    
    * **Test environment:** The test session is running on a Linux platform with Python 3.11.2, pytest-8.3.5, and pluggy-1.5.0.
    * **Browser/driver versions:** Not specified in the test session log.
    * **Resource leaks:** There are no obvious resource leaks identified in the test session log. However, the use of Selenium WebDriver and the shared resources (e.g., browser sessions) may introduce resource leaks if not properly managed.
    
    **Performance Insights:**
    
    * **Slow tests:**
        + `test_authorized_page_access` (setup: 3.59s, call: 0.12s)
        + `test_create_new_item` (setup: 3.23s, call: 0.62s)
        + `test_logout` (setup: 3.20s, call: 0.14s)
    * **Bottlenecks:**
        + The setup times for the tests are significantly longer than the call times, indicating that the setup steps may be a bottleneck.
    
    **Recommendations:**
    
    1. **Use explicit waits:** Add explicit waits to the tests to ensure that the elements are present before attempting to interact with them.
    2. **Improve fixture usage:** Use fixtures to manage the setup and teardown of the tests, and ensure that the fixtures are properly initialized and cleaned up.
    3. **Optimize setup steps:** Optimize the setup steps to reduce the setup times and improve the overall performance of the tests.
    4. **Use more robust element locators:** Use more robust element locators, such as CSS selectors or IDs, instead of XPath expressions to reduce the likelihood of errors.
    5. **Monitor resource usage:** Monitor the resource usage of the tests to identify potential resource leaks and optimize the test execution to reduce the resource usage.
    """
    return summary
