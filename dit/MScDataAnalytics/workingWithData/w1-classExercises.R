install.packages('tidyverse')
library('tidyverse')
install.packages('devtools')
library('devtools')
?devtools

# list of packages installed
library()

# list of packages loaded
search()

# overview of functions contained in a package
help(package = 'devtools')

# list of vignettes
vignette(package = 'devtools')
# view a vignette
vignette('dependencies')

# Unusually, there are five different symbols in R that can be used for assignment:
x <- 10
x = 11
x <<- 12
13 -> x
14 ->> x

# A key difference between R and many of the more mainstream programming languages is the idea of vectorisation.
# What this means is that the functions in R are programmed to operate on collections of data (vectors) 
# e.g. to find the square of the first 10 natural numbers:

x <- 1:10
x
x^2




