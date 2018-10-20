# Probability and Statistical Inference
> Summary of lectures

## Lecture 1 - 19/09/2018
> Introduction & Fundamentals

### Introduction

- (comic strips):
    - Data Analysys:
        - The gathering, display, and and summary of data.
    - Probability:
        - The laws of chances, in and out of the casino.
    - Statistica Inference
        - The science of Drawing statistical conclusions from specific data, using a knownkedge of probability.

- What is the module about:
    - For the purposes of a Statistical Inquiry
        - How to collect and prepare data for use
        - How to describe the data (in terms of format and statistically)
        - How to formulate, state, test and report on hypotheses
        - How to conduct exploratory and predictive analytics
        - How to use an appropriate software package 
            - We will be using R
        - How to report your findings correctly

- How to succeed in the module
    - Focus on learning the process of conducting a statistical analysis 
        - What are you trying to discover or show?
            - Figure out a question you are trying to answer/theory you are trying to test
        - What data do you need to collect?
        - Once you have data, how do you describe the data you have?  
            - You need to explain this to whoever will be the consumer of your work
        - What analysis should you conduct?
            - You need to know the types of tests to run and how to explain this to your consumer
        - How do you interpret your analysis?
            - You need to know how to interpret the outcomes of the analysis and present these to your consumer
        - How will you present your findings?
        - Present the question you are interested in 
            - In a way that makes sense to conduct a statistical analysis
        - Inspect and prepare the data you have 
            - To support a statistical analysis
        - Describe the data you have
            - In a way that your consumer can understand any constraints the data may put on your analysis
        - Conduct a statistical analysis
            - Using appropriate statistical tests
        - Report on your statistical analysis
            - In a way that makes sense for your consumer
        - Interpret the outcomes of your statistical analysis
            - Drawing appropriate conclusions
        - Report on the findings of your statistical analysis
            - In a way that makes sense for your consumer


### Fundamentals
- Types of Data Analysis
    - Qualitative Methods
        - Testing theories using language
    - Quantitative Methods
        - Testing theories using numbers (via statistics)
    - statistical inquiry:
        - science of collecting, analysing, and drawing conclusions from data
        - science of collecting, describing, and interpreting data.
        - objectively and quantitatively
        - Is usually carried out with a SAMPLE
