# Tech-Circle 機械学習を利用したアプリケーション開発をはじめよう(ハンズオン)

URL: [http://techcircle.connpass.com/event/13901/](http://techcircle.connpass.com/event/13901/)

Requiremants
---

* Docker
* Docker-compose

Usage
---

```
$ docker-compose build base
$ docker-compose run base
```

```
         $ source /opt/miniconda3/envs/ml_env/bin/activate ml_env
 (ml_env)$ ipython profile create nbserver
 (ml_env)$ cd scikit-learn-notebook
 (ml_env)$ ipython notebook --profile=nbserver &
```

※起動後、miniconda3へのパスを通す為、下記を実行して下さい。

```
# . /etc/profile.d/conda.sh
```

# qiita手順との相違点

URL: [http://qiita.com/icoxfog417/items/950b8af9100b64c0d8f9](http://qiita.com/icoxfog417/items/950b8af9100b64c0d8f9)
* 複数Pythonバージョンを想定していない為、pyenv未インストール
* miniconda3のインストール先 -> /opt/miniconda3
