# ここで偉い人がすでに作っている便利機能群をインポートする
import tweepy
from datetime import datetime

# Xにアクセスするための秘密番号を定義する（WebブラウザからX Developersにアクセスして得られる番号）
API_KEY = 'WWWWW'
API_SECRET = 'XXXXX'
ACCESS_TOKEN = 'YYYYY'
ACCESS_TOKEN_SECRET = 'ZZZZZ'

# 通信エージェントを定義する（Xの操作は、この変数の力で実行する）
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# 使いまわしできる「ポスト」機能を定義する
def post(text: str)-> None:
    client.create_tweet(text=text)

# 「ポスト」機能を実行する
text = "Good Morning.\n{0}".format(datetime.now())
post(text)