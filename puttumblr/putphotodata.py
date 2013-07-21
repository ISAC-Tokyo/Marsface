#!/opt/local/bin/python
#coding: utf-8

from tumblpy import Tumblpy

CONSUMER_KEY = 'Musqb3f5NbD9TnXzoI3KkbIsOc6qbpAiW0d4HprSvZRxzLGUjj'
CONSUMER_SECRET = 'Vp7pnxYxGwg3XfWhjSZFNCByQHtMUUrvGoJWTsMxmW7oxWM8bU'
ACCESS_TOKEN = '91LC1vQuFzqM7B9kiU1oqLG1BItt43LmbFYWvCnLu2Ebg5ahKo'
ACCESS_TOKEN_SECRET = '821sykPEGqxd2XiITiX5BasKAn8zJ91ITStyoj27YUPlOn2igw'
BASE_HOSTNAME = 'marfaceproj.tumblr.com'

def main():
    t = Tumblpy(app_key = CONSUMER_KEY,
                app_secret = CONSUMER_SECRET,
                oauth_token=ACCESS_TOKEN,
                oauth_token_secret=ACCESS_TOKEN_SECRET)

    blog_url = t.post('user/info')
    blog_url = blog_url['user']['blogs'][0]['url']

    files = open('/home/miyamamoto/work/Marsface/result/PIA08533_result.png', 'rb')
    
    post = t.post('post', blog_url=blog_url, params={'type':'photo', 'caption': 'http://www.nikkei.co.jp', 'data':files})


#    url = 'http://api.tumblr.com/v2/blog/%s/post' % BASE_HOSTNAME
#    post_title = 'テ ス ト 投 稿 '
#    post_body = 'こ れ は テ ス ト 投 稿 で す 。 '
#    token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_TOKEN_SECRET)
#    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
#    params = {
#        'type': 'text',
#        'state': 'draft',
#        'title': post_title,
#        'body': post_body,
#    }
#    client = oauth2.Client(consumer, token)
#    resp, content = client.request(url, method='POST', body=urlencode(params))

if __name__ == '__main__':
    main()
