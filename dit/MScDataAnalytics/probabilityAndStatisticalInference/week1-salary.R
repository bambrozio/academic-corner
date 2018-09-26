setwd("~/workspace/github.com/bambrozio/academic-corner/dit/MScDataAnalytics")
getwd()
salary<-readRDS("probabilityAndStatisticalInference/salary.rds")
names(salary)
setwd("~/workspace/github.com/bambrozio/academic-corner/dit/MScDataAnalytics")

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
install.packages('pylr')

library('pylr')
