# Django-Docker

## ■チャレンジDocker本P288~を参考に「Django＋ポスグレ」環境を準備

このリポジトリをclone後に以下のコマンドを叩く
```
docker-compoe run web django-admin.py startproject <プロジェクト名> .
※プロジェクト名は「config」が一般的
```

プロジェクトフォルダが作成されたら以下を実施
```
cd <プロジェクト名> 
```

フォルダ内にある`setings.py`を以下の様に修正する。  
１）DBの設定を書き換える  
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'django',
        'HOST': 'db',
        'PORT': 3306,
    }
}
```
２）ALLOWD_HOSTSの設定を書き換える  
※どのホストやIPアドレスからのアクセスを許可するか設定する項目。  
環境によってはlocalhostを指定しておかないと開発環境でもアクセス拒否が起きる  
場合があるので念のため追加しておく。  
```
ALLOWED_HOSTS = ['localhost']
```

### 【コンテナ立ち上げ、動作確認】
下記コマンドを実行してイメージ作成、コンテナ立ち上げを実施。  
```
docker-compose up -d
```

シェルに入ってライブラリが実行できることを確認  
```
■シェルの立ち上げ
docker-compose exec <サービス名> bash
※環境によっては「/bash」「/bin/bash」だったりする
※サービス名はdocker-composeで定義しているサービス名

■ライブラリの実行確認
>python3
>import tensorflow, keras
```

その後`http://localhost:8000`にアクセスしてページの表示を確認。  





## ■（補足）機械学習、Django開発に必要なライブラリ
requirements.txtに記載されている内容

```
１）機械学習に必要なライブラリ    
tensor2tensor==1.11.0
tensorboard==1.13.1
tensorboardcolab==0.0.22
tensorflow==1.13.1
tensorflow-estimator==1.13.0
tensorflow-hub==0.4.0
tensorflow-metadata==0.13.0
tensorflow-probability==0.6.0
Keras==2.2.4
Keras-Applications==1.0.7
Keras-Preprocessing==1.0.9
keras-vis==0.4.1

２）G検定サイトで使用したライブラリ    
Django==2.0.0
django-allauth==0.39.1
PyMySQL==0.7.11
dj-database-url==0.4.2
dj-static==0.0.6
gunicorn==19.9.0
boto3==1.4.8
botocore==1.8.7
mysqlclient==1.3.7
requests==2.6.0
```
