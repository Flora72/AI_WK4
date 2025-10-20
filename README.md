```markdown
# Practical Implementation – AI in Software Engineering Assignment

This repository contains the practical deliverables for Week 4's assignment on **"Building Intelligent Software Solutions"**. It showcases how AI can automate coding tasks, enhance testing, and support predictive analytics in software engineering.

---

## Task 1: AI-Powered Code Completion

**Objective:**  
Compare an AI-suggested Python function (via GitHub Copilot) with a manually written version for sorting a list of dictionaries by a specific key.

**Files:**
- `sort_dicts_ai_vs_manual.py`: Contains both implementations.
- [Task 1 Report (Google Doc)](https://docs.google.com/document/d/1IMf61X2JIdBNQEHGaBYMpcvC_dBi5LciOXyGoH94wWE/edit?usp=sharing): Includes code snippets, analysis, and reflections.

**Summary:**  
GitHub Copilot generated a concise, well-documented function using Python’s built-in `sorted()` method. Compared to the manual version, the AI code was more readable and efficient. This task demonstrates how AI tools can accelerate development while requiring human oversight for correctness.

---

## Task 2: Automated Testing with AI

**Objective:**  
Use Testim.io or Selenium IDE with AI plugins to automate login page testing for valid and invalid credentials.

**Files:**
- `login_test_selenium.py`: Automated test script using Selenium WebDriver.
- `login.html`: Mock login page used for testing.
- `screenshots/`: Folder containing test result screenshots.

**Summary:**  
I used Selenium WebDriver to automate login testing on a mock HTML page. The script simulates user input for both valid and invalid credentials, verifies the output message, and captures screenshots for documentation. This approach demonstrates how browser automation can improve test coverage and reliability in software development. Compared to manual testing, Selenium offers speed, repeatability, and scalability. The test script uses direct element locators and assertions to validate expected behavior. ChromeDriver was configured to match the installed browser version, ensuring compatibility. This task highlights the importance of reproducible environments and version alignment when working with browser automation tools. The screenshots provide visual confirmation of test outcomes, supporting the written results. Overall, Selenium WebDriver proves to be a powerful tool for regression testing and UI validation in modern development workflows.

**Report:**  
- [Task 2 Report (Google Doc)](https://docs.google.com/document/d/1SQddWvjjgP1BzKwuD4e4DpUGd5ubGTQ5-3nwJxz0tNg/edit?usp=sharing)


## Task 3: Predictive Analytics for Resource Allocation

**Objective:**  
Use the Kaggle Breast Cancer Dataset to train a machine learning model that predicts issue priority (high/medium/low).

**Files:**
- `predict_priority.ipynb`: Jupyter Notebook with preprocessing, model training, and evaluation.
- `metrics/`: Folder with accuracy, F1-score, and confusion matrix visuals.

**Summary:**  
A Random Forest model was trained to classify issue priority based on labeled data. The model achieved strong performance metrics, demonstrating how predictive analytics can support smarter resource allocation in software projects.

---

## Ethical Reflection

**Prompt:**  
Discuss potential biases in the dataset used for Task 3 and how fairness tools like IBM AI Fairness 360 could mitigate them.

**Summary:**  
The dataset may underrepresent certain teams or issue types, leading to biased predictions. Tools like IBM AI Fairness 360 can audit and correct these biases through reweighting and adversarial debiasing, ensuring equitable outcomes.

---

## Task 3: Predictive Analytics for Resource Allocation

**Objective:**  
Use the Breast Cancer Dataset to train a machine learning model that predicts issue priority (high/low).

**Files:**
- `predict_priority.ipynb`: Jupyter Notebook with preprocessing, model training, and evaluation.
- `metrics/`: Folder with accuracy, F1-score, and confusion matrix visuals.

**Summary:**  
A Random Forest model was trained to classify issue priority based on labeled data. The model achieved strong performance metrics, with minimal misclassifications and clear feature importance. This task demonstrates how predictive analytics can support smarter resource allocation in software projects by identifying high-priority cases early and reliably.

---

## Bonus Task: Innovation Challenge

**Proposal:**  
An AI-powered documentation generator that parses code, commit history, and architecture diagrams to produce clean, updated technical documentation.

**File:**
- `ai_docgen_proposal.pdf`: 1-page proposal outlining purpose, workflow, and impact.

---

## Submission Links

- [Week 4 Full Report (Google Doc)](https://docs.google.com/document/d/1rzOd3mRqmWVk7XXcvqHbqMPtk_bn_f7MLFN3Yfe_ACQ/edit?usp=sharing)
- [Task 1 Report](https://docs.google.com/document/d/1IMf61X2JIdBNQEHGaBYMpcvC_dBi5LciOXyGoH94wWE/edit?usp=sharing)
- [Task 2 Report](https://docs.google.com/document/d/1SQddWvjjgP1BzKwuD4e4DpUGd5ubGTQ5-3nwJxz0tNg/edit?usp=sharing)


---


