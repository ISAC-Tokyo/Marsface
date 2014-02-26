#!/opt/local/bin/python
#coding: utf-8

from tumblpy import Tumblpy
import sys
import csv
import os.path

#

def main():
    csvfile = sys.argv[1]
    reader = csv.reader(file(csvfile, 'r'), delimiter   = ','  )
    
    for row in reader:
        t = Tumblpy(app_key = CONSUMER_KEY,
                    app_secret = CONSUMER_SECRET,
                    oauth_token=ACCESS_TOKEN,
                    oauth_token_secret=ACCESS_TOKEN_SECRET)
        
        blog_url = t.post('user/info')
        blog_url = blog_url['user']['blogs'][0]['url']
    
        files = open('/home/miyamamoto/work/Marsface/result/PIA08533_result.png', 'rb')
        url = os.path.splitext(row[1])[0].replace('tiff', 'catalog')
        post = t.post('post', blog_url=blog_url, params={'type':'photo', 'caption': url, 'data':files})

        url = " http://" +BASE_HOSTNAME + "/" +  str(post['id'])
        print url
        rows = [row[1],row[2],url]
        writer = csv.writer(open("aaa.csv",'w'),lineterminator="¥t")
        writer.writerows(rows)
        

if __name__ == '__main__':
    main()
