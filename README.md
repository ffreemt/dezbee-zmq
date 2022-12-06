# dezbee-zmq
[![pytest](https://github.com/ffreemt/dezbee-zmq/actions/workflows/routine-tests.yml/badge.svg)](https://github.com/ffreemt/dezbee-zmq/actions)[![python](https://img.shields.io/static/v1?label=python+&message=3.8%2B&color=blue)](https://www.python.org/downloads/)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/dezmq.svg)](https://badge.fury.io/py/dezmq)

[de|ez|dz]bee via zmq (zmq.REP)

## python 3.8 only

## Pre-install
Refer to litbee for implementation details
* fasttext
  * `pip install fasttext` or `pip install fasttext*whl`
* pycld2, PyICU
  * e.g. `poetry run pip install pycld2-0.41-cp38-cp38-win_amd64.wh PyICU-2.9-cp38-cp38-win_amd64.whl` 
* polyglot fix:
  * `poetry run pip install -U git+https://github.com/aboSamoor/polyglot.git@master` or
  *  `pip install artifects\polyglot-16.7.4.tar.gz` (modified cloned polyglot: futures removed from requirements.txt)

## Install it

```shell
pip install dezmq
# pip install git+https://github.com/ffreemt/dezbee-zmq
# poetry add git+https://github.com/ffreemt/dezbee-zmq
# git clone https://github.com/ffreemt/dezbee-zmq && cd dezbee-zmq
```

## Use it
DEZMQ_HOST (default local) and  DEZMQ_PORT (default 5555)
```bash
dezmq

```
