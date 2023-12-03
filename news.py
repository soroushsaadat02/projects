from newsapi import NewsApiClient
from datetime import datetime
import csv

newsapi = NewsApiClient(api_key='57d4fec5debd41668df5a0d42623549a')

# search property
keywords = 'oil , gold , dollar'
language = 'en'
sort_by = 'publishedAt'

# search limited time
from_date = datetime( 2023,11,25).strftime('%Y-%m-%d')
to_date = datetime(2023,12,1).strftime('%Y-%m-%d')

# get news
response = newsapi.get_everything(q=keywords, language=language, sort_by=sort_by, from_param=from_date, to=to_date)

# save as .csv file
csv_file = 'news_project.csv'

# get news's list
articles = response['articles']

# read and write .csv file
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    # columns
    writer.writerow(['Published Date' ,'Subject' ,  'Title'])

    # row
    for article in articles:
        writer.writerow([article['publishedAt'] , keywords , article['title']])
