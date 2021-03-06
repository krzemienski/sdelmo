# sdelmo
[![Build Status](https://api.travis-ci.org/elmoiv/sdelmo.svg?branch=master)](https://travis-ci.org/elmoiv/sdelmo)
[![Python version](https://img.shields.io/badge/python-3.6-blue.svg)](https://pypi.org/project/sdelmo/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f52faa974e2c42c3873839cab853b854)](https://www.codacy.com/manual/elmoiv/sdelmo?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=elmoiv/sdelmo&amp;utm_campaign=Badge_Grade)

Simple Soundcloud music downloader.
## *Module no longer works due to updates in soundcloud api mechanism*
## *Wait for a fix soon*

## Features
-   Download any public soundcloud audio file.
-   audio files can be downloaded with cover if you have [eyeD3](https://eyed3.readthedocs.io/).

## Installation
`sdelmo` requires Python 3.

Use `pip` to install the package from PyPI:

```bash
pip install sdelmo
```

Or, install the latest version of the package from GitHub:

```bash
pip install git+https://github.com/elmoiv/sdelmo.git
```

## Usage
```
from sdelmo import scdl

scdl('6aSX01kZxpetA85mf5R9Ezqs3ozjO2zc','https://soundcloud.com/lifeofdesiigner/desiigner-panda')
```

## How to get `client_id` (in case of expiry)

You can find client_id by searching through XHR requests:

![alt text](https://i.imgur.com/Xl3JnuP.png)

## Installing on Android (via [Termux](https://termux.com/))

Type these commands in termux:

-   `apt update && apt upgrade`
-   `pkg install clang python libxml2 libcrypt libxslt libiconv zlib`
-   `pip install sdelmo`

## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/sdelmo/issues) or send me a pull request.

## TODO
-   Gathering `client_id` automatically
