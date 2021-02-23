#Program to send emails
import smtplib
#We access e-mail
print("\t\tSign in")
my_email = str(input("Insert your email:"))
my_password = str(input("Insert your password:"))
print()
oggetto = input("Inserisci l'oggetto della mail: ")
messaggio = input("Ora puoi inserire il messaggio che vuoi inviare: ")
contenuto = oggetto + messaggio
print("Sto effettuando la connessione col Server...")
server = smtplib.SMTP("smtp.gmail.com", 587) # questa configurazione funziona per gmail
server.starttls() # email criptata
server.login("niccolofato13@gmail.com", "")
server.sendmail("niccolofato13@gmail.com", "niccolofato14@gmail.com", contenuto)
server.close()
