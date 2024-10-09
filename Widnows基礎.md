# 1 Windows OSの導入

## (1) Windows 10までのバージョン番号
| オペレーティング システム名                    | バージョン番号 |
|--------------------------------|-------------|
| Windows NT4                    | 4.0         |
| Windows 2000                   | 5.0         |
| Windows XP                     | 5.1         |
| Windows Server 2003, 2003 R2    | 5.2         |
| Windows Vista, Server 2008      | 6.0         |
| Windows 7, Server 2008 R2       | 6.1         |
| Windows 8, Server 2012          | 6.2         |
| Windows 8.1, Server 2012 R2     | 6.3         |
| Windows 10, Server 2016, Server 2019 | 10.0        |

* 以下のコマンドで確認できる
> ```
> ◇ PowerShell
> Get-WmiObject -Class win32_OperatingSystem | select Version,BuildNumber
> 
> ◇ Cmd(DOS)
> systeminfo
> ```

* Windows の多くのバージョンは現在「レガシー」とみなされ、サポートされなくなりました。組織では、重要なアプリケーションをサポートするため、または運用上や予算上の懸念から、さまざまな古いオペレーティング システムを実行していることがよくあります。評価者は、バージョン間の違いと、各バージョンに固有のさまざまな構成ミスや脆弱性を理解する必要がある。

## (2) Windowsへのリモートアクセス
最も一般的なリモート アクセス テクノロジには、次のものがありますが、これらに限定されない。

* 仮想プライベートネットワーク (VPN)???リモートアクセスなのか
* セキュア シェル (SSH) : tcp/22
* ファイル転送プロトコル (FTP) : tcp/20,21
* 仮想ネットワークコンピューティング (VNC) : tcp/5900以降
* Windows リモート管理 (または PowerShell リモート処理) (WinRM) 
> ```
> ◇ windows 7以降
> WinRM HTTP : tcp/5985 , WinRM HTTPS : tcp/5985
>
> ◇ windows 7以前
> WinRM HTTP : tcp/80 , WinRM HTTPS : tcp/443
> ```
* リモート デスクトップ プロトコル (RDP) : tcp/3389

### ① RDPによるWindowsへのアクセス
* Windows : デフォルトで搭載のRDPアプリケーションを利用
* Linux : xfreerdpを利用
> ```
> xfreerdp /v:$IP /u:$USER /p:$PASS
