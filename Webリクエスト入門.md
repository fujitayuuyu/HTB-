# 1 HTTPの基礎
## (1) http
### ① URLの構成
![image](https://github.com/user-attachments/assets/68e0a3cf-8e68-4500-80f3-8ec93a439b57)

| **Component**    | **Example**         | **Description**                                                                                                                                                   |
| ---------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Scheme**       | http:// https://     | クライアントがアクセスするプロトコルを識別するために使い、コロンとダブルスラッシュ (://) で終わる。                                                                 |
| **User Info**    | admin:password@      | 認証に使う資格情報（コロンで区切る）が含まれるオプションのコンポーネントで、ホストとはアットマーク (@) で区切る。                                                  |
| **Host**         | inlanefreight.com    | ホストはリソースの場所を示す。ホスト名またはIPアドレスで指定されることがある。                                                                                      |
| **Port**         | :80                  | ポートはホストとはコロン (:) で区切る。ポートが指定されていない場合、httpはデフォルトでポート80、httpsはポート443を使う。                                           |
| **Path**         | /dashboard.php       | アクセスしているリソース（ファイルやフォルダ）を指す。パスが指定されていない場合、サーバーはデフォルトのインデックス (例: index.html) を返す。                       |
| **Query String** | ?login=true          | クエリ文字列はクエスチョンマーク (?) で始まり、パラメータ (例: login) と値 (例: true) から構成される。複数のパラメータはアンパサンド (&) で区切ることができる。         |
| **Fragments**    | #status              | フラグメントは、クライアント側のブラウザによって処理され、メインリソース内のセクション (例: ページ内のヘッダーやセクション) を特定するために使う。                     |

### ② Webの動き
![image](https://github.com/user-attachments/assets/a8c7cac2-4b11-4506-8ec9-3032753fb3ae)

## (2) https
### ① httpsのフロー
![image](https://github.com/user-attachments/assets/a3fe6b7a-8109-44eb-825c-369364fc9c3b)

### ② curlでSSL証明書のチェックをスキップする方法
> ```
> curl -k $URL
> ```

## (3) HTTPのリクエスト、レスポンス
### ① http request
![image](https://github.com/user-attachments/assets/01e40533-48cc-4533-8f47-c8b3a4617bac)

### ② http response
![image](https://github.com/user-attachments/assets/d2fc9c32-a901-49fc-8c7c-0de35cc016c0)

### ③ curlでリクエストとレスポンスを全表示する方法
```
curl $URL -v
```

## (4) HTTPヘッダー
### ① 一般的なヘッダー
| Header      | Example                                    | Description                                                |
|-------------|--------------------------------------------|------------------------------------------------------------|
| Date        | Date: Wed, 16 Feb 2022 10:38:44 GMT        | メッセージが生成された日時を保持します。時間は標準のUTCタイムゾーンに変換することが推奨されます。 |
| Connection  | Connection: close                          | リクエストが完了した後、現在のネットワーク接続を維持するかどうかを指定します。このヘッダーの一般的な値は「close」と「keep-alive」の2つです。「close」はクライアントまたはサーバーが接続を終了したいことを意味し、「keep-alive」は接続を維持し、追加のデータや入力を受信することを示します。 |

### ② エンティティヘッダ
| Header           | Example                            | Description                                                                                                      |
|------------------|------------------------------------|------------------------------------------------------------------------------------------------------------------|
| Content-Type     | Content-Type: text/html            | 転送するリソースの種類を指定。charset フィールドでエンコーディング（例: UTF-8）を指定。                                  |
| Media-Type       | Media-Type: application/pdf        | Content-Type と同様にデータの種類を指定。charset フィールドも使える。                                                |
| Boundary         | boundary="b4e4fbd93540"            | メッセージ内の複数のコンテンツを区切るためのマーカー。フォームデータの部分を分けるのに使う。                                |
| Content-Length   | Content-Length: 385                | 転送するデータのサイズを指定。ブラウザやツールが自動で生成。                                                       |
| Content-Encoding | Content-Encoding: gzip             | データを圧縮などで変換した場合に使用。どんなエンコーディングかを示す。                                                |

#### ◇ セキュリティ的に
##### ファイルのアップロードでファイルデータを「Content-Type」のみでやってしまうと  
Content-Type自体ユーザ側で変更可能なのでphp形式のファイルなのにcontent-typeを「image/jpeg」に偽装してファイルをアップロード、実行されてしまったりする。  
➡ MIMEタイプチェック、アプリケーションレベルでファイルの中身を検査する(例: PHPのfinfo_file()関数や、Pythonのmimetypesライブラリを使用）。

###### 
