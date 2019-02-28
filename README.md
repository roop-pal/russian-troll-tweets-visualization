# Visualizing Sentiments of Russian Troll Tweets

This data was used in the FiveThirtyEight story [Why We’re Sharing 3 Million Russian Troll Tweets](https://fivethirtyeight.com/features/why-were-sharing-3-million-russian-troll-tweets/).

We utilized a neural network to analyze the sentiments of these tweets and to see how the clemson-derived categories concorded with the sentiments from the dataset.

https://beta.observablehq.com/@mogryzko/for-chris/2

This was done for the COMS 4995 class "Data Visualization" at Columbia university, with Max Ogryzko, Shubham Singhal, Roop Pal, and Chris Doan. Code for the visualization is appended at link above.

From the source description:

"This directory contains data on nearly 3 million tweets sent from Twitter handles connected to the Internet Research Agency, a Russian "troll factory" and a defendant in [an indictment](https://www.justice.gov/file/1035477/download) filed by the Justice Department in February 2018, as part of special counsel Robert Mueller's Russia investigation. The tweets in this database were sent between February 2012 and May 2018, with the vast majority posted from 2015 through 2017.

FiveThirtyEight obtained the data from Clemson University researchers [Darren Linvill](https://www.clemson.edu/cbshs/faculty-staff/profiles/darrenl), an associate professor of communication, and [Patrick Warren](http://pwarren.people.clemson.edu/), an associate professor of economics, on July 25, 2018. They gathered the data using custom searches on a tool called Social Studio, owned by Salesforce and contracted for use by Clemson's [Social Media Listening Center](https://www.clemson.edu/cbshs/centers-institutes/smlc/)."

Taken from the source:
The files have the following columns:

Header | Definition
---|---------
`external_author_id` | An author account ID from Twitter 
`author` | The handle sending the tweet
`content` | The text of the tweet
`region` | A region classification, as [determined by Social Studio](https://help.salesforce.com/articleView?id=000199367&type=1)
`language` | The language of the tweet
`publish_date` | The date and time the tweet was sent
`harvested_date` | The date and time the tweet was collected by Social Studio
`following` | The number of accounts the handle was following at the time of the tweet
`followers` | The number of followers the handle had at the time of the tweet
`updates` | The number of “update actions” on the account that authored the tweet, including tweets, retweets and likes
`post_type` | Indicates if the tweet was a retweet or a quote-tweet
`account_type` | Specific account theme, as coded by Linvill and Warren
`retweet` | A binary indicator of whether or not the tweet is a retweet
`account_category` | General account theme, as coded by Linvill and Warren
`new_june_2018` | A binary indicator of whether the handle was newly listed in June 2018
`alt_external_id` | Reconstruction of author account ID from Twitter, derived from `article_url` variable and the first list provided to Congress
`tweet_id` | Unique id assigned by twitter to each status update, derived from `article_url`
`article_url` | Link to original tweet. Now redirects to "Account Suspended" page
`tco1_step1` | First redirect for the first http(s)://t.co/ link in a tweet, if it exists
`tco2_step1` | First redirect for the second http(s)://t.co/ link in a tweet, if it exists
`tco3_step1` | First redirect for the third http(s)://t.co/ link in a tweet, if it exists

If you use this data and find anything interesting, please let us know. Send your projects to oliver.roeder@fivethirtyeight.com or [@ollie](https://twitter.com/ollie).

The Clemson researchers wish to acknowledge the assistance of the Clemson University Social Media Listening Center and Brandon Boatwright of the University of Tennessee, Knoxville.
