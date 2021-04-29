import matplotlib.pyplot as plt 
import numpy as np

combination=[]
res = [100000, 68000, 39000, 27000, 18000, 10000, 6800, 3900]
div = []
x=[]
for r in res:
    for e in res:
        if r/e not in div and r/e < 1:
            x.append(r/e)
            combination.append((r/e, r, e))
X=sorted(x)
Com = sorted(combination, key = lambda combination: combination[0])  



Y_plus = np.array(X)+3.54
Y_minus = 3.54-np.array(X)

# 3.54*0.05 = 3.717 d=0.177
# 3.54 *0.95 = 3.363 d=0.177

for y in Com:
    if 0.174<y[0]<0.18:
        right_com = y



plt.xticks(np.linspace(0, 1, 25), fontsize=17)
plt.yticks(fontsize=17)
plt.plot(X, Y_plus, '-r', linewidth=3, label='Vth_plus')
plt.plot(X, Y_minus, '-b', linewidth=3, label='Vth_minus')
plt.scatter(X, Y_plus, c='r')
plt.scatter(X, Y_minus, c='b')
plt.xlabel('R_a/R_b', fontsize=30)
plt.ylabel('Voltage', fontsize=30)
plt.plot((X[0], X[-1]), (3.54, 3.54), '-k', linewidth=3, label='Vth')
plt.plot((X[0], X[-1]), (3.54*1.05, 3.54*1.05), '-g', linewidth=3, label='|5%|')
plt.plot((X[0], X[-1]), (3.54*0.95, 0.95*3.54), '-g', linewidth=3)
plt.vlines(right_com[0], 3.54+0.25, 3.54-0.25, 'k', linestyles='--',
           label=f'{right_com[1]}Ω/{right_com[2]}Ω')


plt.grid(b=True, which='both', color='#999999', linestyle='-')

    
    
plt.legend(loc='upper left', fontsize=20)
plt.show()

