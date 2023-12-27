# Flask Mail App
## Description
This is a simple Flask app that sends emails using Flask-Mail extension with Gmail as the email service provider.

## Installation/Setup
1. Clone this repository and `cd` into it.
```bash
git clone https://github.com/pgk95/flask-mail.git
cd flask-mail
```
2. Create a virtual environment and activate it.
```bash
python3 -m venv venv

# For Linux/MacOS
source venv/bin/activate

# For Windows
venv\Scripts\activate
```
3. Install the dependencies.
```bash
pip install -r requirements.txt
```
4. Create a `.env` file and add the following environment variables.
```bash
# Gmail credentials
MAIL_USERNAME=<your-gmail-username>
MAIL_PASSWORD=<your-gmail-password>

# Email settings
MAIL_DEFAULT_SENDER=<your-gmail-username>
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USE_TLS=False
```
5. Run the app.
```bash
python app.py
```
6. Open `http://localhost:5000` in your browser.

## checking the email
1. Open your gmail account and go to settings.
2. Go to the `Accounts and Import` tab.
3. Click on `Other Google Account settings`.
4. Click on `Security` in the left sidebar.
5. Scroll down to the `Less secure app access` section and click on `Turn on access (not recommended)`.
6. Now, go to `http://localhost:5000` and send an email.
7. Check your inbox to see if you have received the email.