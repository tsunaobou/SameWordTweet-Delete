import json
import glob
import tweepy
from dotenv import load_dotenv
import os
from tqdm import tqdm

#twitterAPIの認証キーの呼び出し
load_dotenv('.env')
TWITTERAPI_CONSUMER_KEY = os.getenv('TWITTERAPI_CONSUMER_KEY')
TWITTERAPI_CONSUMER_SECRET = os.getenv('TWITTERAPI_CONSUMER_SECRET')
TWITTERAPI_ACCESS_TOKEN = os.getenv('TWITTERAPI_ACCESS_TOKEN')
TWITTERAPI_ACCESS_TOKEN_SECRET = os.getenv('TWITTERAPI_ACCESS_TOKEN_SECRET')

#最初にdataフォルダに解析したいファイルを配置しておくこと
tweetsId = []   #ツイートのID

#jsファイルの探索部分
filePath = glob.glob('data/*.js')

for fp in filePath:
    with open(fp,mode='r',encoding='utf-8_sig') as f:
        data = f.read()
    #jsonファイルは[]区切りや{}区切りでも読める。
    #今回は[から]までを取得したい、そのため始点[のインデックスを取るために.findメソッドを使う。
    jsonStartIndex = data.find('[')
    tweetsData = json.loads(data[jsonStartIndex:])  #スライスで[以降を取得する。ファイルの終点は]のためそのまま最後まで読みこむだけで[から]までが取得できる
    #ツイートの検索部分
    for tweet in tweetsData:
        if "String You Want to Delete" in tweet['tweet']['full_text']:
            tweetsId.append(tweet['tweet']['id'])
            print(tweet['tweet']['full_text'])
print(len(tweetsId))

#ここからtweepyのツイート削除部分
auth = tweepy.OAuth1UserHandler(consumer_key=TWITTERAPI_CONSUMER_KEY,consumer_secret=TWITTERAPI_CONSUMER_SECRET,
                                access_token=TWITTERAPI_ACCESS_TOKEN,access_token_secret=TWITTERAPI_ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
for id in tqdm(tweetsId):
    api.destroy_status(id)
    
