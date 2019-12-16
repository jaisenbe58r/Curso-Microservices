import sklearn
import pickle

print(sklearn.__version__)

filename = "../010_model/iris_model.pkl"
loaded_model = pickle.load(open(filename, 'rb'))