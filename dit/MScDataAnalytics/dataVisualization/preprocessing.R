

# Set workspace
setwd("~/workspace/github.com/bambrozio/academic-corner/dit/MScDataAnalytics/dataVisualization")

# Using MS Excel 2003 maximum number of rows as reference
ds.max.n = 2^16

# Downloaded dataset has a sample per month (2nd and 3rd quarterly: Apr to Sep)
ds.samples.n = 6

# Maximum rows per sample
ds.sample.max.n = floor(ds.max.n / ds.samples.n)

# Pre-downloaded from https://www.kaggle.com/fivethirtyeight/uber-pickups-in-new-york-city
# Load datasets and create an extra column to hold the quarter
uber_apr14 <- read.csv("input/uber-raw-data-apr14.csv")
uber_apr14$q <- 1
uber_may14 <- read.csv("input/uber-raw-data-may14.csv")
uber_may14$q <- 1
uber_jun14 <- read.csv("input/uber-raw-data-jun14.csv")
uber_jun14$q <- 1
uber_jul14 <- read.csv("input/uber-raw-data-jul14.csv")
uber_jul14$q <- 2
uber_aug14 <- read.csv("input/uber-raw-data-aug14.csv")
uber_aug14$q <- 2
uber_sep14 <- read.csv("input/uber-raw-data-sep14.csv")
uber_sep14$q <- 2

# Create the dataset by extracting samples from each downloaded dataset
uber_q2q3_2014 <- rbind(
  uber_apr14[sample(1:nrow(uber_apr14), ds.sample.max.n), ],
  uber_may14[sample(1:nrow(uber_may14), ds.sample.max.n), ],
  uber_jun14[sample(1:nrow(uber_jun14), ds.sample.max.n), ],
  uber_jul14[sample(1:nrow(uber_jul14), ds.sample.max.n), ],
  uber_aug14[sample(1:nrow(uber_aug14), ds.sample.max.n), ],
  uber_sep14[sample(1:nrow(uber_sep14), ds.sample.max.n), ]
)

# Save the sample to a file to be used in the Tableau for data visualization
write.csv(uber_q2q3_2014, "input/uber_q2q3_2014.csv")

# Cleanup uneeded variables to save memory
rm(uber_apr14, uber_may14, uber_jun14, uber_jul14, uber_aug14, uber_sep14, uber_q2q3_2014)