import smtplib
import random
import datetime as dt
import pandas


now = dt.datetime.now()
data = pandas.read_csv("birthdays.csv")
data = data[data["month"] == now.month]
data = data[data["day"] == now.day]
name = data.at[1,"name"]

letter_list=["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
to_email = data.at[1,"email"]

with open(random.choice(letter_list),"r") as file1:

    message = file1.read()
    message = "".join(message)
    message = message.replace("[NAME]",str(name))
with open("quotes.txt","r") as file:
    list = file.readlines()
    message += "\n"+random.choice(list).strip()
print (message)


# for password use your own application password your email gives you

my_email = "xristakos167@gmail.com"
password = "sqpl gruy raxn hyyh"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=to_email,
                        msg =f"Subject:Happy birthday \n\n {message}")