- The Research Process (Andy Field)
![The Research Process (Andy Field)](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/theResearchProcess.png)

    - Inital Observation (Research Question)
        - Data
            - Find something that needs explaining
            - Read other research
            - Test the concept
                - collect data that will provide evidence you can test to see if your idea is valid
            - Define variables that can be measured and can differ across entities or time
    - Generate Theory
        - Theory: A hypothesized general principle or set of principles that explains known findings about a topic and from which new hypotheses can be generated. e.g. Computer Science attracts students with strong mathematical ability.
    - Generate Hypotheses 
        - Identify Variables.
            - Hypotheses: A prediction from a theory. E.g. the number of people applying for an MSc in Computer Science will have basic mathematical ability greater than the general level in the population.
            - Falsification: The act of disproving a theory or hypothesis.
    - Collect Data to Test Theory
        - Measure Variables
            - What data am I interested in/do I need?
                - Population: The entire set of individuals or objects of interest or the measurements obtained from all individuals or objects of interest
                    - finite or infinite.
                - Sample: A portion, or part, of the population of interest
                    - Statistical inquiry is usually carried out with a SAMPLE
                    - If Sample is not representative it is biased.
                    - Factors influencing the accuracy of a sample’s ability to represent a population: size and randomness.
                - Individuals: people or objects being studied
                    - The set of data of an individua is referred to as a case.
                - Variable: A characteristic about each individual.
                    - Any characteristic whose value may change from one individual to another.
                - Data: Value of a variable for individual observations.
                - Dataset: The set of values collected for the variable(s) from each of the individuals belonging to the sample/population the dataset represents.
                    - Each case in a dataset has one datum or observation for each variable.
                - Experiment: A planned activity whose results yield a set of data.
                - Parameter: A numerical value describing an aspect of an entire population.
                    - For small populations it is possible to measure to compute a parameter
                - Statistic: A numerical value describing an aspect of the sample.
                    - For larger populations you will measure to compute a statistic
        - Example: 
        ```
        A country is interested in learning about the average age of its academic staff working at third level.
        The basic terms in this situation:

        - The population is all academic members working in the country and we want to determine their age.
        - A sample is any subset of that population.  
            - For example, we might select 50 staff members and determine their age.
            As long as this is representative and sufficiently large to model the population.
        - The variable is the “age” of each staff member.
        - One datum would be the age of a specific faculty member.
        - The experiment would be the method used to select the ages forming the sample and determining the actual age of each staff member in the sample.
        - The parameter of interest is the “average” age of all academic staff in the country.
        - The statistic is the “average” age for all academic staff in the sample.
        ```
        - Biased Sampling Method:
            - A sampling method that produces data which systematically differs from the population from which it is taken.  
        - Aim for a Simple Random Sample
            - A sample of n measurements from a population is a subset of the population selected in such a manner that every sample of size n from the population has an equal chance of being selected

        - Data Collection: What to Measure? Eg.:
        ```
        Hypothesis: Consumption of Coca-Cola improves a student’s ability to concentrate.
        Decide what variables you need.
        Independent Variable:
            - The proposed cause
            - Predictor variable
            - Manipulated variable (in experiments)
            - Coca-Cola consumption in the hypothesis above
        Dependent Variable:
            - The proposed effect
            - An outcome variable
            - Measured not manipulated (in experiments)
            - A student’s ability to concentrate in the hypothesis above
        ```

        - Qualitative, or Attribute, or Categorical, Variable
            - A variable that categorizes or describes an element of a population.
            - Identifies basic differentiating characteristics of the population.
            > Note: Arithmetic operations, such as addition and averaging, are **not** meaningful for data resulting from a qualitative variable.
        - Quantitative, or Numerical, Variable
            - A variable that quantifies an element of a population.
            - Observations or measurements take on numerical values
            > Note: Arithmetic operations such as addition and averaging, are meaningful for data resulting from a quantitative variable.
            - Discrete:
                - Isolated points along a number line
                - Usually counted
                - Can only take certain values
                - E.g. rolling a dice, #students attending class
            - Continuous
                - Variable that can be any value in a given range
                - Usually measured
                - E.g. heights of students attending class, time spent concentrating in class

        - Levels of measurement
            - Nominal
                - Data can be assigned to a category
            - Ordinal
                - There is a ranking associated with the variable
                - Data can be ordered from smallest to largest, best to worst etc.
            - Interval
                - Data can be ordered but there is meaning between the values of order
                - Allows comparison between the data values
            Ratio
                - Data can be ordered, there are differences between the values and you can find the ratio 
                - Has an absolute 0
                - It makes sense to say for example one value is twice as large as another
                - Interval and Ration may be referred to as Scale
    - Analyse Data
        - Graph Data
        - Fit a Model
        - Summarizing vs Analysing:
            - Descriptive Statistics
                - Describing the population and the sample
                - Summarizing
            - Inferential Statistics
                - Inference from sample to population
                - Inference from statistic to parameter
            - Using the appropriate statistical tests to draw inference

- Measure of Central Tendency
    - A single number to serve as a representative value around which all the numbers in the set tend to cluster.
- Mode: The value with the greatest frequency on the distribution.
    - The mode is not a very useful measure of central tendency
    - Two data sets that are very different from each other can have the same mode
    - The mode is primarily used with nominal variables
    - Eg.:
        - 3, 7, 5, 13, 20, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29
        - In order these numbers are:
        - 3, 5, 7, 12, 13, 14, 20, **23, 23, 23, 23**, 29, 39, 40, 56
        - In this case the mode is **23**.
    - Bimodal Distributions: 
        - When a distribution has two “modes,” it is called bimodal
    - Multimodal Distributions
        - If a distribution has more than 2 “modes,” it is called multimodal

