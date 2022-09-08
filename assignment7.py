#Week 7 assignment - Dump the news

import csv
import json
import urllib.request

def load_news_json():
    URL = "https://www.npr.org/feeds/1019/feed.json"
    json_string = urllib.request.urlopen(URL).read()
    news_dict = json.loads(json_string)
    return(news_dict["items"])


output_file = open('news.csv', 'w', newline='')
csv_writer = csv.writer(output_file)
csv_writer.writerow(['title', 'url'])
news = load_news_json()

for i in news:
    title = str(i["title"])
    url = str(i["url"])
    csv_writer.writerow([title, url])
output_file.close()