# -*- coding: utf-8 -*-
import requests

from hello import __version__


def main():
    print("Version %s of hello" %  __version__)
    print(requests.get('https://google.com/'))


if __name__ == '__main__':
    main()
