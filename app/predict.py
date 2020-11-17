import numpy as np
import pandas as pd
import joblib

# Get the model and pipeline created in notebook
model = joblib.load('models/TMDBmodel.joblib')
pipeline = joblib.load('models/TMDBpipeline.joblib')


def preprocess(data):
    
    # Dynamic defaults
    feature_values = {
        'belongs_to_collection': 0, # most common
        'budget': 8000000, # median
        'genres': 'Drama', # most common,
        'original_language': 'en', # most common
        'popularity': 7.3748615, # median
        'production_companies': 'Universal Pictures', # most common
        'production_countries': 'United States of America', # most common
        'release_year': 2004, # median
        'runtime': 104, # median
        'spoken_languages': 'English', # most common
        'Keywords': None, # most common
        'cast': None #most common
    }


    # Parse the form inputs and return the defaults updated with values entered.

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]

    return feature_values



####### 
## Now we can predict with the trained model:
#######


def predict(data):
 
    # Store the data in an array in the correct order:

    column_order = ['belongs_to_collection', 'budget', 'genres', 'original_language', 'popularity', 'production_companies',
       'production_countries', 'release_year', 'runtime', 'spoken_languages', 'Keywords', 'cast']

    data = np.array([data[feature] for feature in column_order], dtype=object)
    data = pd.DataFrame(data.reshape(1, -1), columns=column_order)
    
    data = pipeline.transform(data)
    pred = model.predict(data)

    return pred


def postprocess(prediction):

    pred = prediction

    # Validate. As an example, if the output is an int, check that it is positive.
    try: 
        int(pred[0]) > 0
    except:
        pass

    # Format to currency
    pred[0] = pred[0].astype(float)
    pred = "${:,.2f}".format(pred[0])
    
    # Make strings
    pred = str(pred)


    # Return
    return_dict = {'pred': pred}

    return return_dict