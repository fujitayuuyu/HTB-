# 1 webアプリケーション入門
## (1) Webアプリケーションの脆弱性
<table class="table table-striped text-left">
<thead>
<tr>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">欠陥</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">現実世界のシナリオ</font></font></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://owasp.org/www-community/attacks/SQL_Injection" target="_blank" rel="noopener nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">SQLインジェクション</font></font></a></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Active Directory のユーザー名を取得し、VPN または電子メール ポータルに対してパスワード スプレー攻撃を実行します。</font></font></td>
</tr>
<tr>
<td><a href="https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion" target="_blank" rel="noopener nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ファイルのインクルード</font></font></a></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ソース コードを読み取って、リモート コード実行に使用できる追加機能を公開する隠しページまたはディレクトリを見つけます。</font></font></td>
</tr>
<tr>
<td><a href="https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload" target="_blank" rel="noopener nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">無制限のファイルアップロード</font></font></a></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ユーザーがプロフィール写真をアップロードできる Web アプリケーション。画像だけでなく、あらゆるファイル タイプをアップロードできます。これを利用して、悪意のあるコードをアップロードすることで、Web アプリケーション サーバーを完全に制御できます。</font></font></td>
</tr>
<tr>
<td><a href="https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html" target="_blank" rel="noopener nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">安全でない直接オブジェクト参照 (IDOR)</font></font></a></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">アクセス制御の不具合などの欠陥と組み合わせると、他のユーザーのファイルや機能にアクセスするためによく使用されます。例としては、/user/701/edit-profile などのページを参照してユーザー プロファイルを編集することが挙げられます。 を</font></font><code>701</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">に変更できれば</font></font><code>702</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">、他のユーザーのプロファイルを編集できる可能性があります。</font></font></td>
</tr>
<tr>
<td><a href="https://owasp.org/www-project-top-ten/2017/A5_2017-Broken_Access_Control" target="_blank" rel="noopener nofollow"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">アクセス制御の不備</font></font></a></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">もう 1 つの例は、ユーザーが新しいアカウントを登録できるアプリケーションです。アカウント登録機能の設計が適切でない場合、ユーザーは登録時に権限昇格を実行する可能性があります。</font></font><code>POST</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">新しいユーザーを登録する際のリクエストについて考えてみましょう。このリクエストでは、データが送信されます。パラメータを操作して、</font><font style="vertical-align: inherit;">または</font><font style="vertical-align: inherit;">に変更</font></font><code>username=bjones&amp;password=Welcome1&amp;email=bjones@inlanefreight.local&amp;roleid=3</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">できるとしたらどうでしょうか</font><font style="vertical-align: inherit;">。実際のアプリケーションでは、このようなケースがあり、管理者ユーザーをすばやく登録して、Web アプリケーションの意図しない多くの機能にアクセスすることができました。</font></font><code>roleid</code><font style="vertical-align: inherit;"></font><code>0</code><font style="vertical-align: inherit;"></font><code>1</code><font style="vertical-align: inherit;"></font></td>
</tr>
</tbody>
</table>

## (2) フロントエンド、バックエンド
### ① フロントエンド
#### ◇ フロントエンド
クライアント側で実行される表示や、動的表示、入出力のUIを定義する部分

#### ◇ フロントエンドの要素
* タイトルやテキストなどのページの主要要素( HTML )
* すべての要素のデザインとアニメーション( CSS )
* ページの各部分が実行する機能( JavaScript )

#### ◇ フロントエンドの脆弱性
* クライアント側(客)で実行される攻撃になる。
  * XSS (ログイン画面の偽装等による認証情報の奪取やxssの攻撃によるセッションＩＤの摂取)
　* CSRF (重要実行の部分のところにデータを送り実行させる)
  * HTMLインジェクション
  * ファイルアクセス権のミスによる機密ファイルの参照
### ③ バックエンド
#### ◇ バックエンド
サーバ側で実行される。データの操作や、マシン操作が含まれている。

#### ◇ バックエンドで利用される言語、開発フレームワーク
* ruby(Ruby on Railsなどある)
* php(Laravelなど)
* python(Django,Flaskなど)
* javascript(NodeJS(※Web全体を作るよ))
#### ◇ バックエンドの脆弱性
* サーバ側(店員)で実行される攻撃になる
 * 認証、アクセス不備
 * 悪意のファイルのアップロード
 * コマンドインジェクション 
 * SQLインジェクション

※結果的にこれが具体的にこの脆弱性によってどのような(RCEや情報公開など)影響につながるかは、その攻撃される脆弱性や環境による。
## (3) よくあるミス
| **No.** | **Mistake**                                      |
| ------- | ------------------------------------------------ |
| 1.      | 無効なデータがデータベースに入力されることを許可する          |
| 2.      | システム全体に焦点を当てる                            |
| 3.      | 独自に開発したセキュリティ手法を確立する                 |
| 4.      | セキュリティを最後のステップとして扱う                   |
| 5.      | 平文のパスワードを保存する                              |
| 6.      | 弱いパスワードを作成する                               |
| 7.      | 暗号化されていないデータをデータベースに保存する            |
| 8.      | クライアントサイドに過度に依存する                       |
| 9.      | 楽観的すぎる                                          |
| 10.     | URL パス名を介して変数を許可する                        |
| 11.     | サードパーティのコードを信頼する                         |
| 12.     | バックドアアカウントをハードコーディングする                |
| 13.     | 未検証のSQLインジェクション                             |
| 14.     | リモートファイルのインクルージョン                      |
| 15.     | 安全でないデータの取り扱い                              |
| 16.     | データを適切に暗号化できない                            |
| 17.     | 安全な暗号化システムを使用しない                         |
| 18.     | レイヤー8（ユーザーや運用要因）を無視する                 |
| 19.     | ユーザーアクションの確認を怠る                          |
| 20.     | Webアプリケーションファイアウォールの設定ミス               |

