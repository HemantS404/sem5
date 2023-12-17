import numpy as np

l = np.array([[1,0,0,0,0],
    [1,0,0,0,0],
    [1,0,0,0,0],
    [1,1,1,1,1]]).reshape(1, 20)

m = np.array([
    [1,0,0,0,1],
    [1,1,0,1,1],
    [1,0,1,0,1],
    [1,0,0,0,1]]).reshape(1, 20)

class Perceptron:
    def __init__(self):
        self.W = np.array([np.zeros(20)])
    def fit(self, X, Y, epoch):
        for _ in range(epoch):
            for x, y in zip(X, Y):
                net = np.dot(x,self.W.T)
                y_hat = 0 if net<=0 else 1
                dW = 0.05*(y - y_hat)*x
                self.W += dW
        print(self.W)
    def predict(self, X):
        net = np.dot(X,self.W.T)
        return "L" if net<=0 else "M"
    
pr = Perceptron()
pr.fit([l,m],[0,1],5)
print("Prediction of L :",pr.predict(l))
print("Prediction of M :",pr.predict(m))