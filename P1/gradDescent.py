import loadParametersP1 as lp
import loadFittingDataP1 as lfd
import numpy as np
import matplotlib.pyplot as plt

#Implementing basic gradient descent
def gradDescent(n, dg, step_size, threshold, num_iterations, theta = None):
    if theta is None:
        theta = np.zeros(n)
    thetas = []
    for i in range(num_iterations):
        theta_sum = (theta).sum()
        thetas.append(theta_sum)
        new_theta = theta - step_size * dg(theta)
        if np.linalg.norm(new_theta - theta) < threshold:
            return theta, thetas
        theta = new_theta
    return theta, thetas

def d_quadraticBowl(x):
    return (np.matmul(x, A)-b)

def quadraticBowl(x):
    return .5 * (x * np.matmul(A, x.T)) - x.T * b

def d_gaussian(x):
    n = len(mu)
    return -1 * np.matmul(np.matmul(gaussian(x, mu, S, n), np.linalg.inv(S)), (x-mu))

def gaussian(x, mu, S, n):
    coeff = -(1)/np.sqrt((2*np.pi)**n * np.linalg.norm(S))
    print((x-mu).T.shape)
    print(np.linalg.inv(S).shape)
    exponent = -0.5 * (x-mu).T * np.linalg.inv(S) * (x-mu)
    return coeff * np.exp(exponent)

def l_gaussian(mu, S, n):
    return lambda x: gaussian(x, mu, S, n)

def gradientApprox(f, x, d):
    return (f(x+d)-f(x))/d


# mu, S, A, b = lp.getData()
# n = len(mu)

# part 1
# print(mu)
# print(S)
# print(A)
# print(b)
# n = len(mu)
# _, sums_a_0 = gradDescent(n, d_gaussian, 20, 0, 40)
# _, sums_b_0 = gradDescent(n, d_quadraticBowl, 0.01, 0, 40)
<<<<<<< HEAD

# _, sums_a_1 = gradDescent(n, d_gaussian, 100, 0, 40)
# _, sums_b_1 = gradDescent(n, d_quadraticBowl, 0.05, 0, 40)

# _, sums_a_2 = gradDescent(n, d_gaussian, 300, 0, 40)
# _, sums_b_2 = gradDescent(n, d_quadraticBowl, 0.12, 0, 40)

=======
#
# _, sums_a_1 = gradDescent(n, d_gaussian, 100, 0, 40)
# _, sums_b_1 = gradDescent(n, d_quadraticBowl, 0.05, 0, 40)
#
# _, sums_a_2 = gradDescent(n, d_gaussian, 300, 0, 40)
# _, sums_b_2 = gradDescent(n, d_quadraticBowl, 0.12, 0, 40)
#
>>>>>>> e21d6ef5d25b239eff849a29218be4e3f0de6c5d
# plt.plot(sums_a_0, label="gaussian_lr=20")
# plt.plot(sums_b_0, label="quadratic Bowl_lr=0.01")
# plt.plot(sums_a_1, label="gaussian_lr=100")
# plt.plot(sums_b_1, label="quadratic Bowl_lr=0.05")
# plt.plot(sums_a_2, label="gaussian_lr=300")
# plt.plot(sums_b_2, label="quadratic Bowl_lr=0.1")
<<<<<<< HEAD


=======
#
#
>>>>>>> e21d6ef5d25b239eff849a29218be4e3f0de6c5d
# plt.ylabel("Theta Value")
# plt.xlabel("Iteration number")
# plt.title("Theta Convergence")
# plt.legend()
# plt.show("hold")

## part 2
<<<<<<< HEAD
d = 0.000000000001
g_differences = []
q_differences = []
print (mu.shape)
for x in np.random.random([100, n]):
    x * 100
    g_differences.append(np.linalg.norm(gradientApprox(l_gaussian(mu, S, n), x, d) - d_gaussian(x)))
    q_differences.append(np.linalg.norm(gradientApprox(quadraticBowl, x, d) - d_quadraticBowl(x)))
