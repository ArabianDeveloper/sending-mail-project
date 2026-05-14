# Email Sender - Multi Recipient Desktop Application

A professional desktop application for sending personalized emails to multiple recipients from CSV/Excel files.

## Features

✅ **File Support**: Read recipient data from CSV and Excel files  
✅ **Email Personalization**: Use column names to personalize each email  
✅ **SMTP Configuration**: Support for any SMTP server (Gmail, Outlook, custom servers)  
✅ **Settings Persistence**: Save SMTP settings locally  
✅ **Real-time Preview**: See recipient list before sending  
✅ **Progress Tracking**: Visual progress bar and status updates  
✅ **Detailed Logging**: Complete log of all sending operations  
✅ **Error Handling**: Graceful error handling with detailed messages  

## Installation

### 1. Create Virtual Environment (Recommended)

```bash
python -m venv env
env\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### 1. Launch the Application

```bash
python app.py
```

### 2. Configure SMTP Settings

- Enter your email address
- Enter your password (for Gmail, use an [App Password](https://support.google.com/accounts/answer/185833))
- SMTP Server: Default is `smtp.gmail.com`
- SMTP Port: Default is `587`
- Click "Save Settings"

### 3. Select Your Data File

- Click "Browse CSV/Excel"
- Select your CSV or Excel file
- Choose the column containing email addresses

### 4. Compose Your Email

- Enter the subject
- Write the email body
- Use `{{ColumnName}}` to insert data from your file
  - Example: `Hi {{Name}}, your email is {{Email}}`

### 5. Send Emails

- Click "Send Emails"
- Monitor progress in the log

## SMTP Configuration Examples

### Gmail

``` En
Email: your.email@gmail.com
Password: Your App Password (not regular password)
SMTP Server: smtp.gmail.com
SMTP Port: 587
```

### Outlook/Hotmail

``` En
Email: your.email@outlook.com
Password: Your password
SMTP Server: smtp-mail.outlook.com
SMTP Port: 587
```

### Custom SMTP Server

``` En
Email: your.email@company.com
Password: Your password
SMTP Server: mail.company.com
SMTP Port: 587 or 25
```

## CSV/Excel Format Example

| Name | Email | Department | Message |
| ------ | ------- | ----------- | --------- |
| John | <john@example.com> | Sales | Important update |
| Jane | <jane@example.com> | HR | Meeting reminder |
| Bob | <bob@example.com> | IT | Technical support |

## Email Template Example

**Subject:**

``` En
Welcome {{Name}}!
```

**Body:**

``` En
Hi {{Name}},

Welcome to our organization! You are in the {{Department}} department.

{{Message}}

Best regards,
The Team
```

## Important Notes

⚠️ **Security**:

- Store passwords securely
- Use app-specific passwords for Gmail
- Never commit `email_config.json` to version control

📧 **Gmail Setup**:

1. Enable 2-factor authentication
2. Create an [App Password](https://support.google.com/accounts/answer/185833)
3. Use the app password (not your regular password)

🔧 **Troubleshooting**:

- "SMTP connection failed": Check server/port settings
- "Authentication failed": Verify email and password
- "File not found": Ensure CSV/Excel file exists and is readable

## File Structure

``` md
sending mail project/
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── email_settings.json      # Saved settings (auto-generated)
└── README.md             # This file
```

## Supported Formats

- **CSV files**: `.csv`
- **Excel files**: `.xlsx`, `.xls`

## License

Free to use for personal and commercial purposes.
