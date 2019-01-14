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
CRISP-DM stands for cross-industry process for data mining. The CRISP-DM methodology provides a structured approach to planning a data mining project. It is a robust and well-proven methodology.

1. Buisiness Understanding
- understand what you want to accomplish from a business perspective.
- What are the desired outputs of the project?
    - Set objectives, Produce project plan, Business success criteria
- Assess the current situation
    - Inventory of resources
    - Requirements, assumptions and constraints
    - Risks and contingencies
    - Terminology
    - Costs and benefits
- Determine data mining goals
    - Business success criteria
    - Data mining success criteria
- Produce project plan
    - Project plan
    - Initial assessment of tools and techniques
2. Data Understanding
- Initial data collection report 
- Describe data
    - Data description report
- Explore data

- requires you to acquire the data listed in the project resources.
3. Data Preparation
4. Modelling
5. Evaluation
6. Deployment

---

## Clustering
Clustering is a Machine Learning technique that involves the grouping of data points. Given a set of data points, we can use a clustering algorithm to classify each data point into a specific group. In theory, data points that are in the same group should have similar properties and/or features, while data points in different groups should have highly dissimilar properties and/or features. Clustering is a method of unsupervised learning and is a common technique for statistical data analysis used in many fields. Cluster analysis itself is not one specific algorithm, but the general task to be solved. It can be achieved by various algorithms that differ significantly in their understanding of what constitutes a cluster and how to efficiently find them. 

### Types of clusters: 
####  Well-Separated Clusters:
§ A cluster is a set of points such that any point in a cluster is closer (or more similar) to every other point in the cluster than to any point not in the cluster. 

#### Center-based
§ A cluster is a set of objects such that an object in a cluster is closer (moresimilar) to the “center” of a cluster, than to the center of any other cluster
§ The center of a cluster is often a centroid, the average of all the points in the cluster, or a medoid, the most “representative” point of a cluster 

#### Contiguous Cluster (Nearest neighbor or Transitive)
§ A cluster is a set of points such that a point in a cluster is closer (or more similar) to one or more other points in the cluster than to any point not in the cluster.

#### Density-based
§ A cluster is a dense region of points, which is separated by low-density regions, from other regions of high density.
§ Used when the clusters are irregular or intertwined, and when noise and
outliers are present. 

#### Shared Property or Conceptual Clusters
§ Finds clusters that share some common property or represent a particular concept. 



5 popular clustering algorithms:
- K-Means Clustering
    - advantages: pretty fast, easy to implement. Linear complexity O(n). (Simply computes the distances between points and group centers)
    - disadvantages: have to select how many groups/classes there are. K-Medians is another algorithms by using median instead of means. Although more accurate in regarding outliers, it is much slower.
- Mean-Shift Clustering
    - Mean shift clustering is a sliding-window-based algorithm that attempts to find dense areas of data points. It is a centroid-based algorithm meaning that the goal is to locate the center points of each group/class, which works by updating candidates for center points to be the mean of the points within the sliding-window. These candidate windows are then filtered in a post-processing stage to eliminate near-duplicates, forming the final set of center points and their corresponding groups.
    - Find centers > remove overlaps > cluster points > start iterations > converged.
- Density-Based Spatial Clustering of Applications with Noise (DBSCAN)
    - DBSCAN is a density based clustered algorithm similar to mean-shift, but with a couple of notable advantages.
    - DBSCAN begins with an arbitrary starting data point that has not been visited. The neighborhood of this point is extracted using a distance epsilon ε (All points which are within the ε distance are neighborhood points).
    - If there are a sufficient number of points (according to minPoints) within this neighborhood then the clustering process starts and the current data point becomes the first point in the new cluster. Otherwise, the point will be labeled as noise (later this noisy point might become the part of the cluster). In both cases that point is marked as “visited”.
- Expectation–Maximization (EM) Clustering using Gaussian Mixture Models (GMM)
    1. We begin by selecting the number of clusters (like K-Means does) and randomly initializing the Gaussian distribution parameters for each cluster.
    2. Given these Gaussian distributions for each cluster, compute the probability that each data point belongs to a particular cluster.
    3. Based on these probabilities, we compute a new set of parameters for the Gaussian distributions such that we maximize the probabilities of data points within the clusters.
    4. Steps 2 and 3 are repeated iteratively until convergence, where the distributions don’t change much from iteration to iteration.
- Agglomerative Hierarchical Clustering
    - Hierarchical clustering algorithms actually fall into 2 categories: top-down or bottom-up. Bottom-up algorithms treat each data point as a single cluster at the outset and then successively merge (or agglomerate) pairs of clusters until all clusters have been merged into a single cluster that contains all data points. Bottom-up hierarchical clustering is therefore called hierarchical agglomerative clustering or HAC. This hierarchy of clusters is represented as a tree (or dendrogram).

# Classification
classification is a supervised learning approach in which the computer program learns from the data input given to it and then uses this learning to classify new observation. This data set may simply be bi-class (like identifying whether the person is male or female or that the mail is spam or non-spam) or it may be multi-class too. Some examples of classification problems are: speech recognition, handwriting recognition, bio metric identification, document classification etc.
- Linear Classifiers: Logistic Regression, Naive Bayes Classifier
    Naive Bayes: 
        A naive Bayes classifier is an algorithm that uses Bayes' theorem to classify objects. Naive Bayes classifiers assume strong, or naive, independence between attributes of data points. Popular uses of naive Bayes classifiers include spam filters, text analysis and medical diagnosis.
        Naive Bayes classifiers are highly scalable, requiring a number of parameters linear in the number of variables (features/predictors) in a learning problem. Maximum-likelihood training can be done by evaluating a closed-form expression, which takes linear time, rather than by expensive iterative approximation as used for many other types of classifiers.
    Logistic Regression:
        It is a statistical method for analysing a data set in which there are one or more independent variables that determine an outcome. The goal is to find the best fitting model to describe the relationship between the dichotomous characteristic of interest (dependent variable = response or outcome variable) and a set of independent (predictor or explanatory) variables.
