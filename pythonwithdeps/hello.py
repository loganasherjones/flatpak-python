# -*- coding: utf-8 -*-

import requests


def main():
    print(requests.get('https://google.com').text)


if __name__ == '__main__':
    main()
