# Encyclopedia

The module generate sites from markdown files.

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

Remember, it is recommended to use virtualenv/venv for better isolation.

```Bash
pip install -r requirements.txt # alternatively try pip3
```
# Quickstart

Have to use module generator.py after python3. This is create site. After make change in /template/ or /articles/,site auto recreate. Example of script launch on Linux, Python 3.5:

```Bash
$ python3 generator.py
[I 180111 15:47:42 server:283] Serving on http://127.0.0.1:5500
[I 180111 15:47:42 handlers:60] Start watching changes
[I 180111 15:47:42 handlers:62] Start detecting changes
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
