"""Wobble client.

Usage:
    wobble archive [--days-inactive=<days> | -i <days>]

Options:
    -i --days-inactive [default: 14]
"""

from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__)
    print args
