# Python Namespace Package
This is a repo demonstrating how to distribute multiple namespace packages with dependencies between them.
The main package `libtest` installs the executable `libtestmain` which optionally depends on `libtest_foo` and `libtest_bar`.

## Setup
```bash
git clone https://github.com/Sinacam/py-ns-package
cd py-ns-package
pip install ./libtest
```

Optionally, install any of
```bash
pip install ./libtest_foo
pip install ./libtest_bar
```

## Run
```bash
libtestmain
```