import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def predict_price(location, total_sqft, bath, no_of_bedrooms):
    try:
        location_index = __data_columns.index(location.lower())
    except:
        location_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = no_of_bedrooms
    if location_index >= 1:
        x[location_index] = 1
    return round(__model.predict([x])[0], 2)

def get_location_names():
    return __locations
def load_saved_data():
    print("Loading saved data ...")
    global __data_columns
    global __locations
    global  __model

    with open("./model/columns.json", "r") as f:
        __data_columns = json.load(f)["data_columns"]
        __locations = __data_columns[3:]

    with open("./model/home_prices_prediction_model.pickle", "rb") as f:
        __model = pickle.load(f)
    print("Data loading is done")
load_saved_data()
if __name__ == "__main__":
    print(f"GHC{predict_price('1st Phase JP Nagar', 1000.0 , 2.0, 	2.0)}")
    print(get_location_names())