# Django API Project Setup

This repository contains a Django API project setup guide with instructions on installing Virtualenv, creating a virtual environment outside the API project directory, installing Django and Django Rest Framework, and running the Django app.

## Prerequisites

Before proceeding with the setup, make sure you have the following installed:

- Python 3.x
- pip (Python package installer)

## Installation Steps

### 1. Install Virtualenv

```
pip install virtualenv

virtualenv myenv

myenv\Scripts\activate

pip install django djangorestframework

git clone <repository-url>

cd <api-project-directory>

python manage.py runserver
