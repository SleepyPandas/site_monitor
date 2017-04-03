import requests
from bs4 import BeautifulSoup
import time
import smtplib

url = "http://reddit.com/"
headers = {'User-Agent': 'Chrome/56.0.2924.87'}
while True:
	response1 = requests.get(url, headers=headers)
	soup1 = BeautifulSoup(response1.text, "lxml")
	time.sleep(1)
	response2 = requests.get(url, headers=headers)
	soup2 = BeautifulSoup(response2.text, "lxml")
	if str(soup1) == str(soup2):
		continue
	else:
		print "Reddit updated!"
		#msg = 'REDDIT UPDATED!'
		#fromaddr = 'justthings4schcool@gmail.com'
		#toaddr  = ['thanhtrinh12122010@gmail.com','davidtrieu6@gmail.com', 'gameguy47@gmail.com', 'francis.c.phan@gmail.com']

		#server = smtplib.SMTP("smtp.gmail.com:587")
		#server.starttls()
		#server.login("justthings4schcool@gmail", "M1lk3yway")

		# Print the email's contents
		#print('From: ' + fromaddr)
		#print('To: ' + str(toaddrs))
		#print('Message: ' + msg)
		#server.sendmail(fromaddr, toaddrs, msg)
		#server.quit()

		break
