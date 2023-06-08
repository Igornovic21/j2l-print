from django.conf import settings

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from checkout.models import UserEstimate
from checkout.html import HTML_HEADER_TEMPLATE, HTML_BODY_TEMPLATE, HTML_TABLE_DATA

def format_user_table_data(user:UserEstimate) -> tuple:
    user_data = ""
    user_data_values = ""
    
    user_data += HTML_TABLE_DATA.format(DATA="Nom :")
    user_data += HTML_TABLE_DATA.format(DATA="Prénom :")
    user_data += HTML_TABLE_DATA.format(DATA="Email :")
    user_data += HTML_TABLE_DATA.format(DATA="Organisation :")
    user_data += HTML_TABLE_DATA.format(DATA="Téléphone :")
    user_data += HTML_TABLE_DATA.format(DATA="Addresse :")
    user_data += HTML_TABLE_DATA.format(DATA="Code Postal :")
    user_data += HTML_TABLE_DATA.format(DATA="Ville :")
    user_data += HTML_TABLE_DATA.format(DATA="Message :")
    
    user_data_values += HTML_TABLE_DATA.format(DATA=user.last_name)
    user_data_values += HTML_TABLE_DATA.format(DATA=user.first_name)
    user_data_values += HTML_TABLE_DATA.format(DATA=user.email)
    user_data_values += HTML_TABLE_DATA.format(DATA=user.organisation)
    user_data_values += HTML_TABLE_DATA.format(DATA=user.phone)
    user_data_values += HTML_TABLE_DATA.format(DATA=user.address)
    user_data_values += HTML_TABLE_DATA.format(DATA=user.postal_code)
    user_data_values += HTML_TABLE_DATA.format(DATA=user.city)
    user_data_values += HTML_TABLE_DATA.format(DATA=user.message)
    
    return user_data, user_data_values


def format_config_table_data(configurations:list) -> tuple:
    user_configurations = ""
    user_configurations_values = ""
    
    for configuration in configurations:
        for k, v in configuration.items():
            user_configurations += HTML_TABLE_DATA.format(DATA=k + " :")
            user_configurations_values += HTML_TABLE_DATA.format(DATA=v)
            
    return user_configurations, user_configurations_values


def send_mail_estimate(user:UserEstimate, configurations:list) -> bool:
    subject, from_email, to = 'DEMANDE DE DEVIS', settings.EMAIL_HOST_USER, ['j2l@tenteeglobal.com', user.email]
    user_data, user_data_values = format_user_table_data(user)
    user_configurations, user_configurations_values = format_config_table_data(configurations)
    html_content = HTML_HEADER_TEMPLATE + HTML_BODY_TEMPLATE.format(
        USER_INFO=user_data,
        USER_INFO_VALUES=user_data_values,
        USER_CONFIGURATIONS=user_configurations,
        USER_CONFIGURATIONS_VALUES=user_configurations_values
    )
    
    body = MIMEText(html_content, _subtype='html')
    email = MIMEMultipart(_subtype='related')
    email['From'] = from_email
    email['Subject'] = subject
    email['To'] = ",".join(to)
    email.attach(body)

    try:
        server = smtplib.SMTP_SSL(settings.EMAIL_HOST)
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        text = email.as_bytes()
        server.sendmail(from_email, email['To'].split(","), text)
        server.quit()
        return True
    except Exception as e:
        print('Failed to send email:', e)
        return False