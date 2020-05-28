---
layout: default
title: Iric Schoenfeld
description: "Project: Analyzing California wine grape prices using Python and Tableau"
---

# To start

I have a passion for the wine industry, having previously worked for Constellation Brands in a finance/strategy role in their wine & spirits division. I've since consulted with several labels in Napa and try to keep a foot in the door to stay current.

# A note on wine grape prices
Grape prices can be rather volatile so I thought it would be interesting to create a tool that attempts to track the spot price with publicly available data. Most transactions are private, typically made through a broker or with a handshake in the vineyard between grower and vintner. With that being said, <a href="https://www.winebusiness.com/">www.WineBusiness.com</a> has an active classifieds where users can post listings for grapes and bulk wine.

# Pulling the data

To pull the data I enlisted the help of Python. Python is by far the best tool that I know of for automated data collection. With minimal code, I was able to create a tool that scraped grape listings from winebusiness.com and then exported the results to Microsoft Excel. The tool takes less than 30 seconds to run and could even be automated further by scheduling it to run daily without any user action.

<img src="/images/gui.JPG">

When ran the command line reads back:

> Listings found = 861
> Listings scraped = 861
> No errors detected

For technical users, the script uses the following libraries:
*   Beautiful Soup for scraping
*   Pandas for organizing the scraped data
*   Tkinter to create a basic GUI

The full script can be viewed and downloaded from <a href="https://github.com/iricjs/grapes">GitHub</a>

# Analyzing the data

I chose to analyze the data in Tableau for several reasons. First off, the data visualizations are more aesthetically appealing. Secondly, the handoff of data from Python to Tableau is seamless and doesn't require the user to open Excel to refresh pivots or charts.

## Insight 1
The first viz is a simple summary of the data. We can see how many tons are available and the average price.

<img src="/images/Tableau1.JPG">

## Insight 2
The second viz gives us a better understanding of price range. Prices for a single varietal will have a large range due to quality of various appellations, or growing regions.

We can see here that prices for Cabernet Sauvignon range from less than $1K per ton to over $6K per ton. We will dig into this more later.

<img src="/images/Tableau2.JPG">

## Insight 3
The prior viz showed us that with such dramatic ranges it would be necessary to create a weighted average price per ton. Otherwise, the average price in the first viz would be misleading. In other words, the weighted average price will factor in how many tons are available at each price point.

Now we have a better view of price per ton by varietal.

<img src="/images/Tableau3.JPG">

## Insight 4
The last view dives further into the Cab Sauv price range that we saw earlier. This shows us price by appellation and could provide valuable insight. For example, if I was a winemaker and saw a good price for a desired appellation we could then reach out for further info.

<img src="/images/Tableau4.JPG">

All of these visualizations can be arranged on a single dashboard for quick daily viewing.

# Summary

This project shows that with a little coding on the front end we can save a lot of time down the road. By adding trend analysis over time, we could get a better understanding of the overall direction of the market. This could be useful information for winemakers, growers, and brokers.

[back](./)
