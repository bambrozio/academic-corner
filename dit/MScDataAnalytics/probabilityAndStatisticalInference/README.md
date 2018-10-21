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
    - Summing up all the observation and dividing by number of observations. 
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

- Mean or Median
    - The median is less sensitive to outliers (extreme scores) than the mean and thus a better measure than the mean for highly skewed distributions, e.g. family income. 
    - Median is more reflective of the data.
    - Eg: 
        - Mean of 20, 30, 40, and 990 is (20+30+40+990)/4 =270. 
        - Median of these four observations is (30+40)/2 =35. 
        - 3 observations out of 4 lie between 20-40.  
        - Mean of 270 really fails to give a realistic picture of the major part of the data. 

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

- Statistics: Science of collection, presentation, analysis, and reasonable interpretation of data.
    - Statistics provides a rigorous scientific method for gaining insight into data. 
- Experiements and variables:
    - Variable: Things we can manipulate, Compute, Or control for
    - X is a variable, x is the value of the variable
    - Random variable
        - is determined by chance
    - Discrete random variable
        - May only take on a finite number of values or countable number of values
        - Result of a count
    - Continuous random variable 
        - May take on any number of values in a line interval
        - Measured on a continuous scale

- Describe for numerical data
    - Centre: Discuss where the middle of the data falls
        - Measures of central tendency
        - mean, median and mode
    - Spread: Discuss how spread out the data is
        - Refers to the variability in the data
        - Range, standard deviation, IQR
    - Shape: Refers to the overall shape of the distribution
        - Symmetrical, uniform, skewed, or bimodal
    - Unusual Occurrences like Outliers (value that lies away from the rest of the data), Gaps and Clusters
    - Contextualize using **correct statistical vocabulary** and complete sentences.

- Trimmed mean: remove outliers from a data set
    - Use case eg.: 
        - Example Olympic Diving/Gymnastics scoring: eliminate extreme scores/bias from judges.
    - Not often used for large datasets
    - Calculate as per:
        1. Multiply the percent to trim by n (number in the sample)
        1. Truncate that many observations from BOTH ends of the distribution (when listed in order)
        1. Calculate the mean with the shortened data set
        - Eg.: `12, 14, 19, 20, 22, 24, 25, 26, 26, 50`
            - Mean: 23.8
            - 10% trimmed = 10%(10) = 1
            - Removed trimmed observation (1) of each side:
            ~~12~~, `14, 19, 20, 22, 24, 25, 26, 26`, ~~50~~
            - Trimmed mean = (14, 19, 20, 22, 24, 25, 26, 26)/8 = 22

- Methods of Variability/Dispersion Measurement
    - Commonly used: Range, variance, standard deviation, interquartile range, coefficient of variation etc.
    - 3 data sets can have the samen mean and meddian, but different amounts of variability.
- Types of Variation:
    - Systematic Variation
        - Differences in performance created by a specific experimental manipulation.
    - Unsystematic Variation
        - Differences in performance created by unknown factors.
        - Age, gender, IQ, time of day, measurement error, etc.
    - Randomization
        - Minimizes unsystematic variation.

- Degrees of freedom
    - - **DF = number of items - 1**
    - Is the number of independent pieces of information that went into calculating the estimate. 
    - Another way to look at degrees of freedom is that they are the number of values that are free to vary in a data set. 
    - Or the number of values that need to be known in order to know all the values needed to achieve a particular value.
    - If you have two samples and want to find a parameter, like the mean, you have two “N”s to consider (sample 1(N1) and sample 2(N2)).
        - DF in that case is: (N1 + N2) – 2.
    
- Measures of Variability:
    - Interquartile range advantage over the standard deviation:
        - IQR is resistant to extreme values
    - Interquartile range (IQR) is the range of the middle half of the data.  
    - Lower quartile (Q1) is the median of the lower half of the data
    - Upper quartile (Q3) is the median of the upper half of the data

 - Which Descriptive Statistic to use? (***Key slide***)
    - Depends on measurement type and data dispersion
    - Interval or Ratio (Scale)
        - Normally distributed
            - Mean and Standard Deviation 
        - Skewed
            - Median and Interquartile Range 
        - Ordinal or nominal
            - Mode and/or simple frequencies

