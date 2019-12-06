#!/usr/bin/python2.7
from yfinance import Ticker
from pandas import DataFrame as df

class Correlation:
	def getHistoricalData(self,pair):
		ticker = Ticker(pair)
		return ticker.history(period="max")
		
	def adjustData(self):
		baseEarliestDate = self.basePairData.index.min()
		counterEarliestDate = self.counterPairData.index.min()
		
		if baseEarliestDate < counterEarliestDate:
			#BasePair has earlier data than counterPair
			tempTicker = Ticker(self.basePair)
			self.basePairData = tempTicker.history(start=counterEarliestDate)
			
		elif baseEarliestDate > counterEarliestDate:
			tempTicker = Ticker(self.counterPair)
			self.counterPairData = tempTicker.history(start=baseEarliestDate)
			#Coutner has earlier data than basePair
			
			
	def correlate(self):
		df1 = df(self.basePairData)
		df2 = df(self.counterPairData)
		self.correlation = df1.corrwith(df2,axis=0)
		print(self.correlation)

	def __init__(self,basePair,counterPair):
		self.basePair = basePair
		self.basePairData = self.getHistoricalData(self.basePair)
		
		self.counterPair = counterPair
		self.counterPairData = self.getHistoricalData(self.counterPair)
		
		self.adjustData()
		self.correlate()
		
		