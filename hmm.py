from abc import ABC, abstractmethod
import numpy as np
import random
from quantize import quantize

class HMM(ABC):

    def __init__(self, no_of_hidden_states):
        """
            instantiates an HMM model , define number of states , and calls the parameters initialization methods

        """
        self.n = no_of_hidden_states
        self.emission_pb = []
        self.transition_pb = []
        print("Base_HMM")

    @abstractmethod
    def train(self):
        """
        learn the parameters =>emmission and transition
        """
        pass

    @abstractmethod
    def evaluate(self, *args):
        pass

    @abstractmethod
    def decode(self, observation_sequence):
        # return MLE hidden sequence
        pass


class GaussianHMM(HMM):
    def __init__(self, no_of_hidden_states ):
        super().__init__(no_of_hidden_states)
        print("Gaussian")

    def initialize_emission_pb(self):
        pass

    def initialize_transition_pb(self):
        pass

    def train(self, training_sequences, gt_classes ):
        """
        learn the parameters =>emmission and transition
        :param training_sequences: list of observations
        :param gt_classes: list of corresponding ground truth classes (same length as training_sequences[0])
        """

        pass

    def evaluate(self, observation_sequence):


        pass

    def decode(self, observation_sequence):
        # return MLE hidden sequence
        pass


class DiscreteHMM(HMM):
    def __init__(self,no_of_observed_values, no_of_hidden_states):
        super().__init__(no_of_hidden_states)
        self.v = no_of_observed_values
        self.initialize_emission_pb()
        self.initialize_transition_pb()
        self.pi = np.full(no_of_hidden_states, 1/no_of_hidden_states)
        print("Discrete")

    def initialize_emission_pb(self):
        e = np.random.random([self.n, self.v])
        self.emission_pb = e/np.sum(e, axis=1).reshape(e.shape[0],1)
        print("initialize emission_pb :")
        print(self.emission_pb)

    def initialize_transition_pb(self):
        e = np.random.random([self.n, self.n])
        self.transition_pb = e/np.sum(e,axis=1).reshape(e.shape[0],1)
        print("initialize transition_pb :")
        print(self.transition_pb)

    def train(self, training_sequences, method = "BW", no_epochs = 5):
        """
        learn the parameters =>emission and transition
        :param training_sequences: list of observations as lists

        """
        print("//////////////////////////////")
        e = 1
        while e <= no_epochs:
            for sequence in training_sequences:
                T = len(sequence)
                # alpha
                alpha = np.zeros((self.n, T))
                alpha[:, 0] = (1.0 / (self.pi+0.0000001)) * self.emission_pb[:, sequence[0]]
                for t in range(1, T):
                    f = alpha[:, t-1].reshape(self.n, 1)  #
                    alpha[:, t] = np.sum(f * self.transition_pb, axis=0) * self.emission_pb[:, sequence[t]]
                print("alpha",alpha)
                # beta
                beta = np.ones((self.n, T))
                beta[:, T-1] = 1.0
                for t in range(T-2, 0, -1):
                    b = beta[:, t+1].reshape(1, self.n)  # next time step column
                    # print(b.shape,self.transition_pb.shape, self.emission_pb[:, sequence[t+1]].reshape(1, -1).shape)
                    beta[:, t] = np.sum(b * self.transition_pb * self.emission_pb[:, sequence[t+1]].reshape(1, -1), axis=1)
                print("beta",b)
                ev = self.evaluate(sequence)
                print("ev", ev)
                gamma = alpha * beta / (ev+0.0000001) # (n,T) this is needed to keep track of finding a state i at a time t for all i and all t ->vectorized
                zi = np.zeros(shape=(self.n, self.n, T-1))
                for t in range(T-1):
                    for i in range(self.n):
                        for j in range(self.n):
                            zi[i, j, t] = alpha[i, t] * self.transition_pb[i, j] * beta[j, t+1] * self.emission_pb[j, sequence[t+1]] / (ev+0.0000001) # this is needed to keep track of finding a state i at a time t and j at a time (t+1) for all i and all j and all t

                self.pi = gamma[:, 0]

                self.transition_pb = np.sum(zi, axis=2) / (np.sum(gamma[:1], axis=1)+0.0000001)

                for i in range(self.v):
                    self.emission_pb[:,i] = np.sum(gamma * (sequence == i), axis=1) / (np.sum(gamma, axis=1)++0.0000001)



            e += 1

    def evaluate(self, observation_sequence):
        # set up
        """
        :param observation_sequence:python list of the observed sequence
        :return: probability of this obs_sequence
        """
        T = len(observation_sequence)
        # print("T = ", T)
        alpha = np.zeros((self.n, T))
        # forward part
        alpha[:, 0] = self.pi * self.emission_pb[:, observation_sequence[0]]
        # print("t = ", 0)
        # print("alpha[:, 0] : ", alpha[:, 0])
        # print("alpha[:, 0].reshape(self.n, 1)", alpha[:, 0].reshape(self.n, 1))
        for t in range(1, T):
            f = alpha[:, t-1].reshape(self.n, 1)    # last time step column
            alpha[:, t] = np.sum(f * self.transition_pb, axis=0) * self.emission_pb[:, observation_sequence[t]]
            # print("t = ", t)
            # print("alpha[:, t] : ", alpha[:, t])
            # print("alpha[:, t].reshape(self.n, 1)", alpha[:, t].reshape(self.n, 1))
        return np.sum(alpha[:, -1])

    def decode(self, observation_sequence, method="Posterior"):
        # return MLE hidden sequence
        # set up
        if method == "Posterior":
            states_sequence = []
            T = len(observation_sequence)
            fw = np.zeros((self.n, T))
            # forward part
            fw[:, 0] = (1.0 / self.n) * self.emission_pb[:, observation_sequence[0]]
            states_sequence.append(np.argmax(fw[:, 0]))
            for t in range(1, T):
                f = fw[:, t-1].reshape(self.n, 1)    # last time step column
                fw[:, t] = np.sum(f * self.transition_pb, axis=0) * self.emission_pb[:, observation_sequence[t]]
                states_sequence.append(np.argmax(fw[:, t]))

            return states_sequence


if __name__ == "__main__":
    G = DiscreteHMM(5, 3)
    seq = G.decode([0, 1, 2, 1])
    print("seq = ", seq)
    ev = G.evaluate(quantize([[327, 226], [350, 254], [368, 278], [369, 278], [371, 278], [371, 277], [371, 275], [372, 272], [373, 269], [376, 264], [383, 251], [391, 235], [398, 221], [403, 213], [408, 206], [410, 204], [412, 201], [412, 200], [413, 199], [414, 196], [415, 193], [417, 191], [418, 188], [420, 184], [422, 180], [425, 174], [428, 167], [431, 159], [433, 156], [435, 150], [437, 147], [438, 143], [438, 140], [439, 138], [439, 136], [440, 134], [440, 132], [441, 131], [441, 130], [441, 129], [442, 128]], 16))
    print("ev = ", ev)
    # D = GaussianHMM(8)

