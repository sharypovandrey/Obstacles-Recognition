from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import numpy as np


class Encoder:
  
    label_encoder = LabelEncoder()
    onehot_encoder = OneHotEncoder(sparse=False)
    classes = ['10', '30', '50', 'more_than_50']

    def __init__(self):
        self.label_encoder.fit_transform(self.classes)

    def decode_value(self, value):
        inverted = self.label_encoder.inverse_transform([np.argmax(value)])
        return inverted[0]

    def decode_values(self, values):
        inverted = self.label_encoder.inverse_transform([np.argmax(v) for v in values])
        return inverted
