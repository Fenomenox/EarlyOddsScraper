<h1 align="center">
  Soccer Odds Scraper
  <br>
</h1>

<h4 align="center">
  Odds movement(Asian Handicaps) from all major leagues' matches from the past week, from http://bf.spbo1.com/
</h4>

# Description
Perhaps the only publishable part of the betting odds arbitrage project, this code lets the user scrape data that is already gathered by http://bf.spbo1.com/. The site documents the odds movement quite well, but only allows users to access odds from matches that took place within the last seven days

Having compared the data gathered from http://bf.spbo1.com/ to the ones directly scraped from the source(the bookies),I am confident that the data from http://bf.spbo1.com/ is accurate. The method to scrape from the source requires authentification, hence it won't be published. If you decide to scrape it directly from the bookies anyway for more complete data(other odds), make sure you know how to bypass detection.

# Prerequisite
python 3<br>
selenium chrome driver

# How To Use
1. clone repository
2. `pip install -r requirements.txt`
3. install chrome driver for selenium and add it to path
3. let it run
4. locate the excel file that stored the data
