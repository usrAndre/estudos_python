#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:53:48 2022

@author: andreluizrodriguesdasilva
"""

# PIVOT TABLES
'''
We have seen how the GroupBy abstraction lets us explore relationships within a data‐
set. A pivot table is a similar operation that is commonly seen in spreadsheets and
other programs that operate on tabular data. The pivot table takes simple column-
wise data as input, and groups the entries into a two-dimensional table that provides
a multidimensional summarization of the data. The difference between pivot tables
and GroupBy can sometimes cause confusion; it helps me to think of pivot tables as
essentially a multidimensional version of GroupBy aggregation. That is, you split-
apply-combine, but both the split and the combine happen across not a one-
dimensional index, but across a two-dimensional grid.'''

# Motivating Pivot Tables
# For the examples in this section, we’ll use the database of passengers on the Titanic,
# available through the Seaborn library (see “Visualization with Seaborn” on page 311):

import numpy as np
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')

titanic.head()

# This contains a wealth of information on each passenger of that ill-fated voyage,
# including gender, age, class, fare paid, and much more.

'''Pivot Tables by Hand'''

# To start learning more about this data, we might begin by grouping it according to
# gender, survival status, or some combination thereof. If you have read the previous
# section, you might be tempted to apply a GroupBy operation—for example, let’s look
# at survival rate by gender

titanic.groupby('sex')[['survived']].mean()

# This immediately gives us some insight: overall, three of every four females on board
# survived, while only one in five males survived!
# This is useful, but we might like to go one step deeper and look at survival by both sex
# and, say, class. Using the vocabulary of GroupBy, we might proceed using something
# like this: we group by class and gender, select survival, apply a mean aggregate, com‐
# bine the resulting groups, and then unstack the hierarchical index to reveal the hidden
# multidimensionality. In code

titanic.groupby(['sex', 'class'])['survived'].aggregate('mean').unstack()


'''Pivot Table Syntax'''

# Here is the equivalent to the preceding operation using the pivot_table method of
# DataFrames

titanic.pivot_table('survived', index='sex', columns='class')
# This is eminently more readable than the GroupBy approach, and produces the same
# result.

'''Multilevel pivot tables'''
# Just as in the GroupBy, the grouping in pivot tables can be specified with multiple lev‐
# els, and via a number of options. For example, we might be interested in looking at
# age as a third dimension. We’ll bin the age using the pd.cut function:
age = pd.cut(titanic['age'], [0, 18, 80])
titanic.pivot_table('survived', ['sex', age], 'class')

# We can apply this same strategy when working with the columns as well; let’s add info
# on the fare paid using pd.qcut to automatically compute quantiles
fare = pd.qcut(titanic['fare'], 2)
titanic.pivot_table('survived', ['sex', age], [fare, 'class'])
# The result is a four-dimensional aggregation with hierarchical indices (see “Hierarch‐
# ical Indexing” on page 128), shown in a grid demonstrating the relationship between
# the values.

'''Additional pivot table options'''
# The full call signature of the pivot_table method of DataFrames is as follows:
    
# call signature as of Pandas 0.18
'''
DataFrame.pivot_table(data, values=None, index=None, columns=None,
aggfunc='mean', fill_value=None, margins=False,
dropna=True, margins_name='All')
'''
# We’ve already seen examples of the first three arguments; here we’ll take a quick look
# at the remaining ones. Two of the options, fill_value and dropna, have to do with
# missing data and are fairly straightforward; we will not show examples of them here.
# The aggfunc keyword controls what type of aggregation is applied, which is a mean
# by default. As in the GroupBy, the aggregation specification can be a string represent‐
# ing one of several common choices ('sum', 'mean', 'count', 'min', 'max', etc.) or a
# function that implements an aggregation (np.sum(), min(), sum(), etc.). Additionally,
# it can be specified as a dictionary mapping a column to any of the above desired
# options:
titanic.pivot_table(index='sex', columns='class',
                    aggfunc={'survived':sum, 'fare':'mean'})

# titanic.pivot_table(index='sex', columns='class',
#                     aggfunc={'survived':'sum', 'fare':'mean'})


'''
Notice also here that we’ve omitted the values keyword; when you’re specifying a
mapping for aggfunc, this is determined automatically.
At times it’s useful to compute totals along each grouping. This can be done via the
margins keyword'''

titanic.pivot_table('survived', index='sex', columns='class', margins=True)
# Here this automatically gives us information about the class-agnostic survival rate by
# gender, the gender-agnostic survival rate by class, and the overall survival rate of 38%.
# The margin label can be specified with the margins_name keyword, which defaults to
# "All".


'''EXAMPLE; Birthrate Data'''

'''As a more interesting example, let’s take a look at the freely available data on births in
the United States, provided by the Centers for Disease Control (CDC). This data can
be found at https://raw.githubusercontent.com/jakevdp/data-CDCbirths/master/
births.csv (this dataset has been analyzed rather extensively by Andrew Gelman and
his group; see, for example, this blog post):'''

# shell command to download the data:
# !curl -O https://raw.githubusercontent.com/jakevdp/data-CDCbirths/
# master/births.csv

births = pd.read_csv('births.csv')
births.head()

# We can start to understand this data a bit more by using a pivot table. Let’s add a dec‐
# ade column, and take a look at male and female births as a function of decade:

births['decade'] = 10 * (births['year']//10)
births.pivot_table('births', index='decade', columns='gender', aggfunc=sum)


# We immediately see that male births outnumber female births in every decade. To see
# this trend a bit more clearly, we can use the built-in plotting tools in Pandas to visual‐
# ize the total number of births by year (Figure 3-2; see Chapter 4 for a discussion of
# plotting with Matplotlib):


#%matplotlib inline
import matplotlib.pyplot as plt
sns.set() # use Seaborn styles
births.pivot_table('births', index='year', columns='gender', aggfunc='sum').plot()
plt.ylabel('total births per year');

# With a simple pivot table and plot() method, we can immediately see the annual
# trend in births by gender. By eye, it appears that over the past 50 years male births
# have outnumbered female births by around 5%.


'''Further data exploration'''
# Though this doesn’t necessarily relate to the pivot table, there are a few more interest‐
# ing features we can pull out of this dataset using the Pandas tools covered up to this
# point. We must start by cleaning the data a bit, removing outliers caused by mistyped
# dates (e.g., June 31st) or missing values (e.g., June 99th). One easy way to remove
# these all at once is to cut outliers; we’ll do this via a robust sigma-clipping operation:
    
quartiles = np.percentile(births['births'], [25, 50, 75])
mu = quartiles[1]
sig = 0.74 * (quartiles[2] - quartiles[0])

# This final line is a robust estimate of the sample mean, where the 0.74 comes from the
# interquartile range of a Gaussian distribution. With this we can use the query()
# method (discussed further in “High-Performance Pandas: eval() and query()” on
# page 208) to filter out rows with births outside these values

births = births.query('(births > @mu - 5 * @sig) & (births < @mu + 5 * @sig)')

# Next we set the day column to integers; previously it had been a string because some
# columns in the dataset contained the value 'null':

# set 'day' column to integer; it originally was a string due to nulls
births['day'] = births['day'].astype(int)  

# Finally, we can combine the day, month, and year to create a Date index (see “Work‐
# ing with Time Series” on page 188). This allows us to quickly compute the weekday
# corresponding to each row:
    
# create a datetime index from the year, month and day
births.index = pd.to_datetime(10000 * births.year + 
                              100 * births.month + 
                              births.day, format='%Y%m%d')

births['dayofweek'] = births.index.dayofweek

# Using this we can plot births by weekday for several decades
import matplotlib.pyplot as plt
import matplotlib as mpl

births.pivot_table('births', index='dayofweek',
                   columns='decade', aggfunc='mean').plot()
plt.gca().set_xticklabels(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
plt.ylabel('mean births by day');

# Another interesting view is to plot the mean number of births by the day of the year.
# Let’s first group the data by month and day separately:

births_by_date = births.pivot_table('births', 
                                    [births.index.month, births.index.day])
births_by_date.head()
#births_by_date.tail()


# The result is a multi-index over months and days. To make this easily plottable, let’s
# turn these months and days into a date by associating them with a dummy year vari‐
# able (making sure to choose a leap year so February 29th is correctly handled!)

births_by_date.index = [pd.datetime(2012, month, day)
                        for (month, day) in births_by_date.index]
births_by_date.head()
#births_by_date.tail()

# Focusing on the month and day only, we now have a time series reflecting the average
# number of births by date of the year. From this, we can use the plot method to plot
# the data (Figure 3-4). It reveals some interesting trends

# Plot the results
fig, ax = plt.subplots(figsize=(12, 4))
births_by_date.plot(ax=ax);

# In particular, the striking feature of this graph is the dip in birthrate on US holidays
# (e.g., Independence Day, Labor Day, Thanksgiving, Christmas, New Year’s Day)
# although this likely reflects trends in scheduled/induced births rather than some deep
# psychosomatic effect on natural births. For more discussion on this trend, see the
# analysis and links in Andrew Gelman’s blog post on the subject. We’ll return to this
# figure in “Example: Effect of Holidays on US Births” on page 269, where we will use
# Matplotlib’s tools to annotate this plot.