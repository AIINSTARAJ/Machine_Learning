## The  implementation of regressional analysis as an application of supervised machine learning  in the prediction of prices of laptop computers based on specifications.

### * 1. The first step in this project is the analysis of the project.

* The first step in this is data gathering and how do we do this. We simply perform  a method of computation called web scraping i.e we try to get various prices of pc and their diverse specifications from the web through libraries like beautifulsoup4 and selenium.
* The next step on this is implementing a concept called data processing and organization. Due to large data being scraped from the web, there is high need  we perform data processing on the scraped data for filtering out or replacing incomplete data or non  important data. We will mainly implement this in python pandas library, a well known library for analysis.
* Due to specifications like processor type and certain other factors, there is a need to convert this categorical data into numerical form in order for developing the model as regressional models most often works well with numerical data. This categorical data will be converted to numerical data in OneHotEncoder a method for converting categorical data into numerical data.
* After getting the data in a refined format, for optimization purposes there is a need to split the data into training and testing set  for accuracy evaluation .
* The next procedure is developing the model using LinearRegression, a class in sklearn.linear_model() and fitting the data into the model.
* Testing and evaluating the model such as minimizing the mean-squared error value and increasing he learning rate of the mode. This is highly crucial and important as accuracy is highly important.
* Finallly, the development of a web interface for users to nterface with the modell and get prices of laptop computers according to specifications.

### * 2. Project Structures and directory creation.

* The basic directory structure

  ![1723764599825](image/readme/1723764599825.png)
* > The "scrap.py" is the python file for performing the web scraping function.
  >
* > The "preprocess.py" is the python code for the data processing, validation and for he conversion of the categorical data into numerical data as well as for splitting the train and test data sets.
  >
* > The "models.py" contains the code for deveoping the model and evaluating the performance of the model
  >
* > The "app.py" is the python file for the flask web app development and deveoping the interface.
  >
* > The "resources" contains set of assets and resources such as the data, the csv files, the spreadsheets, the databases as well as the app templates files and extra materials.
  >

### * 3. Activating the virtual environment and installing the python packages.

* To activate the virtual environment head over to the Command Prompt in windows or terminal in MacOs or Linux and navigate to your project directory then run this

```bash
python -m venv virtual_env
```

    This will create the directory machine_learning virtual environment.

    Once you’ve created a virtual environment, you may activate it.

    On Windows, run:

```bash
virtual_env\Scripts\activate.bat
```

    On Unix or MacOS, run:

```bash
source virtual_env/bin/activate
```

    The next step is installing the python packages.

    Here are the packages we need:

* beautifulsoup4
* pandas
* sklearn
* pickle
* flask

  So we then create a new file in our directory named requirements.txt copy the packages list and paste into the "requirements.txt"

  Then run

```bash
pip install -r requirements.txt
```

    This should install the required packages

### * 4.  Getting Started with data gathering and web scraping.

    One most important thing is getting started is source of data but no instea of manual collection, we could instead automate the tasks by performing web scraping of popular sites like Amazon and other e-commerce laptop stores for getting the prices and specifications of laptops.

  That method looks great right but how about a unique method that combines Artificial Intelligence aand web scraping. This method would yield more efficient data gathered.
