# Module 11 - CI pipeline

**Goal**: implement all the tests in a CI pipeline

## Steps

1. Add this project to your Semaphore account
2. Use this command to select Python version in your jobs: `sem-version python 3.12`
3. Create a pipeline with these blocks in order:

### Block 1: Install dependencies
```bash
# Install test dependencies for each module
pip install pytest requests flask coverage locust
```

### Block 2: Unit tests (Exercises 1-2)
```bash
cd 1-tdd && python -m pytest test_factorial.py -v
cd 2-unit-testing && python -m pytest test_math_sum.py -v
```

### Block 3: Integration tests (Exercises 3, 6, 10)
```bash
cd 3-integration-testing && python -m pytest test_integration.py -v
cd 6-mocking && python -m pytest test_weather_service.py -v
cd 10-database-testing && python -m pytest test_database.py -v
```

### Block 4: End-to-end tests (Exercise 4)
```bash
# Start the Flask app in background
cd 4-e2e && nohup python app.py &
sleep 3
python -m pytest test_e2e.py -v
```

### Block 5: Test coverage (Exercise 7)
```bash
cd 7-test-coverage
coverage run -m pytest test_calculator.py -v
coverage report -m
```

### Block 6: Performance testing (Exercise 8)
```bash
# Run Locust in headless mode
cd 8-performance-testing
nohup python -c "import sys; sys.path.insert(0, '../4-e2e'); from app import app; app.run()" &
sleep 3
locust -f locustfile.py --host=http://127.0.0.1:5000 --headless -u 10 -r 2 --run-time 30s
```

### Block 7: Security tests (Exercise 9)
```bash
cd 9-security-testing
nohup python -c "import sys; sys.path.insert(0, '../4-e2e'); from app import app; app.run()" &
sleep 3
python -m pytest test_security.py -v
```

### Block 8: Test reports (Exercise 5)
```bash
cd 5-test-reports
pip install -r requirements.txt
pytest --junitxml=reports.xml
[[ -f report.xml ]] && test-results publish report.xml
```

4. Create an "After pipeline job" with:
```bash
test-results gen-pipeline-report
```

5. Check the test reports dashboard after running the pipeline

## Tips

- Check pipeline.png in this folder to see an example.
- If you have trouble running `app.py` in CI try using `nohup python app.py &`
- You can parallelize blocks that don't depend on each other
- Consider using caching to speed up dependency installation
