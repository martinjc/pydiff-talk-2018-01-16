
from config import *
from mailer import Mailer

message = "YOU'RE STRETCHING THIS CONSPIRACY THING REALLY FAR NOW!"
subject = '**REALLY URGENT PLEASE READ*** THE CONSPIRACY IS VERY REAL!!!!11 STOP TALKING'

mailer = Mailer(SMTP_USERNAME, SMTP_PASSWORD, SMTP_SERVER, SMTP_PORT)

mailer.send(SEND_FROM, ['martin.chorley@gmail.com'], subject, message)
