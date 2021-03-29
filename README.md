# WebsiteAnalyzer

## Description
Website Analyzer, which analyse the following things

* The title of the web site
* The HTML version being used by the web site
* Identify login forms in the web site?
* Determine distinct, external links and there reachability.


## Installation

* git clone git@github.com:nabilshafi/WebsiteAnalyzer.git
* go to project directoy
* for install the dependencies run `pipenv install` 
* run `pipenv shell` for running the environment
* run `python web_analyzer.py https://www.facebook.com` for running the project

# Code Structure

* The project is comprised of 
  * `web_analyzer.py`: Includes functions to gather link, identify forms and html version etc.
  * `test.py`: Includes test for the above mentioned functionality


# Dependencies

Beautifulsoup used for scrapping the web page.
Validator used validate the correct url.
Urlparse and urllib used to parse and accessing the url

There are alternatives available but I found them easy to use.

# Challenges

* Html versions: Identifying the html version was one of the challenge because there is no function to read doctype tag.
* Login Form: Classification of a website containing the login form was another challenge.

Ran the Web Analyzer on several different websites and manually matched them in order to verify the results. 
