#Cálculo da TIR - Taxa interna de retorno

import numpy as np
import numpy_financial as npf #biblioteca necessaria pois foi removida da numpy

FC = np.zeros(7)
FC[0]=-155000
for i in range(6):
    FC[i+1] = 70000-15000

# Tit na biblioteca numpy
tir = npf.irr(FC)

print('++++++++++++++++++++++++++++')
print('')
print('TIR = ' + str(round(100*tir,2)) + '%')

#tir é qiando a VPL cruza o valor zero no eixo das abssas. Vamos graficar para exemplificar

import matplotlib.pyplot as fig

eixox = np.linspace(0,0.35,200)
vpl = np.array([npf.npv(i, FC) for i in eixox])
fig.plot(eixox, vpl, '--k', linewidth=2)
fig.plot(tir, 0,'k*', markersize=15)
fig.xlabel('juros-i')
fig.title('TIR = Taxa Interna de Retorno', fontsize=16)
fig.grid()
fig.show()