
# SQL Database Interaction with GCP Gemini and Langchain

This application demonstrates how to use Google Cloud Platform's Gemini model with Langchain to interact with a SQLite database.

## Setup

1. Install the required Python packages:
    ```
    pip install -r requirements.txt
    ```

2. Ensure you have a SQLite database file named `Chinook.db` in your project directory.

3. Configure the Gemini model with your GCP API key in `app.py`.

## Running the Application

Execute the script using Python:

```
python app.py
```

## GCP Permissions

Ensure your GCP service account has the following permissions:
- Access to the Gemini API
- Appropriate roles for using AI and machine learning services on GCP

Consult the GCP documentation for detailed instructions on setting up permissions and roles.
