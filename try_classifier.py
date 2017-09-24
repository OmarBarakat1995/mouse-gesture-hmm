import classifier
from classifier import *

from save_load import *
t0 = load_from_disk("dataset/0.txt")[0]
# t = [[327, 226], [350, 254], [368, 278], [369, 278], [371, 278], [371, 277], [371, 275], [372, 272], [373, 269], [376, 264], [383, 251], [391, 235], [398, 221], [403, 213], [408, 206], [410, 204], [412, 201], [412, 200], [413, 199], [414, 196], [415, 193], [417, 191], [418, 188], [420, 184], [422, 180], [425, 174], [428, 167], [431, 159], [433, 156], [435, 150], [437, 147], [438, 143], [438, 140], [439, 138], [439, 136], [440, 134], [440, 132], [441, 131], [441, 130], [441, 129], [442, 128]]

quantized_t = quantize(t0, 8)
my_classifier = Classifier("dataset")
print("Finished __init__")
my_classifier.create_models_train([5]*my_classifier.n_classes, no_epochs=1)
print("Finished training")
print(my_classifier.predict(quantized_t))