import math
import random

random.seed(0)


def sigmoid(x):
    """
    computes the sigmoid function 1/(1+e^(-x))
    """
    return 1.0 / (1.0 + math.exp(-x))


def d_sigmoid(y):
    """
    derivatve of the sigmoid function
    :return:
    """
    return y * (1 - y)


def matrix(a, b, element=0.0):
    """
    generate a matrix
    """
    mat = []
    for i in range(a):
        mat.append([element] * b)
    return mat


def shuffle_matrix(mat, a, b):
    """
   shuffle the elements of the matrix
    """
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = random.uniform(a, b)

# class definition for the neural network
class NeuralNetwork:
    def __init__(self, n_i, n_h, n_o):
        # initialize the number of input, hidden, and output nodes
        """
        n_i - no of input nodes
        n_h - no of hidden layer nodes
        n_o - no of output nodes
        """
        self.n_i = n_i + 1
        self.n_h = n_h
        self.n_o = n_o

        #
        self.a_i = [1.0] * self.n_i
        self.a_h = [1.0] * self.n_h
        self.a_o = [1.0] * self.n_o

        # weight matrix
        self.w_i = matrix(self.n_i, self.n_h)  # W1
        self.w_o = matrix(self.n_h, self.n_o)  # Theta2

        shuffle_matrix(self.w_i, -1, 1)
        shuffle_matrix(self.w_o, -1, 1)
        print("\nInitial weights:")
        print("W1: ")
        for i in range(self.n_i):
            print(self.w_i[i])
        print("W2: ")
        for j in range(self.n_h):
            print(self.w_o[j])

        self.c_i = matrix(self.n_i, self.n_h)
        self.c_o = matrix(self.n_h, self.n_o)

    def forward_propagation(self, inputs):
        """
        function to perform forward propagation
        """
        if len(inputs) != self.n_i - 1:
            print('incorrect number of inputs')

        for i in range(self.n_i - 1):
            self.a_i[i] = inputs[i]

        for j in range(self.n_h):
            sum = 0.0
            for i in range(self.n_i):
                sum += (self.a_i[i] * self.w_i[i][j])
            self.a_h[j] = sigmoid(sum)

        for k in range(self.n_o):
            sum = 0.0
            for j in range(self.n_h):
                sum += (self.a_h[j] * self.w_o[j][k])
            self.a_o[k] = sigmoid(sum)

        return self.a_o

    def back_propagation(self, t, N, M):
        """
        function to perform backpropagation
        """

        # calculate the delta for output layer
        out = [0.0] * self.n_o
        for k in range(self.n_o):
            error = t[k] - self.a_o[k]
            out[k] = error * d_sigmoid(self.a_o[k])

        # update weight W2
        for j in range(self.n_h):
            for k in range(self.n_o):
                c = out[k] * self.a_h[j]
                self.w_o[j][k] += N * c + M * self.c_o[j][k]
                self.c_o[j][k] = c

        # calculate the delta for the hidden layer
        hid = [0.0] * self.n_h
        for j in range(self.n_h):
            error = 0.0
            for k in range(self.n_o):
                error += out[k] * self.w_o[j][k]
            hid[j] = error * d_sigmoid(self.a_h[j])

        # update W1
        for i in range(self.n_i):
            for j in range(self.n_h):
                c = hid[j] * self.a_i[i]
                self.w_i[i][j] += N * c + M * self.c_i[i][j]
                self.c_i[i][j] = c

        error = 0.0
        for k in range(len(t)):
            error = 0.5 * (t[k] - self.a_o[k]) ** 2
        return error

    def print_weights(self):
        """
        print(the weights
        """
        print("\nFinal weights: ")
        print('W1: ')
        for i in range(self.n_i):
            print(self.w_i[i])
        print('W2: ')
        for j in range(self.n_h):
            print(self.w_o[j])

    def test(self, patterns):
        """
        testing the model
        """
        print("\n")
        for p in patterns:
            inputs = p[0]
            # print('Inputs:', p[0], '-->', self.forward_propagation(inputs), '\tTarget', p[1]
            print('Inputs:', p[0], '-->', self.forward_propagation(inputs), 'Target'.rjust(10), p[1])

    def train(self, patterns, max_iterations=1000, N=0.5, M=0.5):
        """
        training the model
        """

        N = learning_rate
        M = N / 2
        error = 0.0
        for i in range(max_iterations):
            for p in patterns:
                inp = p[0]
                t = p[1]
                self.forward_propagation(inp)
                error = self.back_propagation(t, N, M)

            if i == 0:
                print("\nFirst-batch error: ", error)

            if error < expected_error:
                print("\nFinal error: ", error)
                print("\nTotal number of batches trained: ", i + 1)
                break
        # self.test(patterns)


def main():
    X = [
        [[0, 0], [0]],
        [[0, 1], [1]],
        [[1, 0], [1]],
        [[1, 1], [0]]
    ]
    global expected_error
    global learning_rate
    expected_error = float(input('Enter the expected error: '))
    learning_rate = float(input('Enter the learning rate: '))
    NN = NeuralNetwork(2, 2, 1)
    NN.train(X)
    NN.print_weights()


if __name__ == "__main__":
    main()