- Analysing Data
    - First step: Graph the data
    - Frequency Distributions (aka Histograms)
    - Ideal: The ‘Normal’ Distribution (Bell-shaped, Symmetrical around the centre)

- Properties of Frequency Distributions: Skew, Kurtosis
- Probability: Chance behaviour is unpredictable in the short term, but has a regular and predictable pattern in the long term.
- Sample Space: The set of all possible outcomes of a random phenomenon
- Event: Any set of outcomes of interest
- Probability of an event: The relative frequency of this set of outcomes over an infinite number of trials
- **P(A)** is the probability of **event A**
    - P(X = 1) refers to the probability that the random variable X is equal to 1.
    - P(X<=x) is a Cumulative probability. The probability that a value falls within a particular range or interval
- Discrete Random Variable
    - The sum of all assigned probabilities must be 1
    - Mean is often called the expected value
        - Represents a cluster point for the entire distribution
    - Standard deviation is represented as a measure of risk
        - Larger the standard deviation, the more likely it is that a random variable x is different from the expected value
- Discrete Probability Distribution
    - Shows us the complete space on which the distribution is based
    - The corresponding probability of each event in the sample space
- Probability Distributions
    - Flipping a coin twice. Possible outcomes: HH, HT, TH, and TT.
        - If X is number of Heads resulted, thus X can take on the values 0, 1, or 2. 
        - X is a **random variable** because its value is determined by the outcome of a **statistical experiment**.
    - is a table or an equation that links each outcome of a statistical experiment with its probability of occurrence.
    
    | Number of heads(X)    | Probability   | 
    | :---:                 | :---:         |
    | 0                     | 0.25          | 
    | 1                     | 0.50          | 
    | 2                     | 0.25          |
    
    - Probability of X=the number of Heads that result from this experiment
    - A cumulative probability refers to the probability that the value of a random variable falls within a specified range.
    - If we flip a coin two times, what is the probability that the coin flips would result in one or fewer heads? Cumulative probability: 
        - `P(X < 1) = P(X = 0) + P(X = 1) = 0.25 + 0.50 = 0.75`
    
    | Number of heads(X)    | Probability:P(X = x) | Cumulative Probability:P(X < x) | 
    | :---:                 | :---:                | :---:                           |
    | 0                     | 0.25                 | 0.25                            |
    | 1                     | 0.50                 | 0.75                            |
    | 2                     | 0.25                 | 1.0                             |

    - The simplest probability distribution occurs when all of the values of a random variable occur with equal probability. 
    - Suppose the random variable X can assume k different values. 
    - Therefore, If *P(X=x<sub>k</sub>)* is constant, then, *P(X=x<sub>k</sub>)=1/k*
    - What is the probability that the die will land on 5?
        - Possibilities: *S = { 1, 2, 3, 4, 5, 6 }*
        - Thus, we have a **uniform distribution**. Therefore, the *P(X=5)=1/6*.
    - what is the probability that the die will land on a number that is smaller than 5?
        - **Cumulative probability**:
            - *P( X < 5 ) = P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4) = 1/6 + 1/6 + 1/6 + 1/6 = **2/3***

    - **Continuous Probability Distribution**: When a random variable is a **continuous variable** (variable can take on any value between two specified values).
    - cannot be expressed in tabular form
        - An equation or formula (probability density function) is used
    - **Hypothesis testing** relies extensively on the idea that, having such a function, one can compute the probability of all the corresponding events i.e.
        - probability of a X taking a value less than or equal to a particular value (a)

