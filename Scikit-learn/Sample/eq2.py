from random import randint
from sklearn.linear_model import LinearRegression


TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100


TRAIN_INPUT = list()
TRAIN_OUTPUT= list()


for i in range(TRAIN_SET_COUNT):
 a = randint(0, TRAIN_SET_LIMIT)
 b = randint(0, TRAIN_SET_LIMIT)
 c = randint(0, TRAIN_SET_LIMIT)
 d = randint(0, TRAIN_SET_LIMIT)

 
 op = (7*a)+(3*b)+(4*c)+(9*d)
 TRAIN_INPUT.append([a,b,c,d])
 TRAIN_OUTPUT.append(op)
predictor = LinearRegression(n_jobs=-1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)
X_TEST = [[7,3,4,9]]
outcome = predictor.predict(X=X_TEST)
coefficients = predictor.coef_ 
print('Outcome: {}\n Coefficients: {}'.format(outcome, coefficients))
