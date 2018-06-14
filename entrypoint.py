import argparse

import requests
import time


def create_parser():
    parser = argparse.ArgumentParser(description='Verify rabbitmq is up.')
    parser.add_argument('--attempts', type=int, dest='attempts', default=20,
                        help='Total number of attempts before failing.')
    parser.add_argument('--sleep', type=int, dest='sleep', default=1,
                        help='Number of seconds to wait between attempts.')
    parser.add_argument('--user', dest='user', required=True,
                        help='Rabbitmq credentials - user.')
    parser.add_argument('--password', dest='password', required=True,
                        help='Rabbitmq credentials - password.')
    parser.add_argument('--host', dest='host', required=True,
                        help='Rabbitmq management host.')
    parser.add_argument('--port', type=int, dest='port', required=True,
                        help='Rabbitmq management port.')
    return parser


def check_rabbitmq(host, port, user, password, attempts, sleep):
    rabbitmq = '{}:{}'.format(host, port)
    for i in range(1, attempts):
        r = requests.get('http://{}/api/aliveness-test/%2F'.format(rabbitmq), auth=(user, password))
        print('Accessing http://{}/api/aliveness-test/%2F ... response code {}'.format(rabbitmq, r.status_code))
        if r.status_code == 200:
            print('Rabbitmq at {} is up!'.format(rabbitmq))
            return
        time.sleep(sleep)
    print('FAIL: Unable to connect to Rabbitmq {} after {} attempts.'.format(rabbitmq, attempts))
    exit(1)


if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    check_rabbitmq(**vars(args))
