from django.core.mail import send_mail
from accounts.models import Account
from acme import settings





def send_mail_func(id):

    user = Account.objects.get(email = id)
    
    subject = 'Your ticket has been created'
    message = f'Dear {user.first_name}, Your ticket has been created with the ticket ID 4033 and subject "Something"\n Someone from our customer service team will review it and respond shortly. \n Regards,\n PeerXP Support Team.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email,]
    send_mail( subject, message, email_from, recipient_list )
    
    return 'Done'