# Cosine Similarity
Python code to view the [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity) between news articles. This code allows you to compare a list of postings, articles, etc. against one another based on how similar they are in terms of their cosine distance.

![cosine_similarity_graph](https://github.com/azmelcmie/cosine_csv/blob/master/img/cosine_similarity_graph.PNG)

# Input & Output
The input comes in the form of a tab separated value file with an index, title and summary columns. No headers are present.
Below is a sample of the data.

![news_articles](https://github.com/azmelcmie/cosine_csv/blob/master/img/news_articles.png)

 
 The results will appear in a csv file showing the scores between the value of 0 and 1. These scores can then be converted into percentages.

![cosine_similarity_score](https://github.com/azmelcmie/cosine_csv/blob/master/img/cosine_similarity_score.PNG)

The first column shows the index of the first news articles compared against the index number of the second news article. The third column shows the score rating based on the cosine similarity calculation.

## Environment
Coded and tested in Anaconda version 4.4.0.

## Usage
Edit the following lines in the **coscsva.py** file to customize to your own needs.

Enter the location and type of file, ideally the input will be a tsv file containing an index and a text body column (**line 18**):

````python
data = pd.read_csv('data/news_articles.tsv', header=None, sep='\t', engine='python')
````

The column no. where the comparison is to be made, i.e. the article column (**Line 47**):

````python
text = row[2]
````


This is an initial version with no training and testing. I will continue to enhance this programme in the coming weeks.
