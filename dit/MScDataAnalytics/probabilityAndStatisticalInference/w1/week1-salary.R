setwd("~/workspace/github.com/bambrozio/academic-corner/dit/MScDataAnalytics")
getwd()
salary<-readRDS("probabilityAndStatisticalInference/salary.rds")
names(salary)

#You can look at the data in a variable by entering its name at the command prompt
salary$gender

#Or get a short overview using the str function
str(salary$gender)

#Or get a relevant statistical summary for a variable e.g. gender
summary(salary$gender)

#Or for salary
summary (salary$salary)

#Or get a summary of all the variables in the dataset“
summary(salary)

# package ‘pylr’ is not available (for R version 3.5.1)
# To install it go to https://cran.r-project.org/web/packages/plyr/index.html and download the package source plyr_1.8.4.tar.gz
# In R Studio in the Files section, in the packages tab click install, then choose Package Archive file (.zip, .tar, .gz) from the Install From drop down box. Browse to locat plyr_1.8.4.tar.gz then click install.
install.packages("~/Downloads/Rcpp_0.12.18.tgz", repos = NULL, type = "source")
library('Rcpp')
install.packages("~/Downloads/plyr_1.8.4.tgz", repos = NULL, type = "source")
library('plyr')

count(salary$gender)

tab<-table(salary$gender, salary$rank)
addmargins(tab)

tab #just display the table with frequencies
prop.table(tab) # shows probability distribution

# writing a function to compute mode:
getmode <- function(v)
{
  uniqv <- unique(v)
  uniqv[which.max(tabulate(match(v,uniqv)))]
}
#Using the function to get the mode of salary:
getmode(salary$salary)

#Measures of Central Tendency
mean(salary$salary)
#You can assign the outcome to a variable
meansal <- mean(salary$salary)
#and then display it on screen
meansal
#Or use the print function to make it look the way you want
print(meansal, digits=1)

#Median
median(salary$salary)

#Range
range(salary$salary)

#Quantiles
quantile(salary$salary)
#to get 1st quantil
x=quantile(salary$salary); x[1] 
#Interquartile Range
IQR(salary$salary)
#Variance
var(salary$salary)
#Standard deviation
sd(salary$salary)
#Rounded
round(sd(salary$salary,2)) #rounded to 2 decimal places

####

# RCommander provides us with a GUI to some common statistical tasks

#For mac, you will need: https://github.com/Rdatatable/data.table/wiki/Installation
install.packages("data.table", type = "source",
                 repos = "http://Rdatatable.github.io/data.table")
library('data.table')

install.packages('car')
library('car')

# Install: https://www.xquartz.org/ (Mac) - Need to logout/login Mac
# apt-get install xvfb xauth xfonts-base (Linux Debian)
#more about X11, perform: ?x11()

install.packages('Rcmdr')
# Launch it: 
# - Some missing packages will be asked to install. Confirm it. After that, you should see the GUI
library('Rcmdr')

