from path import path
import pickle
from quantize import quantize_sample
from hmm import *


class Classifier:

    def __init__(self,p, q=8, pretrained=False):
        print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        self.q = q
        if pretrained == False:
            self.data = []
            for f in path(p).files(pattern='*.txt'):
                with open(f, "rb") as fp:
                    b = pickle.load(fp)
                    lenb = len(b)
                    print(lenb)
                    self.data.append(b)
            self.n_classes = len(self.data)
            print("no. of classes ->", self.n_classes)

    def create_models_train(self, no_of_hidden_states_list, no_epochs=10):
        self.hmm_models = []
        for i in range(self.n_classes):
            quantized = []
            for seq in range(len(self.data[i])):
                quantized.append(quantize_sample(self.data[i][seq], self.q))
            self.hmm_models.append(DiscreteHMM(self.q, no_of_hidden_states_list[i]))
            self.hmm_models[i].train(quantized, method="BW", no_epochs=no_epochs)

    def predict(self, observation_sequence):
        evaluations = []
        for i in range(self.n_classes):
            ev = self.hmm_models[i].evaluate(observation_sequence)
            evaluations.append(ev)
            #print(ev)
        maxIndex, maxValue = max(enumerate(evaluations), key=lambda v: v[1])
        return maxIndex, maxValue




