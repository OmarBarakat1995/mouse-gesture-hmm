import classifier
from classifier import *

from save_load import *
t0 = load_from_disk("dataset/0.txt")[0]
t1 = load_from_disk("dataset/1.txt")[0]
t2 = load_from_disk("dataset/2.txt")[0]
t3 = load_from_disk("dataset/3.txt")[0]
t4 = load_from_disk("dataset/4.txt")[0]
t5 = load_from_disk("dataset/5.txt")[0]
t6 = load_from_disk("dataset/6.txt")[0]
t7 = load_from_disk("dataset/7.txt")[0]
# t = [[327, 226], [350, 254], [368, 278], [369, 278], [371, 278], [371, 277], [371, 275], [372, 272], [373, 269], [376, 264], [383, 251], [391, 235], [398, 221], [403, 213], [408, 206], [410, 204], [412, 201], [412, 200], [413, 199], [414, 196], [415, 193], [417, 191], [418, 188], [420, 184], [422, 180], [425, 174], [428, 167], [431, 159], [433, 156], [435, 150], [437, 147], [438, 143], [438, 140], [439, 138], [439, 136], [440, 134], [440, 132], [441, 131], [441, 130], [441, 129], [442, 128]]

quantized_t0 = quantize_sample(t0, 8)
quantized_t1 = quantize_sample(t1, 8)
quantized_t2 = quantize_sample(t2, 8)
quantized_t3 = quantize_sample(t3, 8)
quantized_t4 = quantize_sample(t4, 8)
quantized_t5 = quantize_sample(t5, 8)
quantized_t6 = quantize_sample(t6, 8)
quantized_t7 = quantize_sample(t7, 8)
my_classifier = Classifier("dataset")

print("Finished __init__")
my_classifier.create_models_train([5]*my_classifier.n_classes, no_epochs=1)
print("Finished training")
print(my_classifier.predict(quantized_t0))
print(my_classifier.predict(quantized_t1))
print(my_classifier.predict(quantized_t2))
print(my_classifier.predict(quantized_t3))
print(my_classifier.predict(quantized_t4))
print(my_classifier.predict(quantized_t5))
print(my_classifier.predict(quantized_t6))
print(my_classifier.predict(quantized_t7))