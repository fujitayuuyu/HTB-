# 1 ペネトレPCを使いやすくするために
## (1) ファイル構成の組織化について
適切な組織化(分類分け)で、目的のファイルが取りやすくなるし、調べやすくなるよー。

### ① ファイル組織化の例
ペネトレとかだと、ある程度作業手順があるよねこれを組織化すると
![image](https://github.com/user-attachments/assets/7e8c5c91-abd9-4ed9-b1a0-7a366e72f805)

こんな風に、調べやすくなりエラーとかも分かりやすくなるよ

## (2) ブックマークについて
使いやすいけど、機密情報やプライベートなリソースを含むリソースを保存するな！！

ブックマークのリストは、結局のところ第三者によって見られてしまう！！

→ だから、侵入テスト専用のアカウントを作る必要あるよ〜

そんでローカルに保存しろ

## (3) パスワードの管理について
### ① 注意すべき問題点
* 複雑なパスワードは、ユーザーが知っていて覚えられるコンテンツに関連付けられていることが多い?!

* パスワードは、再利用されることが多い！されなくてもパスワードの作成する個々のルールがある場合が多い！

* 安全なパスワード管理ソリューションを使用しなければ、パスワードを忘れたり、他のパスワード コンポーネントと混同したりするリスクが高い！！また、メモ等に記録しておくことがある！

### ② パスワード管理するなら
2要素認証を取り入れようって話。
1つのパスワードでログインした後、ワンタイムパスワードとかで認証してやればいいって話

## (4) アップデートと自動化
後で簡単に自動化できるように、すべてのリソースとそのソースをファイルに記録することを強くお勧め！！

新しい方法やテクノロジーを学習するときには、さらに多くのツール、実用的な説明、チート シートが見つかります。これらを記録しておき、エントリを最新の状態に保とう！！

## (5) メモメモ
### ① メモする内容
1. 新たに発見された情報
2. さらなるテストと処理のアイデア
3. スキャン結果
4. 作業ログ記録
5. スクリーンショット

#### ◇ 発見された情報
発見された情報とは、新しい IP アドレス、ユーザー名、パスワード、ソース コードなど、侵入テストの取り組みとプロセスに関連して特定された一般的な情報だよー

どーその情報を得たのかまで書いておくといいね！ レポートをその作業のディレクトリに保存したり、GitHubに置いたりでいいかなぁ！

ただGitHubは公開してしまう可能性があるから、後悔しないように、気をつける必要があります！

3も包括すると思う！
#### ◇  処理
簡単に言えばやった事だよー！！
今までどんなアプローチをしたか、してないアプローチはなんだとか、今後しないと行けないアプローチを把握出来るようになるよー！

評価の一環として調査する必要があるものはすべて書き留める習慣を身に付けよう！！！！！

Notion.soとか、Xmindがある！
Xmind使ってみよっかにゃ
#### ◇ スキャン等の結果
発見された情報と似た感じだけど、整理されていないのでいっぱい出るよー

個人的にはスキャン結果を貼り付けておくとか、ファイルとして保存がいいかな！

#### ◇ 作業ログ記録
ここで言うログ記録は、自分が何をしたかのログを残すことだよ！

侵入テスト中に第三者が会社を攻撃し、損害が発生した場合、その損害が当社の活動によるものではないことを証明できるよ！

##### プロンプトで日付の表示
Bashだったら.bashrcファイルの
PS1環境変数へ以下のスクリプトをの代入ですればいい
> `echo 'export PS1="-[\[$(tput sgr0)\]\[\033[38;5;10m\]\d\[$(tput sgr0)\]-\[$(tput sgr0)\]\[\033[38;5;10m\]\t\[$(tput sgr0)\]]-[\[$(tput sgr0)\]\[\033[38;5;214m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;196m\]\h\[$(tput sgr0)\]]-\n-[\[$(tput sgr0)\]\[\033[38;5;33m\]\w\[$(tput sgr0)\]]\\$ \[$(tput sgr0)\]"' >> ~/.bashrc`

##### コマンドログの出力
決まった形式でログを出力するようにしよう！
> 例: 年-月-時間-対象-実施事項.log

※実施事項に関しては特に、スキャンや偵察、エクスプロイトの実行時で分けて記録しよー！
##### scriptコマンドによるコマンドログの記録 in linux

> `script 2024-07-26-0721-hostA-recon.log`

※scriptコマンドは実行してから、exitして抜けるところまでを記録するよ！

##### Start-Transcriptコマンドによるコマンドログの記録 in Windows
	Ø `Start-Transcript -Path "C:\Pentesting\2024-07-26-0721-hostA-exploit.log`

#### ログのやつが使えない場合
パイプやリダイレクションほかのコマンドで頑張ってやる必要があるよ

上書きなら→「>」
追記なら    →「>>」

#### ◇ スクリーンショット
スクリーンショットは瞬間的な記録として機能し、得られた結果の証明を表すよ！

また短い操作なら録画してGIFをつくれるよー！

* スクリーンショット : Flameshot
* Gif録画 : Peek
	
# 1 os(侵入テスト用)のセットアップ
仮想マシンだったら、セットアップ終わった後必ず**スナップショットとろうね**！！！！！！
## (1) linux(ParrotOS Security)
Kaliは、前からあるけど、
ParrotOS Securityは、kaliに本体のセキュリティをしっかりしたヤツだよー！

### ① LVMによる暗号化
#### ◇ LVMとは
物理データ ストレージとコンピューターのオペレーティング システム (論理データ ストレージ領域とファイル システムを含む) の間にある追加の抽象化レイヤーのことだよ！
ほぼ全てのUNIX,linuxにあって、同じような仕組み的なものは、他のOSでもあるよ！
> このLVMを用いて、障害対処や物理データの暗号化を行うことができるよ。
##### こいつの目的
ハード ディスク障害からコンピューターを保護するために、RAID アレイ内の論理ボリュームの構成をサポートするよ！

#### ◇ 暗号化(Parrot OS Security)でのLUKS暗号化の手順(初めのOSインストール時に実行することになる。)
1. パーティションディスクのステップに行くと暗号化のためのパスフレーズを設定できるから、任意のパスワードマネージャを使用して保存しておく必要があるよ
2. パスフレーズを選択して確認すると、作成および構成されたすべてのパーティションの概要が表示され、パーティション分割ができるよ。
3. 構成が終わったらパーティション分割を終了し、変更内容を適用するよ。
4. オペレーティング システムのインストールが行われ、完了するとすぐに再起動されて、再起動後、システムのロックを解除するためのパスフレーズを要求するウィンドウが表示されるよ。
5. パスフレーズを正しく入力し、ログイン画面が出るよ！！

### ② UpdateとAPTパケットマネージャー
#### ◇ APTパケットマネージャとは、
オペレーティング システムをインストールしたので、これを最新の状態にする必要がある。そのためには、APTパッケージ管理ツールを使用する。Advanced Packaging Tool( APT) は、Debian オペレーティング システムに由来するパッケージ管理システムで、dpkg実際のパッケージ管理に使用されます。パッケージ管理にはパッケージ マネージャーが使用されます。つまり、プログラム パッケージを検索、更新、およびインストールできるよ！！

> パッケージソースは、「/etc/apt/sources.list」ディレクトリに保存されるよ
> (ParrotOS の場合は/etc/apt.sources.list.d/parrot.list)

#### ◇ Parrot OSのアップデート
> `sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y`

#### ◇ 必要な追加ツールのインストール
* tool.listを作成して一気にインストールすると楽だよ
> `sudo apt install $(cat tools.list | tr "\n" " ") -y`

* パッケージ等にない、githubにあるようなツールの場合(例：https://github.com/carlospolop/privilege-escalation-awesome-scripts-suiteからダウンロード)
> `git clone https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite.git`

### ③ Bashプロンプトをカスタマイズ
以下は、日付表示を行うプロンプトを適用するスクリプト

> ```
> #!/bin/bash
> ### Make a backup of the .bashrc file
> cp ~/.bashrc ~/.bashrc.bak
> ### Customize bash prompt
> echo 'export PS1="-[\[$(tput sgr0)\]\[\033[38;5;10m\]\d\[$(tput sgr0)\]-\[$(tput sgr0)\]\[\033[38;5;10m\]\t\[$(tput sgr0)\]]-[\[$(tput sgr0)\]\[\033[38;5;214m\]\u\[$(tput sgr0)\]@\[$(tput sgr0)\]\[\033[38;5;196m\]\h\[$(tput sgr0)\]]-\n-[\[$(tput sgr0)\]\[\033[38;5;33m\]\w\[$(tput sgr0)\]]\\$ \[$(tput sgr0)\]"' >> ~/.bashrc
> ```

### ④ VMの暗号化
VMwareでは、仮想自体を暗号化できるからそれもやるとより強固になるね

## (2) Windows
### ① 侵入テストでWindowsを利用する利点
* ほとんどのエンタープライズ環境に溶け込むため、物理的にも事実上も、疑わしいと思われにくくなる。
* Active Directory ドメイン上の他のホストをナビゲートして通信するのが簡単になります。SMB をトラバースして共有を利用するのも、この方法の方がはるかに簡単
* 最近だとWSLが利用できるようになったため、Linuxのコマンド実行等も簡単になった

### ② 今回の注意点
* システムを戦闘態勢に整えるために必要なコア コンポーネント (WSL, Visual Studio Code, Python, Git, and the Chocolatey Package Managerなど) を調べてインストールする。
* このプラットフォームを使用して侵入テスト機能を実行するため、ホストのセキュリティ設定の変更も必要になる。
* ほとんどのエクスプロイト ツールとコードは、エクスプロイト ツールとコードそのもので、注意しないとホストに害を及ぼす可能性があることに注意してください。インストールして実行する内容には注意してください。
* スキャン、エクスプロイト、ポストエクスプロイトのツールを隔離しないと、Windows Defender によって有害と判断された検出されたファイルとアプリケーションがほぼ確実に削除される！！

### ③ 構成するための各要件
#### ◇ ハードウェア要件
* 1GHz 以上で動作するプロセッサ。デュアルコア以上が理想的
* 最低 2G の RAM、4G 以上が理想
* 60G のハード ドライブ容量。これにより、OS と一部のツール用のスペースが確保されます。サイズは、ホストにインストールするツールの数によってことなる。

#### ◇ ソフトウェア要件
以下のURLから開発者VMをコピーするのが最適：https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/
既に構成されているもの
* Windows 10 バージョン 2004
* Windows 10 SDK バージョン 2004
* UWP、.NET デスクトップ、Azure ワークフローが有効になっている Visual Studio 2019 には、Windows Template Studio 拡張機能も含まれています。
* VSCode
* Ubuntu がインストールされた Windows Subsystem for Linux
* 開発者モードが有効

### ④ 構成手順
#### ◇ Windowsの実行ポリシーについて
| 実行ポリシー   | 説明                                                            | リスク/注意点                                                    |
|----------------|---------------------------------------------------------------------------------------------------------------------------|-------------------|
| **AllSigned**   | **すべてのスクリプトが信頼された発行元によって署名されている必要**があります。プロンプトが表示されることがあります。                  | 符号付きでも悪意のあるスクリプトを実行する可能性があります。                                            |
| **Bypass**      | **何もブロックされず、警告やプロンプトも表示されません**。大規模なアプリケーションや独自のセキュリティモデルを持つ構成に使用されます。 | 全くの無制限のため、悪意のあるスクリプトが実行されるリスクがあります。                                   |
| **Default**     | 既定の実行ポリシーを設定します。**Windows クライアントは Restricted、Windows サーバーは RemoteSigned **です。                     | 各プラットフォームに応じた適切な既定の制限が適用されます。                                               |
| **RemoteSigned**| **インターネットからダウンロードされたスクリプトには信頼できる発行者の署名が必要**です。**ローカルのスクリプトには署名は不要**です。     | 符号なしや悪意のある符号付きスクリプトが実行されるリスクがあります。                                    |
| **Restricted**  | 個々のコマンドは許可されますが、スクリプトの実行は許可されません。Windows クライアントの既定のポリシーです。                  | スクリプトの実行が全てブロックされるため、スクリプトによる自動化が制限されます。                         |
| **Undefined**   | 実行ポリシーが設定されていません。すべてのスコープで Undefined の場合は、Windows クライアントでは **Restricted**、Windows Server では **RemoteSigned** になります。 | 特定の実行ポリシーがないため、プラットフォームに応じた既定のポリシーが適用されます。                    |
| **Unrestricted**| 符号なしスクリプトも実行可能です。Windows 以外のコンピューターでは既定のポリシーです。ローカルイントラネット以外では警告が表示されます。 | 悪意のあるスクリプトが実行されるリスクが高まります。                                                     |
#####  実行ポリシーのスコープについて
| スコープ         | 説明                                                                                                      |
|------------------|---------------------------------------------------------------------------------------------------------|
| **MachinePolicy** | グループポリシーによってコンピューターのすべてのユーザーに対して設定されます。                                                             |
| **UserPolicy**    | グループポリシーによってコンピューターの現在のユーザーに対して設定されます。                                                               |
| **Process**       | 現在の PowerShell セッションのみに影響します。 実行ポリシーは環境変数 `$env:PSExecutionPolicyPreference` に保存され、セッション終了時に削除されます。 |
| **CurrentUser**   | 実行ポリシーは現在のユーザーのみに影響します。HKEY_CURRENT_USER レジストリ サブキーに格納されています。                                    |
| **LocalMachine**  | 実行ポリシーはコンピューターのすべてのユーザーに影響します。HKEY_LOCAL_MACHINE レジストリ サブキーに格納されています。                       |
#### ◇ 更新プログラムのインストール
管理者の Powershell ウィンドウを開き、次のコマンドを実行
1. システムの実行ポリシーをモジュールとスクリプトをダウンロード、ロード、実行できることを確認
> `Get-ExecutionPolicy -List`

2. UndefinedやDefault、Restrictedなどの実行ポリシーの場合、スクリプトの実行ができないので、現在のプロセスのみ実行ポリシーを制限なし(Unrestricted)に変更する。(プロセスがターゲットだと今回の開いているターミナルのみに適用され、設定が永続化しない!!)
> `Set-ExecutionPolicy Unrestricted -Scope Process`

3. 設定が適用されたか確認
> `Get-ExecutionPolicy -List`

4. PSWindowsUpdateをインストール及びインポートして更新を実行
> ```
> Install-Module PSWindowsUpdate 
> Install-Module PSWindowsUpdate
> Install-WindowsUpdate -AcceptAll
> ```

5. 完了したなら、再起動
> `Restart-Computer -Force`

#### 2. 追加のツールをインストール
##### Chocolateyパッケージマネージャーについて
ソフトウェア パッケージとスクリプトのインストールと依存関係を管理できる、無料でオープンなソフトウェア パッケージ管理ソリューション

LinuxのAPTパケットマネージャと同じようなものだよ
##### Chocolateyによるインストール
パワーシェルを開いて行う。
1. Chocolateyをダウンロードする。(パッケージ関連のものだから実行ポリシーをBypassにしているよ）
> `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))`

2. Chocolateyを更新してパッケージをインストールする。(定期的に再起動すると問題が発生しにくくなるよ)
> `choco upgrade chocolatey -y `

3. Chocolateyを使って追加で必要なツールをダウンロードする。
> `choco install python vscode git wsl2 openssh openvpn`

4. 環境変数PATHの変更を反映させる、利用しているプロンプトですぐにコマンドを利用できるようにするため。
> `RefreshEnv`

#### ◇ WSL2のインストールと実行
パワーシェルで実行
1. WSL2のインストール
> `choco install WSL2`

2. MicrosoftストアからWSL用のLinuxディストリビューションをインストール(kaliやubuntu、いろいろあるよ)

3. Powershellを開いて「bash」を実行しWSL2を利用する
> `bash`

#### ◇ セキュリティ構成とDefenderの変更
Windows Defender は、潜在的に有害であると判断されたものをスキャンして隔離または削除します。Defender が計画を台無しにしないように、ツールが確実に機能するように除外ルールを追加しよう！！
> `Add-MpPreference -ExclusionPath "C:\Users\your user here\AppData\Local\Temp\chocolatey\"`

##### ※Defenderから除外すべきツールフォルダの例
* `C:\Users\your user here\AppData\Local\Temp\chocolatey\`
* `C:\Users\your user here\Documents\git-repos\`
* `C:\Users\your user here\tools\`

ツールやスクリプトをさらに追加すると、除外対象をさらに追加する必要がある可能性があるよ

### ⑤ ツールインストールの自動化
パッケージ管理にChocolateyを利用するとコア ツールとアプリケーションの初期インストールを自動化するのが非常に簡単になるよ。

スクリプトの例
> ```
> # Choco build script
> 
> write-host "*** Initial app install for core tools and packages. ***"
> 
> write-host "*** Configuring chocolatey ***"
> choco feature enable -n allowGlobalConfirmation
> 
> write-host "*** Beginning install, go grab a coffee. ***"
> choco upgrade wsl2 python git vscode openssh openvpn netcat nmap wireshark burp-suite-free-edition heidisql sysinternals  putty golang neo4j-community openjdk
> write-host "*** Build complete, restoring GlobalConfirmation policy. ***"
> choco feature disable -n allowGlobalCOnfirmation
> ```

### ⑥ 残りのツールは、
他にもツールは、あるから、それらは、githubを使ってとってこい！！
> `git clone $URL`

### ⑦ 古いバージョンをインストールするのに利用できるツール
* MediaCreationTool.bat(https://gist.github.com/AveYo/c74dc774a8fb81a332b5d65613187b15)
* Microsoft Windows and Office ISO Download Tool(https://www.heidoc.net/joomla/technology-science/microsoft/67-microsoft-windows-and-office-iso-download-tool%EF%BB%BF)
* Rufus(https://rufus.ie/en_US/)

### ⑧ Windows 11 仮想を入れたときに起きた問題の対処
![image](https://github.com/user-attachments/assets/5d638135-b880-4e23-ba35-e27252dc0291)
microsoftからとれる仮想だと、デフォルトの状態で、Intel VT-X/EPTの使用が有効になっている

### ⑨ 対処
* Intel VT-Xを有効にする　⇒　いろいろ調べて実施したが、うまいこと有効にならない(supportはされているのは確認している)
ものが違うが、sufaceの人で同じようなことが起きていたらしくそこのアドバイスを用いたらできた。
> https://answers.microsoft.com/ja-jp/surface/forum/all/vt%E3%82%92%E6%9C%89%E5%8A%B9%E5%8C%96%E3%81%99/650e53f9-8850-44b2-a60b-d8b6dd226d23

* VMの仮想マシンの設定でIntel VT-Xの使用を無効にする　⇒　実行できたが、どのような問題が使用中に出るは、不明
VT-Xを無効にして使用すると、仮想マシン上でWSLが利用できない。そのためこの案はなし。

### ⑩ Intel VT-xを有効化した具体的な方法
https://answers.microsoft.com/ja-jp/surface/forum/all/vt%E3%82%92%E6%9C%89%E5%8A%B9%E5%8C%96%E3%81%99/650e53f9-8850-44b2-a60b-d8b6dd226d23

要約すると、hyper-vの機能を無効化してデバイスガードも無効化することで、デバイスガード等に利用されていたVT-xを解放してほかの処理につかえる（有効化）されるようだ
1. Hyper-Vを無効化(Powershellを使用)
> ```
> ①-1 EnterPrice, Pro editionの場合 -> 「windows機能の有効化または、無効化」からHyper-Vを無効化
> ①-2 home editionの場合 -> Disable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V-Hypervisor
> ② bcdedit /set hypervisorlaunchtype off   (共通して実行)
> ```
2. デバイスガードの無効化(cmdを使用)
> ```
> reg add HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard /v EnableVirtualizationBasedSecurity /t REG_DWORD /d 0 /f 
> reg add HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard /v RequireMicrosoftSignedBootChain /t REG_DWORD /d 0 /f 
> reg add HKLM\SYSTEM\CurrentControlSet\Control\DeviceGuard\Scenarios\HyperVisorEnforcedCodeIntegrity /v Enabled /t REG_DWORD /d 0 /f
> ```
3. 再起動

これで、Intel VT-xを有効化して、仮想マシン上でもWSLが利用できる

## (3) linuxにおけるちょっとしたハードニング！！(例でsshの強化)
### ① sshを強化する方法の例
* システムを最新にする
* Fail2banをインストールする
* SSHキーのみで作業する
* アイドルタイムアウト間隔を短縮する
* パスワードを無効にする
* x11転送を無効にする
* 別のポートを使用する
* ユーザーのSSHアクセスを制限する
* ルートログインを無効にする
* SSHプロトコル2を使用する
* SSHの2FA認証を有効にする


### ② システムの更新(システムを強化するための最初のステップだよ)
> `sudo apt update -y && sudo apt full-upgrade -y && sudo apt autoremove -y && sudo apt autoclean -y`

### ③ fail2banによる不正アクセスからの防御
具体的には、ログファイル(/var/log/secureとか)に記録される内容を監視して、何度も認証に失敗しているログや、
連続アクセスしているログを見つけると、ファイアーウォールを自動的に調整して、
接続元からの不正アクセスを禁止するよ！！

#### ◇ Fail2Banの使用
1. fail2banをダウンロード
> `sudo apt install fail2ban -y`
2. fail2banの設定をバックアップする(設定系のいじるやつとか、ソースコードは、しっかりバックアップしような、あとスナップショットもとっとこ）
> `sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.conf.bak`
3. fail2banの設定を変更する(例：sshに対して、3回失敗したら、4週間そのIPのアクセスをBANする)
> sudo vi /etc/fail2ban/jail.conf
> ```
> ...SNIP...
> # [sshd]
> enabled = true
> bantime = 4w
> maxretry = 3
> ```

##### Fail2Banの利点
sshの例で行くと、fail2ban はsshのログインと、２要素認証時の認証コードによる認証で3 回誤って入力した場合もIP アドレスも禁止すること！！

※sshd_configは、アプリケーションレベルの制御(**接続**ごとに許可される認証試行の最大回数を指定ぐらい)しかできないんだ。

### ④ OpenSSH設定の編集
1. 設定のバックアップを取る
> `sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak`

2. 設定を変更
> `sudo vi /etc/ssh/sshd_config`

#### ◇ sshの設定できる項目
| Settings                              | Description                                                                                                      |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------|
| **LogLevel VERBOSE**                  | SSH デーモンからのメッセージをログに記録する際に使用する冗長レベルを設定します。                                           |
| **PermitRootLogin no**                | root が SSH を使用してログインできるかどうかを指定します。                                                             |
| **MaxAuthTries 3**                    | 1 回の接続あたりの認証試行の最大回数を指定します。                                                                     |
| **MaxSessions 5**                     | ネットワーク接続ごとに許可されるシェル、ログイン、またはサブシステム (例: SFTP) セッションの最大数を指定します。                 |
| **HostbasedAuthentication no**        | rhosts または /etc/hosts.equiv 認証と成功した公開鍵クライアントホスト認証を組み合わせたホストベース認証を許可するかどうかを指定します。  |
| **PermitEmptyPasswords no**           | パスワード認証が許可されている場合に、パスワードが空のアカウントへのログインを許可するかどうかを指定します。                          |
| **ChallengeResponseAuthentication yes**| チャレンジレスポンス認証を許可するかどうかを指定します。                                                                 |
| **UsePAM yes**                        | 認証に PAM モジュールを使用するかどうかを指定します。                                                                   |
| **X11Forwarding no**                  | X11 フォワーディングを許可するかどうかを指定します。                                                                    |
| **PrintMotd no**                      | ユーザーが対話的にログインしたときに、SSH デーモンが /etc/motd を表示するかどうかを指定します。                               |
| **ClientAliveInterval 600**           | クライアントからデータが受信されなかった場合に、SSH デーモンがクライアントに応答を要求するメッセージを送信するまでのタイムアウト時間（秒単位）を設定します。 |
| **ClientAliveCountMax 0**             | SSH デーモンがクライアントからメッセージを受信せずに送信できるクライアント存続メッセージの最大数を設定します。                           |
| **AllowUsers <username>**             | このキーワードの後にスペースで区切られたユーザー名パターンのリストを指定できます。指定された場合、ログインはこれらのパターンに一致するユーザー名のみに許可されます。 |
| **Protocol 2**                        | より安全な新しいプロトコルの使用を指定します。                                                                            |
| **AuthenticationMethods publickey,keyboard-interactive** | ユーザーがアクセスを許可されるために正常に完了しなければならない認証方法を指定します。                                      |
| **PasswordAuthentication no**		| パスワード認証を許可するかどうかを指定します。|

### ⑤ 2要素認証の設定(例：パスフレーズとOTP)
2FAは、実装に必要な時間に比べて比較的高いセキュリティ標準を備えているため、認証方法として実証されているよ。
今回は、Android または iOS スマートフォンの認証アプリケーションとして、Google Authenticator を使用するよ。

#### ◇ PAMとは、
Linux プラグ可能認証モジュール(PAM) は、Linuxシステム管理者がユーザー認証方法を設定できるようにするライブラリ スイート。
設定ファイルを使用して、セキュリティ保護されたアプリケーションの認証方法を柔軟かつ集中的に切り替えることがきるよ。

つまり、PAMは、Linux用のいろんな各認証機能を提供するためのプラグインできるモジュールだよ。

#### ◇ 手順
1. Google Authenticator PAM モジュールをインストール
> `sudo apt install libpam-google-authenticator -y`

2. Google Authenticator PAMを実行(実行後、QRコードと秘密鍵が表示される。これを Google Authenticator アプリでQRコードをスキャンするか、秘密鍵を入力します。QR コードをスキャンするか秘密鍵を入力すると、スマートフォンに最初のOTP(6 桁の数字) が表示され、これを端末に入力して、スマートフォンと VPS の Google Authenticator を Google と同期して認証するよ)
> `google-authenticator`

※２の実行の際にスマートフォンを紛失した時に使用してログインするためのいくつかのemergency scratch codes( backup codes) を生成するので、これを安全に保存しよう！！

3. 二要素認証用のPAM 構成
> ```
> sudo cp /etc/pam.d/sshd /etc/pam.d/sshd.bak
> sudo vim /etc/pam.d/sshd
> ```

3.2 「@include common-auth」をコメントアウトし、ファイルの末尾に２つの新しい行を追加
> ```
> #@include common-auth
> auth required pam_google_authenticator.so
> auth required pam_permit.so
> ```

4. sshd_configの編集
> ```
> ...SNIP...
>
> AuthenticationMethods publickey,keyboard-interactive
> PasswordAuthentication no
> ```
※公開鍵認証方式を用いるから、公開鍵は、事前に作っとかなあかん

5. sshの再起動
> ` sudo service ssh restart`

6. ちゃんとできてるかSSH、SCPでアクセスして検証
