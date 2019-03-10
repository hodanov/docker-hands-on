# Docker入門ハンズオン！
## 💻 Dockerの基本操作

### バージョンの確認

```
# 定番
docker -v
docker --version

# もっと詳しく見たい時
docker version
```

### Dockerイメージとコンテナの基本

```
# イメージを探す
docker search python

# イメージの取得
docker image pull python:latest

# イメージの取得（バージョンを指定したい時）
docker image pull python:3.5

# イメージのリスト表示
docker image ls

# コンテナの実行
docker container run -it python:latest
# -iはdocker起動後にコンテナ側の標準入力を繋ぎっぱなしにするオプション
# -tは擬似端末を有効にするオプション
# -itでシェルに入ってコマンド実行などができるようになる。

# コンテナから抜ける
Ctrl + P → Ctrl + Q
or
Ctrl + D

# コンテナのリスト表示
docker container ls
docker container ls -a

# コンテナの停止...XXXXは`CONTAINER ID`または`NAMES`
docker container stop {XXXX}

# コンテナの起動...XXXXは`CONTAINER ID`または`NAMES`
docker container start {XXXX}

# コンテナにコマンドを実行させる...XXXXは`CONTAINER ID`または`NAMES`
docker container exec -it {XXXX} ls -la

# コンテナへ入る...XXXXは`CONTAINER ID`または`NAMES`
docker container exec -it {XXXX} /bin/bash

# コンテナの削除...XXXXは`CONTAINER ID`または`NAMES`
# -fは強制削除のオプション
docker container rm -f {XXXX}
```

## 💻 Dockerfileで開発環境を整える

### DockerfileでPythonイメージをつくる

```
# イメージのビルド
# docker image build -t {IMAGE_NAME}:{TAG} {PATH}
docker image build -t my_python:v1 .

# コンテナの起動
docker container run -dt --name my_python my_python:v1
# --nameでコンテナに名前付け
# -dはコンテナをバックグランドで起動しっぱなしにするオプション

# コンテナへADDしたPythonスクリプトを実行
docker container exec -it my_python python python_script.py
```

#### ボリュームのマウント

```
# ホストのディレクトリをボリュームとして、コンテナへマウントする
docker container run -dt --name my_python -v $(pwd):/code my_python:v1
```

## 💻 イメージの公開

### 作ったイメージをDocker Hubに登録

```
# docker image push [option] {REPOSITORY_NAME}:{TAG}
```

## 💻 運用管理向けコマンド

```
# コンテナの利用状況の取得
docker container stats

# コンテナのお掃除
# Dockerが自動で判断して、停止中のコンテナを吹き飛ばす
docker container prune

# イメージのお掃除
# Dockerが自動で判断して、起動中のコンテナと紐づいていないイメージを吹き飛ばす
docker image prune

# イメージ、ボリューム、ネットワークなど、全てお掃除
docker system prune
```