- Calculating Probability from a Frequency distribution
    - Statisticians have created a range of idealized distributions probability distributions and from these we can calculate the likelihood of achieving particular values if our data distribution matches. 
        - If we have data shaped like the normal distribution then the mean can be mapped to 0 and the standard deviation to 1
        - We can then use the tables of probability created by these statisticians to work out the probability of particular scores occurring within that distribution
        - **z-scores** has a mean of 0 and SD = 1
            - Z score states the position of a raw score in relation to the mean of the distribution, using the standard deviation as the unit of measurement.
                - Z = (Raw score - mean) / SD
            - For population: 
                - Z = (X - μ) / σ
            - For sample: 
                - Z = (X -  x̅) / s
            - z-scores  transform our original IQ scores into scores with a mean of 0 and an SD of 1.
            - Raw IQ scores (mean = 100, SD = 15)
            - z for 100 = (100-100) / 15 = 0, 	z for 115 = (115-100) / 15 = 1,
            - z for 70 = (70-100) / -2, etc.
            ![Z-Score](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/zScores.png)
            
            - The probability that a realization is lower than point 2.33 = 0.99
                - (See on internet Table of the Normal Distribution)
            - Use case of **z-score**:
                - Test A: Fred scores 78. Mean score = 70, SD = 8.
                - Test B: Fred scores 78. Mean score = 66, SD = 6.
                - Did Fred do better or worse in comparison to the rest of the class on the second test?
                - Test A: as a z-score, z = (78-70) / 8   = 1.00
                - Test B: as a z-score , z = (78 - 66) / 6 = 2.00
                - Conclusion: Fred comparatively did much better on Test B.
                ![Z-Score Example 1](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/zScoreExample1.png)
                - z-scores enable us to determine the relationship between one score and the rest of the scores, using just one table for all normal distributions.
                - Eg 2: If we have 480 scores, normally distributed with a mean of 60 and an SD of 8, how many would be 76 or above?
                    ![Z-Score Example 2](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/zScoreExample2.png)
                    - Work out the z-score for 76:
                    - *z = (X - x̅) / s = (76 - 60) / 8 = 16 / 8 = 2.00*
                    - We need to know the size of the area beyond z.
                    - Looking at the table, we find 
                    
                    | Z     | (a) Area btw Mean and Z | (b) Area beyond Z |
                    | :---: | :---:                   | :---:             |
                    | 2.00  | 0.4772                  | 0.0228            |

                    ![Z-Score Example Table](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/zScoreExample2table.png)

                    - So: as a proportion of 1, 0.0228 of scores are likely to be 76 or more.
                    - As a percentage, = 2.28%
                    - As a number,  0.0228 * 480  = 10.94 scores.
                - Eg 3: Word comprehension test scores:
                    - Person with no brain damage: no. correct: mean = 92, SD = 6 out of 100
                    - Brain-damaged person: no. correct: 89  out of 100.
                    - Is this person's comprehension significantly impaired?
                    - Step 1: Graph the problem:
                    ![Z-Score Example 3](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/zScoreExample3.png)
                    - Step 2: Convert 89 into a z-score:
                        - *z = (89 - 92)/6 =  - 3/6  = -0.5*
                    - Step 3: use the table to find the "area beyond z" for our z of - 0.5:
                        - Area beyond z = 0.3085
                    - **Conclusion**: .31 (31%) of people without brain damage are likely to have a comprehension score this low or lower.

- The Normal Distribution
    - Normal Curve, Bell-shaped Curve or Gaussian distribution
    - It's symmetrical around the mean.
    - The mean, median and mode all have same value.
    - It can be specified completely, once mean and SD are known.
    - The area under the curve is directly proportional to the relative frequency of observations.
        - Thus we can calculate the probability of observations occurring in a population
    The Empirical Rule
    - 68% of the observations fall within σ of the mean µ.
    - 95% of the observations fall within 2σ of the mean µ.
    - 99.7% of the observations fall within 3σ of the mean µ.
    ![SD Empirical Rule](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/sdEmpiricalRule.png)
    - Z-Score properties:
        - 1.96 cuts off the top 2.5% of the distribution.
        - −1.96 cuts off the bottom 2.5% of the distribution.
        - As such, 95% of z-scores lie between −1.96 and 1.96.
        - 99% of z-scores lie between −2.58 and 2.58,
        - 99.9% of them lie between −3.29 and 3.29. 

- Distribution is central to choosing the correct test
    - Parametric Tests
        - Normal distribution
    - Non-parametric Tests
        - Non normal distribution
    - Always start by looking at the data!

- Population
    - The collection of units (be they people, plankton, plants, cities, suicidal authors, etc.) to which we want to generalize a set of findings or a statistical model
