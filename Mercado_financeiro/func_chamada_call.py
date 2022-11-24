import numpy as np
import math
from scipy import stats
import matplotlib.pyplot as fig

def call (S,K,T,r, sigma):
    d1 = (math.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1-sigma*np.sqrt(T)
    c_t = S*stats.norm.cdf(d1)-K*math.exp(-r*T)*stats.norm.cdf(d2)
    return c_t

def call2 (S,K,T,r, sigma):
    d1 = (math.log(S / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    #Grafico da área d1 e d2
    Ix1=np.linspace(-1,d1,100)
    Ix2 = np.linspace(-1, d2, 100)
    Iy1 = stats.norm.pdf(Ix1,0,sigma)
    Iy2 = stats.norm.pdf(Ix2, 0, sigma)
    eixox=np.linspace(-1,1,100)
    eixoy=stats.norm.pdf(eixox,0,sigma)
    fig.figure()
    ax1 = fig.subplot(121)
    ax1.plot(eixox, eixoy,'-k')
    ax1.fill_between(Ix1, Iy1, color='k')
    ax1.text(d1-0.3,1,'N(d1', fontsize=14, weight='bold')
    ax2=fig.subplot(122)
    ax2.plot(eixox, eixoy,'-k')
    ax2.fill_between(Ix2, Iy2, color='k')
    ax2.text(d2-0.3,0.5,'N(d2', fontsize=14, weight='bold')


    #Calculo do valor da call
    c_t = S * stats.norm.cdf(d1) - K * math.exp(-r * T) * stats.norm.cdf(d2)
    print(d1,d2)
    fig.show()
    return c_t

    #Functio para call volatilidade implicita

def call3(S,K,T,r,sigma):
    d1=(math.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2= d1-sigma*np.sqrt(T)
    c_t = S*stats.norm.cdf(d1)-K*math.exp(-r*T)*stats.norm.cdf(d2)
    return c_t,d1