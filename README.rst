====================
сsv2keychain utility
====================
 
About
-----

Small tool for adding exported credentials from Chrome to the macOS keychain

Preparing credentials from Chrome
---------------------------------

To use this tool you should manually export credentials from Google Chrome into *.csv* file
In the browser, switch to *chrome://flags* and enable function *#password-import-export*
Then reload Chrome

Go to *chrome://settings/passwords*, click *Export* and save the *.csv* file in any convinient location

How to use
----------

* $ csv2keychain [path.csv] [-u] [-s]*

* *-u* - update existing password for every account in keychain, if any
* *-s* - display credentials on the screen during the process

Example
-------
* $ csv2keychain ~/Desktop/credentials.csv -s*

Now your Chrome passwords are available for Safari :)