plt.hist(g_differences)
plt.title("g_diff")
plt.show('hold')
plt.hist(q_differences)
plt.title("q_diff")
plt.show('hold')
=======
# g_differences = []
# q_differences = []
# x = np.ones(n)*0.5
# for d in range(10):
#     d = 10**(-d)
#     g_differences.append(np.linalg.norm(gradientApprox(l_gaussian(mu, S, n), x, d) - d_gaussian(x)))
#     q_differences.append(np.linalg.norm(gradientApprox(quadraticBowl, x, d) - d_quadraticBowl(x)))
# print(g_differences)
# plt.plot(g_differences, label = "Gaussian")
# plt.plot(q_differences, label = "Quadratic Bowl")
# plt.legend()
# plt.title("g_diff")
# plt.show('hold')
>>>>>>> e21d6ef5d25b239eff849a29218be4e3f0de6c5d


## part 3 a batch
#Implementing basic gradient descent
def batchGradDescent(y, x, step_size, num_iterations, theta = None):
    if theta is None:
        theta = np.zeros([len(x[0])])
    evaluations = []
    thetas = []
    errors = []
    for i in range(num_iterations):
        evaluations.append(i*len(y))
        thetas.append(theta.sum())
        error = np.matmul(x, theta) - y
        errors.append(abs(error).sum())
        a = np.matmul(error.T, x)
        theta -= step_size * a

    return theta, (evaluations, thetas), errors


## part 3 b stochastic
#Implementing stochastic gradient descent
def stochGradDescent(y, x, t_o, k, num_iterations, theta=None):
    if theta is None:
        theta = np.zeros(len(x[0]))
    thetas = []
    evals = 0
    evaluations = []
    errors = []
    for i in range(num_iterations):
        error = np.matmul(x, theta) - y
        errors.append(abs(error).sum())
        p = np.random.permutation(len(y))
        y = y[p]
        x = x[p]
        step_size = (t_o+i)**(-k)
        for point in range(len(x)):
            thetas.append(theta.sum())
            evaluations.append(evals)
            evals += 1
            gradient = (np.matmul(x[point], theta) - y[point]) * x[point]
            theta -= step_size * gradient

    # plt.plot(errors)
    # plt.show("hold")
    return theta, (evaluations, thetas), errors

x, y = lfd.getData()
y/1000.0
x/1000.0
#
_, t_batch_1, e_batch_1 = batchGradDescent(y, x, 0.00001, 20)
_, t_stoch_1, e_stoch_1 = stochGradDescent(y, x, 100000, 1, 20)

# convergence plot

# plt.plot(e_batch_1, label="Batch gradient decent")
# plt.plot(e_stoch_1, label="Stochastic gradient decent")
# plt.title("Batch vs Stochastic gradient decent")
# plt.xlabel("Number of Iterations")
# plt.ylabel("error over dataset")
# plt.legend()
# plt.show("hold")


#
# # theta plots
# plt.plot(t_batch_1[0], t_batch_1[1], label="Batch gradient decent")
# plt.plot(t_stoch_1[0], t_stoch_1[1], label="Stochastic gradient decent 1")
# plt.plot(t_stoch_2[0], t_stoch_2[1], label="Stochastic gradient decent 2")
# plt.plot(t_stoch_3[0], t_stoch_3[1], label="Stochastic gradient decent 3")
# plt.title("Batch vs Stochastic gradient decent")
# plt.xlabel("Number of Evaluations")
# plt.ylabel("Sum of Theta vector")
# plt.legend()
# plt.show("hold")


## eval
# y = np.matrix(y)
# x = np.matrix(x)
# A2 = np.linalg.inv(x.T*x)*x.T*y.T
# print(A2.sum())
# print(A, A2)
# print(A * x.T)
