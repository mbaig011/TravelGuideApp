# TravelGuideApp

A lightweight, server‑rendered Flask application that provides curated travel information for global cities, including top attractions, itineraries, and user‑submitted reviews. Built as part of the **DevOps and AI on AWS** specialization, this project demonstrates clean Python architecture, DynamoDB integration, automated testing, linting, and preparation for generative‑AI upgrades.

## Features

* **City Directory**Browse a list of cities stored in DynamoDB.
* **City Detail Pages**View country information, top things to do, and recommended itineraries.
* **User Reviews**Display star‑rated reviews stored in a DynamoDB table.
* **Flask Server‑Rendered UI**Clean Jinja templates with custom filters (`nl2br`, `relative_url`).
* **AWS DynamoDB Integration**Uses `boto3` to query and scan city and review data.
* **High Code Quality**
  * **Pylint Score:** 10.00/10
  * **Test Coverage:** 96%
  * Fully passing unit tests

## Architecture Overview

**Backend:** Python + Flask
**Data Layer:** AWS DynamoDB
**Templates:** Jinja2
**Testing:** `unittest` + Flask test client
**Linting:** Pylint
**Coverage:** Coverage.py
**Deployment-ready:** Can run locally or be containerized for AWS deployment

## Project Structure

TravelGuideApp/
│
├── app.py                # Main Flask application
├── test_app.py           # Unit tests (96% coverage)
├── templates/            # Jinja2 HTML templates
│   ├── index.html
│   ├── city.html
│   └── 404.html
├── local_build.sh        # Lint + test + coverage automation
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

## Setup Instructions

**1. Clone the Repository**

git clone https://github.com/<your-username></your>/TravelGuideApp.git
cd TravelGuideApp

**2. Install Dependencies**
Code
pip install -r requirements.txt

**3. Configure AWS Credentials**
Ensure your AWS CLI or environment variables provide access to DynamoDB:

Code
aws configure

**4. Run the Application**
Code
python app.py
Visit:

Code
http://localhost:5000

Testing & Code Quality
Run Pylint
Code
pylint app.py
Run Unit Tests
Code
python -m unittest
Generate Coverage Report
Code
coverage run -m unittest
coverage html
Open htmlcov/index.html to view detailed coverage.

🧰 Custom Jinja Filters
nl2br
Converts newline characters into  tags for readable multi-line text.

relative_url
Generates relative paths for internal navigation.

🗄️ DynamoDB Tables
Cities Table
Attribute	Type
CityName	PK
CountryCode	S
CountryName	S
TopThingsToDo	S
Itinerary	S

CityReviews Table
Attribute	Type
CityName	PK
ReviewContent	S
Stars	N

🔮 Next Steps (Lab 2 Preview)
This project is designed to be upgraded with:

Amazon Bedrock generative AI

AI‑powered itinerary generation

AI‑enhanced travel recommendations

CI/CD pipelines for automated deployment

Containerization and AWS deployment

👤 Author
Mirza Baig
GitHub: https://github.com/<your-username></your>
Specialization: DevOps and AI on AWS

📄 License
This project is part of the AWS DevOps & AI learning labs and is intended for educational use.
