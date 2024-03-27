#Vera! your local install paths for chrome & chromedriver are:
~/chrome/linux-123.0.6312.86/chrome-linux64/chrome
~/chromedriver/linux-123.0.6312.86/chromedriver-linux64

123.0.6312.86 is the appropriate chromedriver version for compatability on the latest stable chrome for testing.

#TODO: make the filepaths environment variables so the project is more redistributable. Or set up puppeteer in a build script to handle this!

install pipenv

#install associated dependencies:

python -m pipenv install

#run virtual environment:

python -m pipenv shell

#run main script:

python main.py

#todo:

scrape dynamic page content with selenium, running chrome headlessly

-install chromium and chrome driver

-install selenium

-run headlessly and pass html result into bs4 for use.