- Support Vector Machines
    In machine learning, support-vector machines (SVMs, also support-vector networks[1]) are supervised learning models with associated learning algorithms that analyze data used for classification and regression analysis. Given a set of training examples, each marked as belonging to one or the other of two categories, an SVM training algorithm builds a model that assigns new examples to one category or the other, making it a non-probabilistic binary linear classifier.
- Decision Trees
    Decision tree builds classification or regression models in the form of a tree structure. It breaks down a data set into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes. A decision node has two or more branches and a leaf node represents a classification or decision. 
    How to split nodes/attributes
        § Gini Index
            § Can be understood as calculating how often the target levels of instances in a data
            set would be misclassified if predictions where made based on the distribution of
            the target levels in the data set
            § Can be computed by summing the probability of each item being chosen times the
            probability of a mistake in categorising that item
            § It reaches its minimum (Zero) when all cases in the node fall into a single target
            category
            § The attribute the provides the smallest gini split (or the largest reduction in impurity) is chosen to split the node.
- Boosted Trees
- Random Forest
    Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks, that operate by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees.
- Neural Networks
    A neural network consists of units (neurons), arranged in layers, which convert an input vector into some output. Each unit takes an input, applies a (often nonlinear) function to it and then passes the output on to the next layer. Generally the networks are defined to be feed-forward: a unit feeds its output to all the units on the next layer, but there is no feedback to the previous layer. Weightings are applied to the signals passing from one unit to another, and it is these weightings which are tuned in the training phase to adapt a neural network to the particular problem at hand.
    Input layer > Hidden layer (when added == Deep Learning) > output layer
    Neural Networks can be used for traditional classification and regression
    But very effective for Image, sound and complex objects
- K Nearest Neighbor
    The k-nearest-neighbors algorithm is a classification algorithm, and it is supervised: it takes a bunch of labelled points and uses them to learn how to label other points.
    In pattern recognition, the k-nearest neighbors algorithm (k-NN) is a non-parametric method used for classification and regression.[1] In both cases, the input consists of the k closest training examples in the feature space. The output depends on whether k-NN is used for classification or regression:
    In k-NN classification, the output is a class membership. An object is classified by a majority vote of its neighbors, with the object being assigned to the class most common among its k nearest neighbors (k is a positive integer, typically small). If k = 1, then the object is simply assigned to the class of that single nearest neighbor.
    In k-NN regression, the output is the property value for the object. This value is the average of the values of its k nearest neighbors

- Splitting the data set for Training and Testing: 
    60% - 70% (Training) 30% - 40% (Testing)

### Classification Accuracy Measures
Classification accuracy can be measured in many different ways
Two of the most popular are:
§ Classification / Misclassification rates
§ Other associated values
§ Primarily used for binary classification
§ Average squared error
§ Typically used with Regression / Prediction / Continuous values
§ Used in conjunction with Classification / Misclassification rates

The accuracy of a classifier on a given test set is the percentage of test set
tuples that are correctly classified by the classifier
§ Often also referred to as recognition rate
§ Error rate (or misclassification rate) is the opposite of accuracy

False positives vs false negatives
§ Related to type I and type II errors in statistics

## Prediction is different from classification
§ Classification refers to predict categorical class label
§ Prediction models continuous-valued functions

# Regression Measures
r-squared from 0 to 100%
In general, the higher the R-squared, the better the
model fits your data.

## Confusion Matrix
A confusion matrix is a table that is often used to describe the performance of a classification model (or "classifier") on a set of test data for which the true values are known. The confusion matrix itself is relatively simple to understand, but the related terminology can be confusing.

In a desease prediction example:
    - true positives (TP): These are cases in which we predicted yes (they have the disease), and they do have the disease.
    - true negatives (TN): We predicted no, and they don't have the disease.
    - false positives (FP): We predicted yes, but they don't actually have the disease. (Also known as a "Type I error.")
    - false negatives (FN): We predicted no, but they actually do have the disease. (Also known as a "Type II error.")

Accuracy: Overall, how often is the classifier correct?
(TP+TN)/total = (100+50)/165 = 0.91
Misclassification Rate: Overall, how often is it wrong?
(FP+FN)/total = (10+5)/165 = 0.09
equivalent to 1 minus Accuracy
also known as "Error Rate"
True Positive Rate: When it's actually yes, how often does it predict yes?
TP/actual yes = 100/105 = 0.95
also known as "Sensitivity" or "Recall"
False Positive Rate: When it's actually no, how often does it predict yes?
FP/actual no = 10/60 = 0.17
True Negative Rate: When it's actually no, how often does it predict no?
TN/actual no = 50/60 = 0.83
equivalent to 1 minus False Positive Rate
also known as "Specificity"
Precision: When it predicts yes, how often is it correct?
TP/predicted yes = 100/110 = 0.91
Prevalence: How often does the yes condition actually occur in our sample?
actual yes/total = 105/165 = 0.64

## Receiver Operating Characteristic (ROC) Curve:
This is a commonly used graph that summarizes the performance of a classifier over all possible thresholds. It is generated by plotting the True Positive Rate (y-axis) against the False Positive Rate (x-axis) as you vary the threshold for assigning observations to a given class.
originally used to make sense of noisy radio signals
§ Can be used to help us talk about classifier performance and determine the
best operating point for a classifier
ROC curves can be used to compare classifiers
§ The greater the area under the curve the more accurate the classifier