- Median
    - It is the score in the middle
    - The middle score of a sequence of all the scores in a distribution arranged from lowest to highest.
    - Eg.:
        - Sort the data from highest to lowest
        - Find the score in the middle
            - middle = (N + 1) / 2 
            - If N, the number of scores, is even the median is the average of the middle two scores
        eg.: 
            - 10   8   14   15   7   3   3   8   12   10   9
            - Sort the scores:
            - 15   14   12   10   10   9   8   8   7   3   3
            - Determine the middle score:
            - middle = (N + 1) / 2 = (11 + 1) / 2 = 6
            - Middle score = median = 9
        eg2:
            - 24  18  19  42  16  12
            - 42  24  19  18  16  12
            - middle = (N + 1) / 2 = (6 + 1) / 2 = 3.5
            - Median = average of 3rd and 4th scores:
            - (19 + 18) / 2 = 18.5

- The Mean
    - The arithmetic average of a group of scores
    - eg.:
        - 1   5   4   3   2
        - 1 + 5 + 4 + 3 + 2 = 15
        - 15 / 5 = 3
    - The mean is sensitive to extreme values 

- Measures of Dispersion
    - Descriptive statistics that describe how similar a set of scores are to each other (or the range of scores)
        - The more similar the scores are to each other, the lower the measure of dispersion will be
        - The less similar the scores are to each other, the higher the measure of dispersion will be
        - In general, the more spread out a distribution is, the larger the measure of dispersion will be
        - 3 main measures: 
            - The range
                - difference between the largest and smallest score in the set of data:
                    - 4   8   1   6   6   2   9   3   6   9
                    - XL=9; XS=1
                    - Range = XL - XS = 8
                - is used when mainly for ordinal data
                - rarely used in scientific work
                - Two very different sets of data can have the same range
            - Variance / standard deviation
                - Variance:
                    - Concerned with deviations from the mean (X-µ)
                    - It's the **average** of the **squared** differences from the mean
                    - First subtract the mean from each of the scores  
                        - This difference is called a **deviate** or a **deviation score**
                        - The deviate tells us how far a given score is from the typical, or average, score
                        - Thus, the deviate is a measure of dispersion for a given score
                    - Then square the result
                        - Because if we just added up the differences from the mean the negatives would cancel the positives
                        - Also, If we used absolute values we wouldn’t get an accurate measure of spread
                    - Variance is defined as the average of the deviations from the mean squared:
                    ![Variance](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/variance.png)
                    - N here is the **degrees of freedom**:
                        - the number of independent pieces of information on which the estimate is based
                - standard deviation
                    - Standard deviation = **the square root of the Variance**
                    - The standard deviation is the most useful and the most popular measure of dispersion. 
                        - ** Used to calc margens of the mean. Eg: group is from (mean - SD) until (mean + SD)
                    - Also helpful in comparing samples.
                    - Greek symbol sigma **σ**
                    - The larger the value the more spread out around the mean the data is, smaller means less spread.
                    - The 68-95-99.7 Empirical Rule In the normal distribution with mean µ and standard deviation σ:
                        - 68% of the observations fall within σ of the mean µ.
                        - 95% of the observations fall within 2σ of the mean µ.
                        - 99.7% of the observations fall within 3σ of the mean µ.
                    - ** Eg.: If you compare 2 Data Sets with the same mean score for Probability and Statistics, it doesn't mean they will have the same performance, as SD may be diff.
            - The Interquartile Range (IQR)
                - the difference of the first (25th percentile) and third (75th percentile) quartiles divided by two
                - **IQR = (Q3 - Q1) / 2**
                - Eg: IQR of `2, 4, 6, 8, 10, 12, 14, 20, 30, 60`:
                    - (25 - 5) / 2 = **10**

- Measure of Skew
![Measure of Skew](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/skewMeasure.png)
    - Skew is a measure of symmetry in the distribution of scores
    - Normal distributions: mean = median = mode
    - Positively skewed distributions: mean > median
    - Negatively skewed distributions: mean < median
- Kurtosis
![Kurtosis](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/kurtosis.png)
    - measures whether the scores are spread out more or less than they would be in a normal (Gaussian) distribution
    - Distribution Normal == 3 == mesokurtic
    - Distribution less spread == kurtosis > 3 == leptokurtic
    - Distribution more spread == kurtosis < 3 == platykurtic

