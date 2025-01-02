0. 仮想環境をアクティベートする

source venv/bin/activate

1. 時刻表を名古屋市交通局のサイトからJSON形式でスクレイピングする。このディレクトリで下記コマンドを実行する

scrapy crawl diagrams -o all_yyyymmdd.json

2. all_yyyymmdd.jsonをall.jsonにリネームしてから、アプリで利用可能な形式に変換する

python convert_json.py



