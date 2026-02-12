# Web Automation Testing - DEMO
#### Selenium - Python 
MDG 2026

---
# Environment Versions
- macOS Tahoe Version 26.2 (25C56)
- Homebrew 5.0.14
- node v25.6.1
- Google Chrome Version 144.0.7559.110
- ChromeDriver 144.0.7559.96
- Python 3.14.2
- 
---

# Set up
1. Install python on machine
   - brew install python
   - python --version
   - python3 --verison
2. Navigate to root project directory
3. Set up virtual environment
   - python3 -m venv .venv
4. Activate virtual environment
   - source .venv/bin/activate
5. Install requirements
   - pip3 install -r requirements.txt

---
# Tests
### Run all tests:
- pytest

### Run all tests with verbose output
- pytest -v

### Run with print statements visible
- pytest -v -s

### Run specific test
- pytest tests/test_bat_suite.py::TestBuildAcceptance::test_homepage_loads -v

### Run tests matching a keyword
- pytest -k "homepage" -v

### Run tests in parallel (requires pytest-xdist)
- pip install pytest-xdist
- pytest -n 4  # Run with 4 workers

### Generate HTML report (requires pytest-html)
pip install pytest-html
pytest --html=report.html --self-contained-html
