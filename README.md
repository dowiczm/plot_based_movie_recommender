# Executive Summary
It's often difficult trying to decide on a movie to watch. A sometimes more challenging and feat is trying to remember the name of a movie you watched last month, last week, or even yesterday. More often than I would like to admit, I find myself looking up movies on Google by typing in plot keywords and specific scenes that I remember. This trivial problem inspired my research.

The goal of this research was to create a model that received text input from a user specifying the genre and specific plot keywords of a movie they could not remember by name. To do this, data was scraped directly from a collection of IMDb movies containinig 6,656 movies. Each movie had brief plot summaries submitted by IMDb users, which was the focal point of my study.

The collection of plot summaries for each movie was combined into a large text document, cleaned and used for extraction. A wide variety of extraction methods were tested and are explained within the 'code' folder. Ultimately, the 10 most common nouns and verbs from each collection of summaries were extracted using the spaCy library. These 10 words were placed into a separate column and used for similarity comparisons.

At its core, the model I created uses spaCy's similarity function to calculate a similarity score for the user-text and the extracted keyword for every movie in the dataframe. In order to increase speed and accuracy, the user was also prompted to includ the specific genre/genres they believed their mystery-movie to be in. Including the genres in the  query reduced the dimensionality of the dataframe by filtering out movies that did not meet that genre criteria. 

To evaluate the models performance, 5 queries from fellow classmates were placed into the model via Streamlit. Of the 5 queries, 3 were succesfull and 2 failed. The failures exposed the models weaknessess, as the model is unable to identify very specific plot points and quotes. The 3 successful queries demonstrated the models ability to accurately match users very general and broad keywords. 

Overall, this research highlighted how general plot keywords extracted from IMDb movie summaries could be for accurate predictions for users on the application. It also demonstrated that different people describe movies differently and remember a wide array of details. I am currently working on incorporating quotes and a full synposis into the model to better predict queries that reference specific plot points and character quotes. I am also workinig on improving the models speed and exploring new ways to find similarity between text documents other than the spaCy similarity function, such as an LSTM. 

The streamlit application can be found in the 'code' folder. 

This project remains opened ended and is by no means complete.  



## Problem Statement
Create a recommender system that returns 10 movies most similar to a list of keyword and genres submitted by the user.
 

### Data Description 

The data used for this research was scraped using the bs4 and requests library. The IMDb collection of movies can be found here:(https://www.imdb.com/search/title/countries=us&title_type=feature&num_votes=10000,&sort=user_rating,desc). 

* [`imdb_6k.csv`](./data/imdb_6k.csv): Raw Data


### Data Dictionary

|Feature|Type|Description|

|---|---|---|

|href|object|anchor tag for imdb lookup|
|title|object|title of movie|
|genre|object|list of genres (max 3)|
|user_plots|object|collection of plot summaries submitted by users on IMDb|
|synopsis|object|full-length synopsis of movie|
|directors|object|directors of movie|
|writers|object|writers of movie|
|stars|object|top 3 cast memebers of movie|

