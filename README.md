# An Exploratory Data Analysis about Exoplanets

The purpose of this project is to understand a little bit more about exoplanets, which are basically planets that lay far beyond our Solar System and that orbit other stars. The programming goal is to emphasize on the importance of obtaining raw data to later infer valuable insights from it. It is focused on the laborious work of searching for the best data that can solve the problem. For demonstration purposes, I'm just going to do the Exploratory Data Analysis (EDA), but in a real-world scenario, these data could be used, for example, to feed a ML or DL algorithm.

The project development only consists of **two steps**:

### 1. Gathering the data

My source for obtaining the data is [NASA's Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/index.html) databse. In [this archive](https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html) there is an explanation on how to use the API to fetch the data from the [table](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS) I wanted. I've also based all my explanations on the [Table definitions](https://exoplanetarchive.ipac.caltech.edu/docs/API_PS_columns.html) to know what was each variable.

### 2. Exploratory Data Analysis

Once the data is gathered, I'm performing the EDA on the Google Colab Notebook in the following steps: 1) Data cleaning, 2) Data visualization, 3) Data Analysis and 4) Interpretation.


**Tools and Technologies**: NASA's Open API Exoplanet, Python 3, Google Colab, Pandas, Numpy, Matplotlib, Seaborn
