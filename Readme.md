# Python Automation Framework

### Tech Stack
- Python 3.12
- Requests-HTTP requests
- PyTest-Testing Framework
- Reporting-Allure report,PyTest HTML
- Test Data-CSV,Excel,JSON,Faker
- Advance API Testcase- jsonschema
- Parallel Execution-x distribute (xdist)

### How to install Packages
pip install requests pytest pytest-html faker allure-pytest jsonschema

### How to run Testcase parallel
pip install pytest-xdist

### How to add .gitignore file?
copy the content from this to .gitignore file
https://www.toptal.com/developers/gitignore/api/pycharm

### How to run a basic Test with allure report?
 pytest tests/crud/test_create_booking.py --alluredir=allure_result -s
 
### How to see allure report?
allure serve allure_result

