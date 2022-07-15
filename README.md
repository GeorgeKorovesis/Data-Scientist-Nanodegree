Table of Contents 
=================
* [Installation](#installation) 
* [Project Motivation](#project-motivation) 
* [Project Motivation](#file-descriptions) 
* [Results](#results) 
* [Licensing, Authors, and Acknowledgements](#licensing,-authors,-and-acknowledgements) 

## Installation
There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.

## Project Motivation 
For this project, I was interested, based on transaction, demographic and offer data, to determine which demographic groups respond best to which offer type. The data set I used, is a simplified version of the real Starbucks app because the underlying simulator only has one product whereas Starbucks actually sells dozens of products. I was interested in questions such as:
Which offer type do customers mostly respond to? Do people with lower income respond more to offers? Are customers of specific gender more likely to  accept an offer? Do younger people accept more offers? Are newer members more likely to accept any offer than older ones?

## File Descriptions 
There is 1 notebook available here to showcase work related to the above questions. The notebook is exploratory enough in searching through the data pertaining to the questions showcased by the notebook title. Markdown cells were used to assist in walking through the thought process for individual steps.
There is also one ready to use offer_data file that provides the full cleaned data, which can be loaded to a new dataframe as 
df = pd.read_pickle('offer_data').
There are also provided 3 json files provided, profile.json, portfolio.json and transcript.json, which contain the full dataset needed for this study. Below there is a Data Dictionary of each file.


Data Dictionary
====================================================================
profile.json
Rewards program users (17000 users x 5 fields)

gender: (categorical) M, F, O, or null
age: (numeric) missing value encoded as 118
id: (string/hash)
became_member_on: (date) format YYYYMMDD
income: (numeric)

====================================================================
portfolio.json
Offers sent during 30-day test period (10 offers x 6 fields)

reward: (numeric) money awarded for the amount spent
channels: (list) web, email, mobile, social
difficulty: (numeric) money required to be spent to receive reward
duration: (numeric) time for offer to be open, in days
offer_type: (string) bogo, discount, informational
id: (string/hash)

====================================================================
transcript.json
Event log (306648 events x 4 fields)

person: (string/hash)
event: (string) offer received, offer viewed, transaction, offer completed
value: (dictionary) different values depending on event type
offer id: (string/hash) not associated with any "transaction"
amount: (numeric) money spent in "transaction"
reward: (numeric) money gained from "offer completed"
time: (numeric) hours after start of test

====================================================================

## Results 
The main findings of the code can be found at the post available here.

## Licensing, Authors, Acknowledgements 
Must give credit to Starbucks for the data. You can find the Licensing for the data and other descriptive information at the Kaggle link available here. Otherwise, feel free to use the code here as you would like!
