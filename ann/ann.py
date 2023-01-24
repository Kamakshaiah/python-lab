
import numpy as np

class NeuralNetwork(object):

    def __init__(self):
        np.random.seed(1)
        self.synaptic_wts = np.random.random((3, 1))

    def __sigmoid(self, x):
        return 1/(1 + np.exp(-x))

    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    def train(self, inputs, outputs, t_iterations):
        for i in range(t_iterations):
            output = self.learn(inputs)
            error = outputs - output
            factor = np.dot(inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_wts += factor

    def learn(self, inputs):
        return self.__sigmoid(np.dot(inputs, self.synaptic_wts))
            
if __name__ == '__main__':
    nn = NeuralNetwork()
    inputs = np.array([[0, 1, 1], [1, 0, 0], [1, 0, 1]])
    outputs = np.array([[1, 0, 1]]).T
    nn.train(inputs, outputs, 1000)
    print(nn.learn(np.array([1, 0, 1])))
