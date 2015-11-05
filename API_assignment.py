import urllib2, json
import re 

def clean_json(json):
    return re.sub(r'new Date\(.*?\)', '""', json)

#1.Hillary's emails
#data = urllib2.urlopen('https://foia.state.gov/search/results.aspx?searchText=*&caseNumber=F-2014-20439').read()

#2.Benghazi emails
#data = urllib2.urlopen('https://foia.state.gov/search/results.aspx?searchText=Benghazi&caseNumber=F-2014-20439').read()

dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?searchText=*&beginDate=false&endDate=false&postedBeginDate=false&postedEndDate=false&caseNumber=F-2014-20439&collectionMatch=false&page=1&start=0&limit=15766').read()
valid_json = clean_json(dirty_json)

data = json.loads(valid_json)

#3.print raw files
for links in data['Results']:
    print links['pdfLink']
