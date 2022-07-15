Table of Contents 
=================
* [Installation](#installation) 
* [Project Motivation](#project-motivation) 
* [File Descriptions](#file-descriptions) 
* [Results](#results) 
* [Licensing, Authors, and Acknowledgements](#licensing,-authors,-and-acknowledgements) 

## Installation
There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python. The code should run with no issues using Python versions 3.*.

## Project Motivation 
For this project, I was interested, based on transaction, demographic and offer data, to determine which demographic groups respond best to which offer type. The data set I used, is a simplified version of the real Starbucks app because the underlying simulator only has one product whereas Starbucks actually sells dozens of products. I was interested in questions such as:
Which offer type do customers mostly respond to? Do people with lower income respond more to offers? Are customers of specific gender more likely to  accept an offer? Do younger people accept more offers? Are newer members more likely to accept any offer than older ones?

## File Descriptions 
There is 1 notebook available here to showcase work related to the above questions. The notebook is exploratory enough in searching through the data pertaining to the questions showcased by the notebook title. Markdown cells were used to assist in walking through the thought process for individual steps. <br/>
There is also one ready to use file with name 'offer_data', that contains the full cleaned data, which can be loaded to a new dataframe as 
```
df = pd.read_pickle('offer_data')
```
There are also provided 3 json files provided, profile.json, portfolio.json and transcript.json, which contain the full dataset needed for this study.
The schema and explanation of each variable in all 3 files, can be found in the notebook.

## Results 
The main findings of the code can be found at the post available here.

## Licensing, Authors, Acknowledgements 
Must give credit to Starbucks for the data. Feel free to use the code here as you would like!

