
# 概要

旭川版 CHaser (※)のサーバを自分で作りたい。従来のものと比べ、チェイサーの学習を始める人、教える人に更に役立つものとしたい。
[※ CHaser には、全国情報技術教育研究会版とそれを簡略化した旭川版があります。](https://ja.wikipedia.org/wiki/CHaser)

## 使い方

Changeconfig.py を起動し、設定変更(下記参照)をしたあと、
Main.py を実行。Cool と Hot のクライアントからの接続を確認したら、エンターでスタート

## 資料

旭川版 CHaserのサーバを見る[参照](http://www.procon-asahikawa.org/files/2020U16rule.pdf)  
クライアントのプログラムも見る

## プログラム分け

### Main.py

ゲーム本体（ロジックもここ）
クライアントとの通信

### Cliant.py

動作確認用の、クライアントのデモプログラム
クライアント側のプログラムを用意していない方は、
こちらからサーバに接続してください。

### ReadConfig.py

設定ファイルである Config.dt (中身はtxt) の書き込み＆読み込みを行う

### GUI.py

未定

### ChangeConfig.py

設定ファイルの作成・書き換えを行う
CLI が起動するので、内容に従って設定ファイルを作成・書き換えをしてほしい
インデックス入力 → 値の入力で変更
save でセーブして終了  
end でセーブせずに終了

## Config.dt の中身

通常は ChangeConfig.py から作成してほしいが、
json 形式なので、直接書き換えることも可能。

上から順番に（デフォルト値）  

- Coolのポート番号 (2009)
- Hotのポート番号 (2010番)
- ゲーム進行速度[ms] (100)
- 通信タイムアウト時間[ms] (20000)
- ボット対戦モード (0)

### ボット対戦モード

0: オフ
1: lookupするだけ
2: Hot.batを実行する（中身を使いたいBOT用に書き換える)

## 通信例の中身

WireSharkで通信を傍受した結果の改変  

- Client: C  
- Server: (無印)

### 分析

1回目に名前  
Cの#は行動終了、Serverの@は行動開始  
エラーの通信がない(追加したい)
