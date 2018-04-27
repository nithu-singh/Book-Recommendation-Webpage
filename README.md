# Book Recommendation Webpage

The dataset for this was obtained from Kaggle website, the dataset contains ten thousand books, one million user ratings and other necessary data.

* [Kaggle](https://www.kaggle.com/philippsp/book-recommender-collaborative-filtering-shiny/data) - Link to the dataset

Used this data to perform analysis using the technology Spark and Python web-framework Flask on local machine.
The results can be viewed on the website that can be deployed locally.

## For Testing Puropse

These instructions will get you a copy of the project up and running on your local machine for testing purpose.

### Prerequisites

Pre-requisites to run flask app are python and other libraries as mentioned in the myapp.py file in the Webpage folder.

### Deployment

To deploy the flask app locally the following steps are to be performed,

1. Download the Webpage folder onto your local machine.
2. Use command prompt with python installed or use Anaconda prompt instead and cd to the Webpage folder.
3. Run the following commands,

```
python -m flask

set FLASK_DEBUG=1

set FLASK_APP=%path%myapp.py

flask run
```
Note: The commands above are with respect to windows machine.