- When to use Median & IQR:
    - The median is often used when the distribution of scores is either positively or negatively skewed
        - The few really large scores (positively skewed) or really small scores (negatively skewed) will not overly influence the median
    - The IQR is often used with skewed data as it is insensitive to the extreme scores
- Mean and Standard Deviation
    - You should use the mean when
        - the data are interval or ratio scaled
            - Many people will use the mean with ordinally scaled data too
        -  and the data are not skewed
    - The mean is preferred because it is sensitive to every score
    - If you change one score in the data set, the mean will change
    - **If you use mean you also use standard deviation**

 - **Key concepts:**
    - Sample: Size, representativeness, extremes
    Differing types of variable: nominal/categorical, ordinal, interval and ratio
    Measures of central tendency: the mean, median and mode
    Measures of dispersion: range, inter-quartile range, variance and standard deviation
    Shape: normal, skew, kurtosis


---

## Lecture 2 - 19/09/2018
> Describing and Presenting Data

- Source of the class:
    - Statistics and Data Analysis, Peck, Olsen and Devore
    - Discovering Statistics Using IBM SPSS (equivalent R book), Andy Field
    - Understanding Basic Statistics, Brase and Brase

 - Webcourses portal: Download content (Week 2): 
```
File geoms.docx (843.268 KB)
File PSIWeek2.R (6.032 KB)
File L2-More on Describing Data.pptx (2.435 MB)
File PSIWeek2Data.zip (12.167 KB)
File Datasets.docx (14.26 KB)

Attached to this page you will find the material you need for the lecture tomorrow plus the practical class.

geoms.docx is a scan of pages from Andy Field's book about common geom functions and aethetics
Datasets.docx describes the data we are using.
PSIWeek2Data.zip contains the datasets we are going to use.
PSIWeek2.R includes the R script for creating some graphs from the lecture.
```

---

## Lecture 3 - 19/09/2018
> Correlation and Difference

- Sources of the class:
    - Statistics and Data Analysis, Peck, Olsen and Devore
    - Discovering Statistics Using IBM SPSS (And equivalent R book), Andy Field
    - Understanding Basic Statistics, Brase and Brase
    - SPSS Survival Manual, Julie Pallant

 - Webcourses portal: Download content (Week 3): 
```
File PSIWeek3-Lecture.Rmd (6.118 KB)
File Field-BDI-Non-parametric.dat (466 B)
File L3 - Correlation and Difference.pptx (3.075 MB)
File PSIWeek3-Lecture.html (958.808 KB)
File PSIWeek3Exercise.docx (198.319 KB)
File survey.dat (192.817 KB)
File Regression.sav (190.589 KB)
This week we are introducing statistical tests for correlation and difference.

Attached to this page you will find:

Lecture notes (.pptx)
PSI-Week3.rmd - R markdown file with all the commands used in the lecture + PSIWeek3-Lecture.html which is the knitted output
All the datafiles used in the lecture (both .dat and .sav formats)
The specification for the practical class PSIWeek3Exercise.pdf (this uses the survey dataset from this week and the regression dataset from last week)
I will be using R markdown from now on to provide you with the R code. A guide to getting started is available at https://rmarkdown.rstudio.com/lesson-1.html
```

(WIP)

---

## Lecture 4 - 10/10/2018
> Difference

- Sources of the class: 
    - Statistics and Data Analysis, Peck, Olsen and Devore;
    - Discovering Statistics Using R, Field and Miles
    - Understanding Basic Statistics, Brase and Brase
    - SPSS Survival Manual, Julie Pallant

 - Webcourses portal: Download content (Week 4): 
```
File experim.dat (3.964 KB)
File Field-BDI-Non-parametric.dat (466 B)
File L4 - Difference.pptx (1.66 MB)
File PSIWeek4-Lecture.html (790.572 KB)
File PSIWeek4-Lecture.Rmd (3.924 KB)
File Regression.sav (190.636 KB)
File survey.dat (192.817 KB)
File PSIWeek4Exercise.docx (198.268 KB)

Attached to this page you will find:

Lecture notes for this week
Rmd file plus Html output for rmd used in the lecture
Exercise for this week
Datasets used (regression.sav, survey.dat, Field-BDI-Non-Parametric.dat, experim.dat)
```

(WIP)