- Sample
    - A smaller (but hopefully representative) collection of units from a population used to determine truths about that population

- ***outcome<sub>i</sub>=(model)+error<sub>i</sub>***
    - In statistics we fit models to our data 
    - The mean is a hypothetical value 
        - As such, the mean is simple statistical model.
    - How can we assess how well the mean represents reality?
        - Calculating ‘Error’:
            - ***deviation** = x<sub>i</sub> - x̅*
            Total Error: (sum the deviations)
                - *Σ(x<sub>i</sub> - x̅)*
                - We could add the deviations to find out the total error.
                - Deviations cancel out because some are positive and others negative. 
                - Therefore, we square each deviation. 
                - *SS=Σ(x<sub>i</sub> - x̅)<sup>2</sup>*
        - **Variance:**
            - The sum of squares is a good measure of overall variability, but is dependent on the number of scores.
            - We calculate the average variability by dividing by the number of scores (n).
            - This value is called the variance (s2).
            - *variance(s<sup>2</sup>) = SS/N-1 = Σ(x<sub>i</sub> - x̅)<sup>2</sup>/N-1*
            - The variance has one problem: it is measured in units squared.
            - This isn’t a very meaningful metric so we take the square root value (measured in units).
            - This is the standard deviation (s).
        - **Standard Deviation**
            - ![SD Formula](https://raw.githubusercontent.com/bambrozio/academic-corner/master/dit/MScDataAnalytics/probabilityAndStatisticalInference/img/sdFormula.png)

- Important to remember:
    - The sum of squares, variance, and standard deviation represent the same thing:
    - The ‘fit’ of the mean to the data
    - The variability in the data
    - How well the mean represents the observed data
    - Error

- Standard error of the mean (SE)
    - **When you calculate the Standard Deviation of sample means
        - means of many samples of the same Population, in order to estimate the mean of the entire population
    - Central Limit Theorem
        - As samples get large, the sampling distribution has a normal distribution with a sample mean equal to the population mean and a standard deviation of
            - ***σ<sub>x̅</sub>=S / √N̅***
        - We can use the standard deviation of the sampling distribution as the approximation of the sample error
            - If our distribution follows the normal distribution

- Confidence Intervals (CI)
    - CI represents a range of values between which we think a population value will fall
    - Eg.: Suppose we are looking at our fish in Lough Mask
        - True mean: 15 thousand fish
        - Sample mean: 17 thousand fish
        - Interval estimate: 
            - 12 to 22 thousand(contains true value)
            - 16 to 18 thousand (misses true value)
            - CIs constructed such that 95% contain the true value.
    - Typically look at 95% CI but can also look at 99%
    - What does  this mean?
        - If we say CI is 95% then if we collected 100 samples, calculated the mean 
        - Then a CI of 95% means we are confident that 95 of these would contain the true mean
    - How to calculate?
        - Need to know the limits within which 95% of the means fall
        - Go back to the normal distribution – 95% of scores fall between  +-1.96 
        - Once we know the mean and standard deviation we can calculate any score and therefore the CI
            - Lower boundary: ***X̅=1−SE***
            - Upper boundary: ***X̅= 1+SE***

- Graphical presentation: (***Key slide***)
    - Nominal or Ordinal: 
        - Bar charts, Pie charts or Frequency Tables
    - Interval or Ratio numerical: 
        - Histogram, Stem and Leaf  diagrams or Box-plot 
            - Depending on dispersion

    - Stem-and-Leaf plot
        - Shows data arranged by place value. 
        - You can use a stem-and-leaf plot when you want to display data in an organized way that allows you to see each value.
            - Use for small to moderate sized data sets.
        - Accompany with a comment on the centre, spread, and shape of the distribution and if there are any unusual features.

    - Histogram
        - Use for univariate numerical data (one variable)
        - To compare two or more histograms, use the same scale on the horizontal axis
        - Describe it as per example:
        - "The median number of hours spent watching TV per day was greater for the 1-year-olds than for the 3-year-olds. The distribution for the 3-year-olds was more strongly skewed right than the distribution for the 1-year-olds, but the two distributions had similar ranges."
        


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