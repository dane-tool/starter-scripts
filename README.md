# Selenium scripts for automated web browsing

Emulating/automating web browsing behavior for watching streaming content and general internet browsing.

## Setup

1. Set up the Python environment/dependencies.

   ```
   conda create -n selscripts
   conda activate selscripts
   conda install -y -c conda-forge pip selenium geckodriver bs4 python-dotenv
   ```

   **Note:** You may choose to use a different webdriver than Firefox (`geckodriver`), e.g. for Chrome you would replace geckodriver with `python-chromedriver-binary`. See [Selenium docs](selenium) and do a web search for the drivers you can install with Anaconda.

2. Specify your desired webdriver and options in `scripts/driver.py`.

   For options, see https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.firefox.options or https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.options.
   
   **Note:** Command line arguments can also be specified with `driver_options.add_argument('--option argument')`.

3. Create a `.env` file at the root of this directory and write in your credentials.

   ```
   # Inside .env
   CURIOSITYSTREAM_EMAIL="your.email@address.com"
   CURIOSITYSTREAM_PASS="y0ur_p4ssw0rd"
   ```

   **Note:** That's a horrible password.

## Running

To run a specific script, you must run it as a module like so:

```
python -m scripts.streaming.curiositystream
```

## References

- [urllib]: https://docs.python.org/3/library/urllib.parse.html
  [urllib.parse Documentation][urllib] -- url parsing
- [selenium]: https://selenium-python.readthedocs.io/index.html
  [Selenium Python Documentation][selenium] -- browser automation
- [selenium-waits]: https://selenium-python.readthedocs.io/waits.html#explicit-waits
  [Selenium Explicit Waits Documentation][selenium-waits] -- often we need to wait for page content to load
- [bs4]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
  [BeautifulSoup4 Documentation][bs4] -- page parsing (unused so far)
