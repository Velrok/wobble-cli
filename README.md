# wobble-cli

A command line interface to wobble.

It focusses on batch processing and complex tasks which are not or poorly supported by the web interface.

This is intended as a addition not a replacement. 

#usage

```
Wobble client.

Set the following environment variables:
WOBBLE_SERVER_URL <- optional
WOBBLE_USERNAME
WOBBLE_PASSWORD

Usage:
    wobble archive [-i <days>]

Options:
    -i --days-inactive=<days>   [default: 14]
```

# installation
```
git clone git@github.com:Velrok/wobble-cli.git <project-folder>
<project-folder>/install_dependencies.sh
ln -s <project-folder>/wobble_cli.py /usl/local/bin/wobble
```

test that everything worked by running

`wobble -h`


# dependencies

- python 2.7
	- pip (for easy dependency installation)
	- docopt
	- BeautifulSoup