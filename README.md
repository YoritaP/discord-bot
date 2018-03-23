# discord-bot
pythonで動くdiscord botの開発をしています。

### 下準備
Windows上でvirtualenvを使う例を紹介します。

Linuxなどでvirtualenvwrapperなどを使うのであればそのやり方に従ってください。

1. virtualenvなどでPython仮想環境を作成します。
2. Python仮想環境内でPythonパッケージをインストールします。
   実行するだけならrequirements.txt、開発もするならrequirements-dev.txtを指定します。

```bat
(ステップ1)
> cd <cloneしたgitリポジトリディレクトリ>
> py -3 -m venv .venv

(ステップ2)
> .venv\scripts\activate.bat
> pip install -r requirements.txt   (またはrequirements-dev.txt)
```

### 使い方
直下に`config.ini`を作成してください。  

```
# config.ini
[bitcoin]
rpc_name=name
rpc_pass=pass

[discord]
token=login_token
```

### 依存するPythonパッケージを変更したくなったら

実行時に必要なパッケージは`requirements.in`、開発時にだけ必要なものは`requirements-dev.in`に記載します。

該当するファイルを編集したら、pip-toolsを使用して`*.in`ファイルから`*.txt`ファイルを生成します。

```bat
(実行時用)
> pip-compile -o requirements.txt requirements.in

(実行時+開発時用)
> pip-compile -o requirements-dev.txt requirements.in requirements-dev.in
```
