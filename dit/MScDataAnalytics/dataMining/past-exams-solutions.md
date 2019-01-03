Explain the following terms, clearly distinguishing the differences between them, in relation to data analytics,
data mining and machine learning:
• Descriptive Analytics
• Predictive Analytics
• Prescriptive Analytics
[15 marks]

```
Data Analytics is the discovery and communication of meaningful patterns in data. It’s not the data but the signals buried in and inferred from data. In this context, Data Mining is used as a sort of tools to extract meaningful information from the data and Machine Learning is one of the Data Mining methods available to be used in each analytics stage.
Descriptive Analytics, Predictive Analytics and Prescriptive Analytics are distinct types of analytics, which in summary tries to explain, respectively, "What happened", "What is likely to happen" and "Why did it happen".

Descriptive analytics is a preliminary stage of data processing that creates a summary of historical data to yield useful information and possibly prepare the data for further analysis. Data aggregation and data mining methods organize the data and make it possible to identify patterns and relationships in it that would not otherwise be visible. Querying, reporting and data visualization may be applied to yield more insight.

Predictive analytics is a form of advanced analytics that uses both new and historical data to forecast activity, behaviour and trends. It involves applying statistical analysis techniques, analytical queries and automated machine learning algorithms to data sets to create predictive models that place a numerical value (or score) on the likelihood of a particular event happening.

Prescriptive analytics is the area of business analytics (BA) dedicated to finding the best course of action for a given situation. It's related to both descriptive and predictive analytics. It seeks to determine the best solution or outcome among various choices, given the known parameters. It can also suggest decision options for how to take advantage of a future opportunity or mitigate a future risk, and illustrate the implications of each decision option.
```

When investigating data you need to look at data at many different levels. For each of the following, explain
what information you would be looking at, what are the typical issues and how you would address the issues.
§ Attribute data
§ Related data across attributes
§ Record level data
Illustrate your answers with example data issues that exists in the following table.

```
Data Understanding is the stage II of CRISP-DM. Here's where pretty much all data investigation is conducted and addressed. It has 4 main sub-items: 
- Describe Data: Describe the data that has been acquired including its format, its quantity, the identities of the fields and any other surface features which have been discovered. Evaluate whether the data acquired satisfies your requirements.
- Explore Data: 
    - Distribution of key attributes
    - Relationships between pairs or small numbers of attributes
    - Results of simple aggregations
    - Properties of significant sub-populations
    - Simple statistical analyses
- Verify Data Quality 
    - Is the data complete?
    - Is it correct, or does it contain errors and, if there are errors, how common are they?
    - Are there missing values in the data? If so, how are they represented, where do they occur, and how common are they?
- Data Quality Report.
List the results of the data quality verification. If quality problems exist, suggest possible solutions. Solutions to data quality problems generally depend heavily on both data and business knowledge
```

Explain how the Random Forests algorithm works for both the building of the model and the scoring of the
data.
```
Random Forest is a supervised learning algorithm. It creates a forest and makes it random. The "forest" it builds, is an ensemble of Decision Trees, most of the time trained with the "bagging" method. The general idea of the bagging method is that a combination of learning models increases the overall result.
To say it in simple words: Random forest builds multiple decision trees and merges them together to get a more accurate and stable prediction.
One big advantage of random forest is, that it can be used for both classification and regression problems, which form the majority of current machine learning systems.
```

