import requests
from bs4 import BeautifulSoup
import time
import smtplib

url = "http://reddit.com/"
headers = {'User-Agent': 'Chrome/56.0.2924.87'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

while True:
	#store the last retrieved soup for comparison
	oldSoup = soup
	#get the webpage again
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, "lxml")
	
	#create strings from the old & new soups to compare
	str1 = str(soup)
	str2 = str(oldSoup)
	
	#the old "check for changes" code
	#if str(soup).find("Reddit") == -1:
	#	time.sleep(60)
	#	continue
	#compare the two strings
	if str1 == str2:
		continue
	else:
		msg = 'REDDIT UPDATED!'
		fromaddr = 'justthings4schcool@gmail.com'
		toaddr  = ['thanhtrinh12122010@gmail.com','davidtrieu6@gmail.com', 'gameguy47@gmail.com', 'francis.c.phan@gmail.com']

		server = smtplib.SMTP("smtp.gmail.com:587")
		server.starttls()
		server.login("justthings4schcool@gmail", "M1lk3yway")

		# Print the email's contents
		print('From: ' + fromaddr)
		print('To: ' + str(toaddrs))
		print('Message: ' + msg)
		server.sendmail(fromaddr, toaddrs, msg)
		server.quit()

		break
		
	time.sleep(60)
