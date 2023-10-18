# Loan-Default-Prediction.

![Alt text](<Loan image.webp>)

## Group Members
* Killion Mokaya
* Derrick Wekesa
* James Murigi
* Brenda Mutai
* William Ndoni
* Franklin Muchiri

# Introduction

Financial sector has emerged as the benchmark in leveraging the potential of data analtytics and machine learning to not only improve operations but to also proactively minimise the risks.

Our primary goal is to use data science tool as predictive modelling to build a strong framework capable of predicting loan outcomes.Our technique has the potential to help financial institutions to make more informed lending decisions.

SuperLender uses data driven a data-driven  approach to assess the credit risk of its customers and determine  the two fundermental drivers of repayment; `willingness` and `ability`.We will explore how SuperLender uses machine learning models to predict loan outcomes and evaluate their performance.


# Business Understanding

Defaulting borrowers cause significant financial losses, impacting profit margins and liquidity ultimately affecting long-term business sustainability. Moreover, loan defaults can tarnish a company's reputation, erode investor confidence, and hinder future borrowing opportunities. 

Super Lender a local digital lending company seeks to provide effective credit risk model which determines borrower’s chances of repaying a loan. In this project we seek to develop a credit risk model employing machine learning techniques. The model assesses historical data to predict potential defaults, enabling proactive risk management. Also the model informs credit manager and the institution’s employees on borrower important details to enable data driven decisions not only to deny or advance a loan  but targeted strategies, including personalized loan terms.

# Problem Statement

A defaulted loan is an expense to the business. There is a need for financial institutions to enhance their risk assessment strategies and only lend responsibly.  As such predicting customer loan defaults is central to minimizing financial risks and ensuring sustainable lending practices. Chances of customer paying their loan are influenced by demographics and past financial details. The challenge is for financial institutions to distinguish customers who can pay loans and only lend to them.

## Main Objective

To develop a model which predicts customer loan repayment chances.

## Specific Objective

* Determine which demographic factors affects customer loan repayment chances.
*	Determine which past financial details and behavior affects customer loan repayment chances
*	To develop a UI which informs credit manager on customer’s loan repayment details. 

# Data Understanding

The loan default prediction project uses three datasets from Zindi, a platform for data science competitions. The datasets are:
* Demographic data: Contains 4,346 rows and 9 columns.
* Performance data: Contains 4,368 rows and 10 columns.
* Previous loans data: Contains 18,183 rows and 12 columns.

> Demographic Data: It has customer identification and demographics that include birthdate,bank account information, geographic location, bank name and branch, employment status and level of education.

> Performance Data: The details about loan performance include loan identification, loan approval date, loan amount, total amount due,term duration, information about referrals and a classification indicating ‘good’meaning loan settled on time or ‘bad’ loan

> Previous Loans Data: This has details of historical information about previous loans, including loan identification, loan approval date, creation date, loan amount, total amount due, loan closure date, information about referrals and dates related to the first due payment and the first payment made.


# Data Preparation
Within our data preparation phase, we perfommed the following tasks:
* Data cleaning
* Checking missing values and filling missing values
* checking for outliers
* Checking for duplicates

# Exploratory Data Analysis

We examined our dataset thoroughly during the exploratory data analysis (EDA) phase of the project. This EDA method included univariate analysis, which focused on individual factors, bivariate analysis, which looked at correlations between pairs of variables, and multivariate analysis, which looked at complicated interactions between many variables. 

# Modeling

The project evaluated two loan default prediction models: Logistic Regression and Decision Trees. Logistic Regression achieved an accuracy of 84% and a balanced trade-off between precision and recall. It could spot loan defaults 88% of the time while not missing many, and 81% of the time for non-default loans. Decision Trees, on the other hand, had exceptional precision and recall scores of 97% and 98% for both default and non-default loans, resulting in an impressive 98% overall accuracy.

# Conclusions

* High Accuracy: The model achieved accuracy levels exceeding 99%, minimizing financial risks for lending institutions
* Lending institutions can benefit from improved risk assessment, minimizing financial risks and optimizing lending decisions with the model's accurate predictions.
* The development of a user-friendly web app using Streamlit has greatly improved accessibility to the model, enhancing its value for lending professionals and stakeholders.
* Continuous updates to the model through the web app enhance its adaptability to changing market conditions.


# Recommendations

* Implement a structured plan for continuous model maintenance, including regular updates and retraining to keep it relevant.
* Provide training and guidelines to users of the web app to ensure they make the most of the model's insights.
* Establish robust data quality assurance processes to ensure data accuracy and consistency, crucial for model performance.
* Conduct periodic risk assessments to ensure that the model aligns with the evolving lending landscape.
* Create a feedback mechanism within the web app to gather insights from users for model improvement.
* Implement stringent data security measures to protect sensitive information used by the model.





