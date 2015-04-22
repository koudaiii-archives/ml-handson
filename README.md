Tech-Circle 機械学習を利用したアプリケーション開発をはじめよう(ハンズオン)
---

* [Techcircle](http://techcircle.connpass.com/event/13901/)

Requiremants
---

* [Docker](http://docs.docker.com/installation/mac/)
* [Docker-compose](http://docs.docker.com/compose/install/)

Install
---

* Let's git clone This Repository

```
$ docker-compose up -d server
```

* open http://$(boot2docker ip 2>/dev/null):8888/
* open http://$(boot2docker ip 2>/dev/null):3000/

Enter the Container
---

* check process

```
$ docker-compose ps
Name            Command       State           Ports
------------------------------------------------------------------
mlhandson_server_1   /root/server.sh   Up    0.0.0.0:3000->3000/tcp, 0.0.0.0:8888->8888/tcp
```

* exec

```
$ docker exec -it mlhandson_server_1 /bin/bash
[root@9724e3015c4e /]# source /opt/miniconda3/envs/ml_env/bin/activate ml_env
```

Stop docker
---

```
$ docker-compose stop server
```


qiita手順との相違点
---

* [Pythonで機械学習アプリケーションの開発環境を構築する](http://qiita.com/icoxfog417/items/950b8af9100b64c0d8f9)
* 複数Pythonバージョンを想定していない為、pyenv未インストール
* miniconda3のインストール先 -> /opt/miniconda3

develop
---

```
$ docker-compose build developbase
$ docker-compose build developserver
```
