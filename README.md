# сsv2keychain #
[![PyPI](https://img.shields.io/badge/pypi-v0.1.3-blue.svg)](https://pypi.python.org/pypi/cmdline-csv2keychain/0.1.3)
[![Python](https://img.shields.io/badge/python-3.4-green.svg)](https://pypi.python.org/pypi?name=cmdline-csv2keychain&version=0.1.0&:action=display)

## About ##

Small command-line tool for adding exported credentials (login/password pairs) from Chrome to the macOS keychain.

**Note**: As of macOS High Sierra (`v10.13`) Safari is able to import bookmarks, history and passwords from Chrome and Firefox: https://support.apple.com/guide/safari/import-bookmarks-history-and-passwords-ibrw1015/mac.

The passwords are stored in the (iCloud) keychain. It is therefore not necessary to use `csv2keychain` for this use case, especially since the tool is not able to import to the iCloud keychain (see [#9](https://github.com/nntarasov/csv2keychain/issues/9)).

## Installing ##
You can install the package via *pip*.
```bash
$ pip3 install cmdline-csv2keychain
```

## Preparing credentials from Chrome ##

1. To use this tool you should manually export credentials from Google Chrome into *.csv* file. In the browser, switch to  ```chrome://flags/#PasswordExport``` and enable option ```#PasswordExport```. 
*UPD: seems that last versions of Chrome enables this feature by default. So you can omit this step*.

2. Reload Chrome

3. Go to ```chrome://settings/passwords```, click ```Other actions``` button (three dots, to the right of ```Saved Passwords``` text), then click ```Export``` and save the ```.csv``` file in any convinient location.

## How to use ##

```bash
$ csv2keychain [path.csv] [-u] [-s]
```

* ```-u``` - update existing password for every account in keychain, if any
* ```-s``` - display credentials on the screen during the process

## Example ##
```bash
$ csv2keychain ~/Desktop/Chrome\ Passwords.csv -s
```

Now your Chrome passwords are available for Safari & other apps. :)
