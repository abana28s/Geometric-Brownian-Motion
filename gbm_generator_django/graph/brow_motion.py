# Brow Motion: X(ti+1) = X(ti) + µ*(ti+1−ti) + σ*((ti+1 − ti)^0.5)*Zi+1
# Geo Brow Motion: S(ti+1) = S(ti)*exp([µ - (sigma^2)/2](ti+1 - ti) + sigma((ti+1 - ti)^0.5)*Zi+1)

import matplotlib.pyplot as plt 
import numpy as np
import io
import base64

class BrownianMotion:
    def __init__(self, mu, sigma, T, n, flag, no_paths, S_0):
        self.mu = mu
        self.sigma = sigma
        self.T = T
        self.n = n
        self.t = T/n
        self.flag = flag
        self.no_paths = no_paths
        self.S_0 = S_0

    def cal(self, x):
        z = np.random.normal(0, 1, 1)
        val = x + self.mu*self.t + self.sigma*pow(self.t, 0.5)*z[0]

        return val

    def cal_geo(self, x):
        z = np.random.normal(0, 1, 1)
        val = x*np.exp((self.mu - (pow(self.sigma,2) / 2))*self.t + self.sigma*pow(self.t, 0.5)*z[0])

        return val

    def generate_seq(self):
        ts = []
        ts.append(0)
        S = []
        S.append(self.S_0)

        for i in range(1, self.n + 1):
            ts.append(self.t*i)

            s = 0
            if (self.flag == 1):
                s = self.cal(S[i - 1])
        
            if (self.flag == 2):
                s = self.cal_geo(S[i - 1])

            S.append(s)

        return ts, S 

    def theor_mean_brow(self):
        return self.mu*self.T

    def theor_variance_brow(self):
        return pow(self.sigma, 2)*self.T

    def theor_mean_geo(self):
        theoMean = self.S_0*np.exp(self.mu*self.T)
        return theoMean 

    def theor_variance_geo(self):
        theoVar = pow(self.S_0, 2)*np.exp(2*self.mu*self.T)*(np.exp(pow(self.sigma, 2)*self.T) - 1)
        return theoVar

    def generate_brownian(self):
        self.S_0 = 0
        
        theoMean = self.theor_mean_brow()
        theoVar = self.theor_variance_brow()
        ST = 0
        Var = 0
        for i in range(0, self.no_paths):
            ts, S = self.generate_seq()
            plt.plot(ts, S)

            ST = ST + S[self.n]
            Var = Var + pow((S[self.n] - theoMean), 2)
            

        # print("Calculated value of E(S[",T,"]) is", ST / 100, "\nTheoretical value of E(S[",T,"]) is", theoMean, "\n\n")
        # print("Calculated value of Var(S[",T,"]) is", Var / 100, "\nTheoretical value of Var(S[",T,"]) is", theoVar)    

        return {
            "image": self.getBase64(plt),
            "calculated_variance": Var/self.no_paths,
            "theoretical_variance": theoVar,
            "calculated_mean" : ST/self.no_paths,
            "theoretical_mean": theoMean
        }

    def generate_geo_brownian(self):

        theoMean = self.theor_mean_geo()
        theoVar = self.theor_variance_geo()
        ST = 0
        Var = 0
        for i in range(0, self.no_paths):
            ts, S = self.generate_seq()
            plt.plot(ts, S)

            ST = ST + S[self.n]
            Var = Var + pow((S[self.n] - theoMean), 2)
        
        # print("Calculated value of E(S[",T,"]) is", ST / 100, "\nTheoretical value of E(S[",T,"]) is", theoMean, "\n\n")
        # print("Calculated value of Var(S[",T,"]) is", Var / 100, "\nTheoretical value of Var(S[",T,"]) is", theoVar)

        return {
            "image": self.getBase64(plt),
            "calculated_variance": Var/self.no_paths,
            "theoretical_variance": theoVar,
            "calculated_mean" : ST/self.no_paths,
            "theoretical_mean": theoMean
        }

    def getBase64(self, plt):
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png', bbox_inches="tight")
        plt.close()
        return base64.b64encode(buffer.getvalue()).decode("utf-8").replace("\n", "")

if __name__ == "main":
    mu = 0.06
    sigma = 0.5
    S_0 = 5
    T = 5
    n = 10000

    #flag = 1 -> brownian motion, flag = 2 -> geometric brownian motion => user input 

    # mu, sigma, T, n, type, # of paths, s[0]

    brow_motion = BrownianMotion(mu, sigma, T, n, 1, 10, 0)
    brow_motion.generate_brownian()

    brow_motion = BrownianMotion(mu, sigma, T, n, 2, 10, S_0)
    brow_motion.generate_geo_brownian()