# Week 1: Introduction to Course (September 17, 2018)
install.packages('tidyverse')

# loading a package
library('devtools')

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

# A key difference between R and many of the more mainstream programming languages is 
# the idea of vectorisation.
# functions in R are programmed to operate on collections of data (vectors) 
# e.g. to find the square of the first 10 natural numbers:
x <- 1:10
x
x^2

# Google's R Style Guide:
# https://google.github.io/styleguide/Rguide.xml

########################################################################################
########################################################################################

# Week 2: R Essentials (September 25, 2018)

# 3 fundamental types:
# 1. numeric - a real number e.g. −10, 0, 2, pi, 4, 8.52
#   two types of numerics “doubles” and “integers”.
#   To specify an integer use a capital L after the number e.g. 4L is the integer four.
a <- 1  # double
a <- 1L # integer
# 2. logical - boolean values e.g. 
a <- TRUE
a <- FALSE
a <- T
a <- F
# 3. character - character strings e.g. 
a <- 'David'
a <- 'loves'
a <- 'R'
a <- '101'
a <- 'TRUE'

# The usual math operations apply to numerics:
-10 + 2
4 * 4
4 / 2
2 ^ 4

# R also provides a number of built-in math functions:
sqrt(4)
abs(-10)
floor(8.52)
cos(pi)

# Comparison operations result in a logical value:
-10 > 2
4 <= 4
4 != 2
2 == 4
(0.5 - 0.4) == 0.1

# The all.equal function allows for insignificant differences:
all.equal(0.5 - 0.4, 0.1)


# AND Operator
(-10>2) & (4!=2)
(-10>2) && (invalid !=2) # If true in the first condition, won't test the seocond one

# OR Operator
(-10 < 2) | (4 != 2)
(-10 < 2) || (invalid != 2) # If true in the first condition, won't test the seocond one

# querying and manipulating strings:
nchar('David')
substr('David', 2, 5)
toupper('David')

# change the type (character > double > integer > logical)
as.character(T)
as.character(pi)
as.character(4L)
as.double(T)
as.double(FALSE)
as.double(4L)
as.integer("1")

# Missing values can crop up in data for various reasons.
# R uses the special value NA (not available) to represent missing
# values e.g. an NA is produced by this coercion:
as.double('David')

# Problem with NA's when they are in the midle of data, they "kill" all your equation. Thus, first identify 
# and treat them before
7 + 12 + 3 + 15 + NA

x <- c(7, 12, 3, 15, NA)
sum(x)

# Some functions has the feature of ignoring NA's:
x <- c(7, 12, 3, 15, NA)
sum(x, na.rm = T)

# type of an object can be resolved by using the functions “is.” or typeof:
x <- 'David'
is.character(x)
x <- T
is.logical(x)
x <- 4
is.integer(x)
is.double(x)
is.na(x)
typeof(x)
x <- NA
is.na(x)

# Data Structures
## Vector

# combine objects in a Array: 
age <- c(71, 56, 71, 71)
age

# The type of a vector is the type of the data stored in it:
typeof(age)

# Similarly, it is possible to create vectors of character or logical type.
name <- c('Donald', 'Barack', 'George', 'Bill')
democrat <- c(F, T, F, T)

# The type of the data in a vector can be changed explicitly using the “as.” functions:
as.character(age)

# note all numeric values except zero are coerced to TRUE (including negatives)
as.logical(age)

# The type can also be changed implicitly if the context permits it:
sum(democrat)

# It is also possible to attach metadata to a vector e.g. to name the entries.
age <- c(trump = 71, obama = 56, bush = 71, clinton = 71)
age
names(age) # names associated with a vector:

# Assignment can be used to change the names associated with a vector after creation 
# i.e. overwriting the current names (if any).
age <- c(71, 56, 71, 71)
age
names(age) <- c('trump', 'obama', 'bush', 'clinton')
age

# Assignment can also be used to remove the names:
names(age) <- NULL
age













