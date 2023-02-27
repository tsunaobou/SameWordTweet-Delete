# SameWordTweet-Delete

同じ単語が含まれるツイートを一括で消去します。
同じ単語を何回もつぶやいてしまって黒歴史になった人とかは特に使えると思います。

## 使い方

1. `python-dotenv`と`tweepy`と`tqdm`をインストールする

```cmd
pip install python-dotenv tweepy tqdm
```

2. このリポジトリをcloneする

3. Twitterからデータのアーカイブをダウンロードし、`tweets.js`,`tweets-partN.js(Nは任意の自然数)`を探して`data`フォルダーに入れる

4. Twitter APIの4つのキー(コンシューマーキー,コンシューマーシークレット,アクセストークン,アクセストークンシークレット)を`.env.sample`にしたがって`.env`の中に書く

5. `String You Want to Delete`の部分を自分が消したい文言にする

6. スクリプトを動かす
