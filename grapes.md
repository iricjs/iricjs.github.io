---
layout: default
title: Iric Schoenfeld
description: "Project: Analyzing California wine grape prices using Python and Tableau"
---

# To start

I have a fondness for the wine industry, having previously worked for Constellation Brands in a finance/strategy role for their wine division. I've since consulted with several labels in Napa and try to keep a foot in the door to stay current.

Grape prices can be rather volatile so I thought it would be interesting to create a tool that tracks the spot price. Most transactions are private, typically made through a broker or with a handshake in the vineyard between grower and vintner. With that being said, www.winebusiness.com has an active classifieds where users can post listings for grapes and bulk wine.

# Pulling the data

To pull the data I enlisted the help of Python. Python is by far the best tool that I know of for automated data collection. With minimal code, I was able to create a tool that scraped grape listings from winebusiness.com and then exported the results to Microsoft Excel. The tool takes less than 30 seconds to run and could even be automated further by scheduling it to run daily without any user action.

<img src="/images/gui.JPG">

When ran the command line reads back:
>Listings found = 861
>Listings scraped = 861
>No errors detected

For technical users, the script uses the following libraries:
*   Beautiful Soup for scraping
*   Pandas for organizing the scraped data
*   Tkinter to create a basic GUI

The full script can be viewed and downloaded from <a href="https://github.com/iricjs/grapes">GitHub</a>

# Analyzing the data

I chose to analyze the data in Tableau for several reasons. First off, the data visualizations are more asthetically appealing. Secondly, the handoff of data from Python to Tableau is seamless and doesn't require the user to open Excel to refresh pivots or charts.

The first viz is a simple summary of the data. We can see how many tons are available and the average price.
<img src="/images/Tableau1.JPG">

The second viz was created to get a better understanding of price range. Grape prices for a single varietal will have a large range due to quality of various appellations, or growing regions.

We can see here that prices for Cabernet Sauvignon range from less than $1K per ton to over $6K per ton. We will dig into this more later.
<img src="/images/Tableau2.JPG">

The last viz showed that with such dramatic ranges it would be necessary to create a weighted average price per ton. Otherwise, the average price in the first viz would be misleading. In other words, the weighted average price will factor in how many tons are available at each price point.

Now we have a better view of price per ton by varietal. This graph would be the primary chart I would look at on a recurring basis to get an understanding of price.
<img src="/images/Tableau3.JPG">

The last image digs further into the Cab Sauv price range that we saw earlier. This shows us price by appellation and could give us insights to dig in further. For example, if I was a winemaker and saw a good price for a desired appellation we could then reach out for further info.
<img src="/images/Tableau4.JPG">

# Summary

This project shows that with a little coding on the front end we can save a lot of time down the road. This analysis can now be refreshed and reviewed daily with no additional work. This could be useful information for winemakers, growers, and brokers.

[back](./)
