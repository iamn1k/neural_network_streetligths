class StreetlightsNeuroWeb:
    def __init__(self,input,answer):
        self.input = input
        self.answer = answer
    def __relu(self,x):
        return (x > 0) * x 
    def __relu2deriv(self,output):
        return output>0  
    def fit(self,count_iterations,div_print=9,alpha=0.2,hidden_size=8):
        import numpy as np

        np.random.seed(5)
        global weights_0_1
        global weights_1_2
        # random weights init
        weights_0_1 = 2*np.random.random((3,hidden_size)) - 1
        weights_1_2 = 2*np.random.random((hidden_size,1)) - 1
        # fit this model
        for iteration in range(count_iterations):
            layer_2_error = 0
            for i in range(len(self.input)):
                # the first layer is assigned a string from input
                layer_0 = self.input[i:i+1]
                # scalar multiplication of the first layer and the weights 
                # between layer 1 and 2, as well as "off"
                # negative weights using the __relu () function
                layer_1 = self.__relu(np.dot(layer_0,weights_0_1))

                # scalar multiplication between the second layer 
                # and weights between the 2 and 3 layers
                layer_2 = np.dot(layer_1,weights_1_2)
                # calculation of the squared mean error method
                layer_2_error += np.sum((layer_2 - self.answer[i:i+1]) ** 2)
                # calculating the "clean" error: 
                # the difference between the forecast and the correct answer
                layer_2_delta = (layer_2 - self.answer[i:i+1])
                #similar calculation of the mean error of the first layer
                layer_1_delta = layer_2_delta.dot(weights_1_2.T)*self.__relu2deriv(layer_1)
                # changing weights by multiplying the alpha coefficient by 
                #the dot product neighboring "clean" errors
                weights_1_2 -= alpha * layer_1.T.dot(layer_2_delta)
                weights_0_1 -= alpha * layer_0.T.dot(layer_1_delta)

            if(iteration % 10 == div_print):
                print("Error:" + str(layer_2_error),end=' ')
                print("Iteration:"+ str(iteration),end='\n')
    def predict_light(self,input):
        import numpy as np
        import math
        layer_0 = np.array(input)
        layer_1 = np.dot(layer_0,weights_0_1)
        layer_2 = np.dot(layer_1,weights_1_2)
        return True if 1 / (1 + math.exp(-layer_2)) > 0.59 else False
        
