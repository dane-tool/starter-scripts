# Behavior Scripts

Emulating/automating web browsing behavior for watching streaming content and general internet browsing.

## Setup

1. Set up the Python environment/dependencies.

```
conda create -n behavior
conda activate behavior
conda install -y -c conda-forge pip selenium geckodriver bs4 python-dotenv
```

**Note:** You may choose to use a different webdriver than Firefox (`geckodriver`), e.g. for Chrome you would replace geckodriver with `python-chromedriver-binary`. See [Selenium docs](selenium) and do a web search for the drivers you can install with Anaconda.

1. Create a `.env` file at the root of this directory and write in your credentials.

```
# Inside .env
CURIOSITYSTREAM_EMAIL="your.email@address.com"
CURIOSITYSTREAM_PASS="y0ur_p4ssw0rd"
```

**Note:** That's a horrible password.

## Running

```
python scripts/streaming/curiositystream.py
```

If you want to further play with the script, comment out the last few lines of the file, and run it in interactive mode with the `-i` flag.

```
python -i scripts/streaming/curiositystream.py
```

## References

- [urllib]: (https://docs.python.org/3/library/urllib.parse.html)
  [urllib.parse Documentation][urllib] -- url parsing
- [selenium]: (https://selenium-python.readthedocs.io/index.html)
  [Selenium Python Documentation][selenium] -- browser automation
- [selenium-waits]: (https://selenium-python.readthedocs.io/waits.html#explicit-waits)
  [Selenium Explicit Waits Documentation][selenium-waits] -- often we need to wait for page content to load
- [bs4]: (https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  [BeautifulSoup4 Documentation][bs4] -- page parsing (unused so far)
