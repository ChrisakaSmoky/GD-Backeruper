Here's a README file explaining what users will need to run the provided program:

---

# Google Drive Backup Program

This program allows you to backup a local folder to Google Drive using the Google Drive API.

## Requirements:

1. **Python**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Google API Credentials**:
    - You need to set up Google API credentials to authenticate with the Google Drive API. Follow these steps:
        1. Go to the [Google API Console](https://console.developers.google.com/).
        2. Create a new project.
        3. Enable the Google Drive API for your project.
        4. Create credentials (OAuth 2.0 client ID).
        5. Download the credentials JSON file and save it as `credentials.json` in the same directory as the program.

3. **Required Python Libraries**:
    - Install the required Python libraries using pip:
        ```
        pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client schedule
        ```

## Usage:

1. **Running the Program**:
    - Run the program by executing the script using Python:
        ```
        python <script_name>.py
        ```
    - Follow the prompts to provide the local folder path and Google Drive folder ID.

2. **Resetting Credentials**:
    - If you need to reset your current credentials, type 'y' when prompted. This will remove the existing token file (`token.json`).

3. **Scheduled Backups**:
    - The program schedules backups to run every 24 hours. You can modify the schedule as needed in the script.

4. **Note**:
    - Ensure the local folder path and Google Drive folder ID are correctly entered to avoid errors during backup.

---

Feel free to reach out if you have any questions or encounter any issues!
