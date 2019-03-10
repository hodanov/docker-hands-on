# Docker入門ハンズオン！
## 💻 Dockerの基本操作

### バージョンの確認

```
# 定番
$ docker -v
$ docker --version

# もっと詳しく見たい時
$ docker version
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

# コンテナから抜ける
Ctrl + P → Ctrl + Q
or
Ctrl + D

# コンテナのリスト表示
docker container ls
docker container ls -a

# コンテナの停止...XXXXは`CONTAINER ID`または`NAMES`
docker container stop {XXXX}

# コンテナの開始...XXXXは`CONTAINER ID`または`NAMES`
docker container start {XXXX}

# コンテナにコマンドを実行させる...XXXXは`CONTAINER ID`または`NAMES`
docker container exec -it {XXXX} ls -la

# コンテナへ入る...XXXXは`CONTAINER ID`または`NAMES`
docker container exec -it {XXXX} /bin/bash
```

## 💻 Dockerで開発環境を整える

### 💻 Dockerfileでイメージをつくる
