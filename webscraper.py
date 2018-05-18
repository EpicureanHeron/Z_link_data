import csv
import urllib2

file_1 = open("ListOfURLStest.txt", "r+") 
file_2= open("Results.txt", "r+")

#https://stackoverflow.com/questions/16283799/how-to-read-a-csv-file-from-a-url-with-python

#I could create a text file that can be read in as a list (or dictionary with URL : CR#) which prints its findings puts it in another file based on the count

urlArray = file_1.readlines()

for urlcsv in urlArray:
	response = urllib2.urlopen(urlcsv)
	cr = csv.reader(response)
	
	for row in cr:
		print row
		

'''

url = 'https://z.umn.edu/shortener/urls/154734/csv/click_data.csv' 
response = urllib2.urlopen(url)
cr = csv.reader(response)
count = -1 #this is -1 so it ignores the header information

for row in cr:
    print row
    count = count + 1
	
print count
'''


#https://z.umn.edu/shortener/urls/154734/csv/click_data.csv URL for CR13 before clicked the export to CSV button, the screen defaults in on "last 24 hours" which is 0 currently and aftering
# running this program it returns 51 which is the all time amount

#After hitting the "export to csv" button I got this URL https://z.umn.edu/shortener/urls/154734/csv/click_data.csv and it is sitll on the graph for the last 24 hours, still at 51

#Click on last 30 days, the url https://z.umn.edu/shortener/urls/154734/csv/click_data.csv the data still shows as 51 and 


#I'm not sure how the csv data works...the URL doesn't change but the data CAN change and it doesn't seem to be dictated by the tab using. I have got data that is not the "all time data"...but I can't recreate that for w/e reason