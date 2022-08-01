
# Setup

Install brew if not already installed

`https://brew.sh/`

use brew to install pyenv

`brew install pyenv`

pyenv requires additional steps to ensure that your shell checks for python in your pyenv directory instead of the default system python. Follow the instructions in the link below, starting at step 2, for whatever shell your machine uses. The Apple silicon machines default to ZSH and not Bash.

`https://github.com/pyenv/pyenv#basic-github-checkout`

In order to successfully build Python on your machine, you will need to install some dependencies needed for the build to succeed:

`brew install openssl readline sqlite3 xz zlib`

Then, we can build and install Python:

`pyenv install 3.9.9`

We should update pip, Python's dependency manager:

`pip install --upgrade pip`

Add the following `.zprofile` and reload your shell, either by `source .zprofile` or by opening a new window:

`export LDFLAGS="-I/opt/homebrew/opt/openssl/include -L/opt/homebrew/opt/openssl/lib"`

Now pull the repo and install it
```
cd ~
git clone git@github.com:zriddle/scriptps.git
cd scriptps/py-applescript
python setup.py install
cd ..
python setup.py install
```

# CLI Usage

## Setup

Setup the `config.ini` file to point to the right places
