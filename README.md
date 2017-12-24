# breach_compilation_utils

Small utility class to manipulate more easily the 41Go login/pwd
breach. The script folder contains all the scripts using this module.

> Disclaimer: This module does not intent to be polished or clean, but
rather quick and dirty and used for testing purposes.

## Using it

The main usage is to iterate all login/passwords regardless
of where they are located in files. Examples:

```python

bc = BreachCompilation("BreachCompilation/data/")
for login, pwd in bc.iter_credentials():
    # Do whatever you want with the credentials
```

You can also look for the existence of a specific email and all
credentials associated.

```python

bc = BreachCompilation("BreachCompilation/data/")
if bc.email_exists("my_email@gmail.com"):
    for login, pwd in bc.iter_email("my_email@gmail.com"):
        print(login, pwd)
```

## Notes

As this module is made in python, its definitely slower at iterating files
than standard coreutils, ``grep`` and so on.