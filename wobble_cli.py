"""Wobble client.

Set the following environment variables:
WOBBLE_SERVER_URL <- optional
WOBBLE_USERNAME
WOBBLE_PASSWORD

Usage:
    wobble archive [-i <days>]

Options:
    -i --days-inactive=<days>   [default: 14]
"""
from __future__ import with_statement
from docopt import docopt
from os import environ

import sys
# add wobble lib
sys.path.append("./libs/wobble-client-python/")

from wobble import WobbleService


def enforce_credentials():
    if 'WOBBLE_USERNAME' not in environ:
        print "please configure a username as WOBBLE_USERNAME environment variable"
        sys.exit(1)
    if 'WOBBLE_PASSWORD' not in environ:
        print "please configure a password as WOBBLE_PASSWORD environment variable"
        sys.exit(1)


def archive_topics(days):
    try:
        wobble_service = WobbleService(api_endpoint=environ['WOBBLE_SERVER_URL'])
    except KeyError:
        wobble_service = WobbleService()

    with wobble_service.connect(environ['WOBBLE_USERNAME'],
                                environ['WOBBLE_PASSWORD']) as service:
        topics = service.topics_list()
        for topic in topics['topics']:
            print topic['max_last_touch']


if __name__ == '__main__':
    args = docopt(__doc__)
    enforce_credentials()
    if args['archive']:
        archive_topics(args['--days-inactive'])
