Title: Computational Investing
Date: 2012-10-29
Tags: coursera, investing
Slug: computational-investing
Author: Snehasish
Summary: Computational Investing from Coursera

After the completion of the ["Computing for Data Analysis"](http://www.snehasish.net/blog/post.php?filename=cG9zdHMvMjAxMi0wOS0yNC1MZWFybmluZyBSLm1k) course, I wanted to take another course from Coursera. Looking around, I found "Computational Investing" to be a suitable candidate due to my recent interest in stock markets (fueled by my conversations with [Sudipta Das](tarmackisser.blogspot.in)), the fact that portfolio managers are users of multiple monitor setups with pretty graphs everywhere, and the fact that the course started only a week back. The [course](https://www.coursera.org/course/compinvesting1) is taught formally at Georgia Tech by Tucker Balch. The coursera version is split into 2 parts, with the first part of length 8 weeks. Part 1 should culminate in building a stock market simulator in Python (using [QSTK](http://wiki.quantsoftware.org/index.php?title=QuantSoftware_ToolKit)). All software is supported on Mac and Ubuntu. I'll be taking notes as usual which I guess will mostly be stock market related jargon.

### Jargon
1. ETF = Electronically Traded Funds
2. Two and Twenty = 2% of total assets and 20% of return (in relation to Hedge Fund incentives for Portfolio Managers)
3. Back Test = Testing a simulation strategy
4. Risk can be defined as standard deviation of return (volatility of the fund)
5. Risk can also be defined as draw down ( by how much the portfolio went down when it did)
6. Sharpe Ratio = Assessment of performance of the investment with respect to risk. Higher values better
7. Portfolio = Group of ETF's managed by a person. Picking which stocks to invest in is a delicate task. Sharpe ratio analyses the risk to reward ratio. It's probably a good idea to combine ETFs to obtain a high Sharpe ratio (>2) so that there is high reward for low risk.
8. Paper Trading = Simulated trading on pen and paper (spreadsheets).
9. Order Format = (Symbol,Buy/Sell,Market/Limit,Shares,[Price]) - The price is only required if it is a Limit Order. The limit order type ensures that the order doesn't execute unless the limit condition is met.
10. Order Book = The order book for a symbol lists the asking price and the bid price offered by traders.
11. Spread = Difference between the highest bid price and the lowest ask price for a share. (Spread for frequently traded shares is low)
12. Short Selling = Betting on the fact that the price of shares will go down, borrow shares and sell them, wait for price to fall and return shares to owner. 
13. Arbitrage = Monitoring several exchanges for overlapping spread. Leads to price equity across different markets.
14. Market Cap = No. of shares x Price per share
15. Intrinsic Value = Sum of GP series of dividend and the discount rate.
16. CAPM = Capital Assets Pricing Model. Tries to find the relation between the stock under scrutiny and the market.

### Setting up QSTK

Setting up QSTK is [well explained in the wiki](http://wiki.quantsoftware.org/index.php?title=QSToolKit_Installation_Guide_Ubuntu) and is easily done on Ubuntu. In order to use Sublime Text 2 and its own build system shortcut, add the variables defined in local.sh (present in QSTK root) to the Python.sublime-build json as an env array. The file would now look like this:

	{
		"cmd": ["python", "-u", "$file"],
		"file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
		"selector": "source.python",

	    "env":
	    {
	        "PATH": "/usr/lib/lightdm/lightdm:/usr/local/sbin:/usr/local/bin:/home/ska124/QSTK/Bin",
	        "PYTHONPATH": ":/home/ska124/QSTK:/home/ska124/QSTK/Bin:/usr/local/lib/NAG/",
	        "QS": "/home/ska124/QSTK",
	        "QSDATA": "/home/ska124/QSTK/QSData",
	        "HOSTNAME": "Qosmio",
	        "QSDATAPROCESSED": "/home/ska124/QSTK/QSData/Processed",
	        "QSDATATMP": "/home/ska124/QSTK/QSData/Tmp",
	        "QSBIN": "/home/ska124/QSTK/Bin",
	        "QSSCRATCH": "/home/ska124/QSTK/QSData/Scratch",
	        "CACHESTALLTIME": "12"
	    }
	}
