```markdown
# INTELLIGENTSIA Club Email Script

This Python script is used to send high-priority congratulatory emails to newly selected aspirants of the INTELLIGENTSIA club. Each aspirant will receive an email that includes a link to join the official Aspirants group on Telegram.

## Prerequisites

- Python 3.x installed on your system.
- Required Python libraries:
  - `smtplib`
  - `email.mime` (MIMEMultipart and MIMEText)

These libraries are available in the standard Python library, so no need for external installations.

## Email Configuration

The script uses Gmail's SMTP server to send emails. You'll need:
1. The sender email (used for the club).
2. A generated App password for Gmail, since using regular passwords may not work due to security settings.

### Steps to Generate App Password:
1. Go to your Gmail account settings.
2. Navigate to 'Security' and enable 2-Step Verification (if not already enabled).
3. Under the 'Signing in to Google' section, generate an App password.
4. Copy the App password and replace it in the script where the password is defined.

## Usage

1. **Update Sender Email Credentials:**
   In the script, replace the `sender_email` and `password` with your club's email and the generated app password:
   ```python
   sender_email = "your_email@gmail.com"
   password = "your_app_password"
   ```

2. **Aspirant IDs:**
   The script uses a list of aspirant IDs and sends emails to the corresponding institutional email addresses (`<id_number>@kluniversity.in`). If you need to add more IDs, modify the `aspirant_ids` list:
   ```python
   aspirant_ids = [
       "2300030379",
       "2300033155",
       # Add more aspirant IDs
   ]
   ```

3. **Update Telegram Link:**
   Replace the `telegram_link` variable with the valid invite link to your Telegram group:
   ```python
   telegram_link = "https://t.me/your_group_link"
   ```

4. **Run the Script:**
   Once all configurations are set, run the Python script. The script will send personalized high-priority emails to each aspirant.

   ```bash
   python send_emails.py
   ```

## Script Details

- The script sends emails via Gmail's SSL-enabled SMTP server on port 465.
- The email contains a high-priority flag, ensuring it appears with more visibility in the recipient's inbox.
- The message contains a body with the aspirant's selection information and a link to the Telegram group.
- The emails are addressed to `<ID_NUMBER>@kluniversity.in`, so make sure the aspirants' ID numbers are correctly input in the `aspirant_ids` list.

## Example Email Content

```
Dear Aspirant,

Congratulations on being selected as part of the INTELLIGENTSIA club!

We are excited to have you on board and can't wait to see the amazing work you'll contribute. 
As a next step, please join the official Aspirants group using the following link:

https://t.me/+cYly3NBMztM4MGFl

Please note, the link will expire in 6 days.
When joining the group, use the following format: <ID_NUMBER NAME>

Best regards,
INTELLIGENTSIA Team
Department of AI & DS
```

## Notes

- Ensure you have a stable internet connection while sending emails.
- The Telegram link is only valid for 6 days, so update it as necessary if you're running the script later.
- If you encounter any issues with SMTP or authentication, verify your Gmail account's app password and the correct port (465 for SSL).

## License

This project is open-source and available for use and modification.
```

This `README.md` provides all the necessary details for setting up, configuring, and using the script effectively.
