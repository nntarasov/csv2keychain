# сsv2keychain #
[![PyPI](https://img.shields.io/badge/pypi-v0.1.3-blue.svg)](https://pypi.python.org/pypi/cmdline-csv2keychain/0.1.3)
[![Python](https://img.shields.io/badge/python-3.4-green.svg)](https://pypi.python.org/pypi?name=cmdline-csv2keychain&version=0.1.0&:action=display)

## About ##

Small command-line tool for adding exported credentials (login/password pairs) from Chrome to the macOS keychain

**macOS 10.12.3 Sierra** tested

## Installing ##
You can install the package via *pip*
```bash
$ pip3 install cmdline-csv2keychain
```

## Preparing credentials from Chrome ##

1. To use this tool you should manually export credentials from Google Chrome into *.csv* file. In the browser, switch to  ```chrome://flags/#PasswordExport``` and enable option ```#password-import-export```.

2. Reload Chrome

3. Go to ```chrome://settings-frame/passwords```, click ```Export``` and save the ```.csv``` file in any convinient location

## How to use ##

```bash
$ csv2keychain [path.csv] [-u] [-s]
```

* ```-u``` - update existing password for every account in keychain, if any
* ```-s``` - display credentials on the screen during the process

## Example ##
```bash
$ csv2keychain ~/Desktop/credentials.csv -s
```

Now your Chrome passwords are available for Safari & other apps :)
