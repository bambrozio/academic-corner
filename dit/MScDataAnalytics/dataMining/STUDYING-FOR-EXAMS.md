# Class 1

## Data Mining.
It's the non-trivial extraction of previously unknown and potentially useful information from data. Exploration & Analysis, by automatic, or semi-automatic means, of large quantities of data in order to discover meaningful patterns.

### Data Mining (Method + Applications)
DM: It does look at defining the business question being investigated, what data is related to that question, understanding that data, indentifying appropriate techniques to use (eg.: ML), analysing the results generated to apply domain knownledge, being able to related this back to the business, understanding how the results/models etc can be incorporated into the business processes, and monitor & updating the processes based on their performance on live data.

- the practice of examining large pre-existing databases in order to generate new information
- Data mining is the process of discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems.
- Data mining is an interdisciplinary subfield of computer science and statistics with an overall goal to extract information (with intelligent methods) from a data set and transform the information into a comprehensible structure for further use.
- Data mining is the analysis step of the "knowledge discovery in databases" process, or KDD.
- The difference between data analysis and data mining is that data analysis is to summarize the history such as analyzing the effectiveness of a marketing campaign, in contrast, data mining focuses on using specific machine learning and statistical models to predict the future and discover the patterns among data.

## Machine Learning (Theory + Methods)
Focuses on the algorithms, how these work, how they can be customised, how they can be tuned, finding or discovering how they can be used in new situations.
ML is only one component of DM.

## Data Analytics
is the discovery and communication of meaningful patterns in data. It’s not the data but the signals buried in and inferred from data. In this context, Data Mining is used as a sort of tools to extract meaningful information from the data and Machine Learning is one of the Data Mining methods available to be used in each analytics stage.
Descriptive Analytics, Predictive Analytics and Prescriptive Analytics are distinct types of analytics, which in summary tries to explain, respectively, "What happened", "What is likely to happen" and "Why did it happen".

## Descriptive Analytics
Descriptive analytics is a preliminary stage of data processing that creates a summary of historical data to yield useful information and possibly prepare the data for further analysis. Data aggregation and data mining methods organize the data and make it possible to identify patterns and relationships in it that would not otherwise be visible. Querying, reporting and data visualization may be applied to yield more insight.

## Predictive Analytics
Predictive analytics is a form of advanced analytics that uses both new and historical data to forecast activity, behaviour and trends. It involves applying statistical analysis techniques, analytical queries and automated machine learning algorithms to data sets to create predictive models that place a numerical value (or score) on the likelihood of a particular event happening.

## Prescriptive Analytics
Prescriptive analytics is the area of business analytics (BA) dedicated to finding the best course of action for a given situation. It's related to both descriptive and predictive analytics. It seeks to determine the best solution or outcome among various choices, given the known parameters. It can also suggest decision options for how to take advantage of a future opportunity or mitigate a future risk, and illustrate the implications of each decision option.

---

# Class 2

## Data Mining Life Cycle

### Knowledge Discovery in Databases (KDD) Process
{Data} -> Selection -> {Target Data} -> Preprocessing -> {Preprocessed Data} -> Transformation -> {Transformed Data} -> Data Mining -> {Patterns} -> Interpretation / Evaluation -> {Knowledge}.

1. Learning the application domain
- Relevant prior knowledge and goals of application
2. Creating a target data set: data selection
3. Data cleaning and preprocessing
- May take 70% of effort!
4. Data reduction and transformation
- Find useful features, dimensionality/variable reduction
5. Choosing functions of data mining
- Classification, regression, clustering, etc.
6. Choosing the mining algorithm(s)
7. Data mining: search for patterns of interest
8. Pattern evaluation and knowledge presentation
- Visualization, transformation, removing redundant patterns, etc.
9. Use of discovered knowledge.

## CRISP-DM
CRISP-DM stands for cross-industry process for data mining. The CRISP-DM methodology provides a structured approach to planning a data mining project. It is a robust and well-proven methodology. We do not claim any ownership over it.

1. Buisiness Understanding
- understand what you want to accomplish from a business perspective.
- What are the desired outputs of the project?
    - Set objectives, Produce project plan, Business success criteria
- Assess the current situation
    - Inventory of resources
    - 
2. Data Understanding
- requires you to acquire the data listed in the project resources.
3. Data Preparation
4. Modelling
5. Evaluation
6. Deployment