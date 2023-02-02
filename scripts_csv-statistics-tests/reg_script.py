class LinearRegression:

    def fit(self,X,Y):
        import numpy as np
        X=np.array(X).reshape(-1,1)
        Y=np.array(Y).reshape(-1,1)
        x_shape = X.shape
        self.parameter_cache = []
        num_var = x_shape[1]       #the shape corresponds to number of input variable dimensions. There’s only one for this dataset i.e weight of person
        self.weight_matrix = np.random.normal(-1,1,(num_var,1))
        self.intercept = np.random.rand(1)
        for i in range(50):
            self.dcostdm = np.sum(np.multiply(((np.matmul(X,self.weight_matrix)+self.intercept)-Y),X))*2/x_shape[0] #w.r.t to the weight
            self.dcostdc = np.sum(((np.matmul(X,self.weight_matrix)+self.intercept)-Y))*2/x_shape[0]          #partial derivative of cost w.r.t the intercept
            self.weight_matrix -= 0.1*self.dcostdm                                                                  #updating the weights with the calculated gradients
            self.intercept -= 0.1*self.dcostdc                                                                      #updating the weights with the calculated gradients
            self.parameter_cache.append(np.array((self.weight_matrix,self.intercept)))                             #the parameters are cached just to track the progress
            return self.weight_matrix,self.intercept,self.parameter_cache

    def predict(self,X):
        import numpy as np
        product = np.matmul(np.array(X).reshape(-1,1),self.weight_matrix)+self.intercept
        return product
