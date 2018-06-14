# israbbitmqup
Docker image to verify a rabbitmq cluster is up

Usage
-----
```bash
$ docker run --net=host gavind/israbbitmqup:latest --user user --password password --host my-rabbitmq.domain.com --port 15672
Accessing http://my-rabbitmq.domain.com:15672/api/aliveness-test/%2F ... response code 200
Rabbitmq at my-rabbitmq.domain.com:15672 is up!
```

Kubernetes
----------
Can be used as an `InitContainer` in Kubernetes, to verify if rabbitmq is up, before deploying a pod which depends on rabbitmq.
