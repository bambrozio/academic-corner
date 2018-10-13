# Task 2 of: http://b-tierney.com/msc-data-mining/dm_wk4/
# Task 2 – Text Mining & Word Cloud in R
# Demo R script for building a word cloud

install.packages (c ( "tm", "wordcloud", "RCurl", "XML", "SnowballC")) # install ‘tm" package
install.packages("RColorBrewer")
install.packages("NLP")
install.packages("tmap")

library (RColorBrewer)
library (wordcloud)
library (SnowballC)
library (NLP)
library(tm)
library(tmap)

# load htmlToText:
# https://github.com/tonybreyal/Blog-Reference-Functions/blob/master/R/htmlToText/htmlToText.R
source("dataMining/htmlToText.R")

# Read the webpages into some local variables
data1 <- htmlToText("http://www.oracle.com/technetwork/database/options/advanced-analytics/overview/index.html")
data2 <- htmlToText("http://www.oracle.com/technetwork/database/options/advanced-analytics/odm/index.html")
data3 <- htmlToText("http://www.oracle.com/technetwork/database/database-technologies/r/r-technologies/overview/index.html")
data4 <- htmlToText("http://www.oracle.com/technetwork/database/database-technologies/r/r-enterprise/overview/index.html")

# combine each of these webpages
data <- c(data1, data2)
data <- c(data, data3)
data <- c(data, data4)

# To convert our web documents into a Corpus.
txt_corpus <- Corpus (VectorSource (data)) # create a corpus

# We can see that we have 4 documents in the corpus.
summary(txt_corpus)

# Remove the White Space in these documents
tm_map <- tm_map (txt_corpus, stripWhitespace) # remove white space

# Remove the Punctuations from the documents
tm_map <- tm_map (tm_map, removePunctuation) # remove punctuations

# Remove Numbers from the documents
tm_map <- tm_map (tm_map, removeNumbers) # to remove numbers

# Remove the typical list of Stop Words
tm_map <- tm_map (tm_map, removeWords, stopwords("english")) # to remove stop words(like ‘as’ ‘the’ etc….)

# Apply stemming to the documents

#If needed you can also apply stemming on your data. 
# I decided to not perform this as it seemed to trunc some of the words in the word cloud.
# tm_map <- tm_map (tm_map, stemDocument)

# Remove any addition words (would could add other words to this list)
tm_map <- tm_map (tm_map, removeWords, c("work", "use", "java", "new", "support"))

# If you want to have a look at the output of each of the above commands you can use the inspect function.
inspect(tm_map)

# Convert into a Text Document Matrix and Sort
Matrix <- TermDocumentMatrix(tm_map) # terms in rows
matrix_c <- as.matrix (Matrix)
freq <- sort (rowSums (matrix_c)) # frequency count of the data
freq #view the words and their frequencies

# Generate the Word Cloud
tmdata <- data.frame (words=names(freq), freq)
wordcloud (tmdata$words, tmdata$freq, max.words=100, min.freq=3, scale=c(7,.5), random.order=FALSE, colors=brewer.pal(8, "Dark2"))







