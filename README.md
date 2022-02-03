Table of Contents 
=================
* [Installation](#installation) 
* [Project Motivation](#project-motivation) 
* [File Descriptions](#file-descriptions) 
* [Licensing, Authors, and Acknowledgements](#licensing,-authors,-and-acknowledgements) 

## Installation

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`


## Project Motivation 
For this project, I was interestested to build a model for an API that classifies disaster messages.
At first I analysed real messages that were sent during disaster events, taken from Figure Eight.  
Then I categorize those events by implementing a machine learning pipeline.  
Finally, I created a web app, where user can input a new message and get back classification results in several categories.  This web app, 
additionally displays visualisations of the data.

## File Descriptions 
The hierarchy of the project is 

- app
| - template
| |- master.html  # main page of web app
| |- go.html  # classification result page of web app
|- run.py  # Flask file that runs app

- data
|- disaster_categories.csv  # data to process 
|- disaster_messages.csv  # data to process
|- process_data.py
|- InsertDatabaseName.db   # database to save clean data to

- models
|- train_classifier.py
|- classifier.pkl  # saved model 


## Licensing, Authors, Acknowledgements 
Must give credit to Figure Eight for the data. You can find the Licensing 
for the data and other descriptive information [here](https://github.com/SimplifyData/Disaster-Response-with-Figure-Eight/blob/master/LICENSE). 
Otherwise, feel free to use the code here as you would like!
