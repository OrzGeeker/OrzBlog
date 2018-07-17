# OrzBlog

Python Flask Powered Blog


## Install the Elasticsearch Service

The Search module need Elasticsearch been installed

Use apt install Elasticsearch：

```
$ sudo apt-get update && sudo apt-get install elasticsearch
```

Maybe you should Change Config Option in file: `/etc/elasticsearch/elasticsearch.yml`


Enable Elasticsearch service start when system boot:

```
$ sudo systemctl enable elasticsearch
```


## Install Redis

The Redis service support the task queue function for blog


## How make this blog to real

learn from site: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

And the corresponding course by the author is: https://courses.miguelgrinberg.com/
