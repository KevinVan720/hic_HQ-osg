#!/usr/bin/env python3
import xml.etree.cElementTree as ET
import numpy as np
import matplotlib.pyplot as plt
import h5py, sys

lattice1_x = [1.46, 2.20, 2.93]
lattice1_y = [1.8, 2.0, 2.3]
lattice1_stat = [0.7, 0.4, 0.4]
lattice1_sys = [(1.3, -0.5), (0.6, -1.2), (0.2, -1.1)]
lattice2_x = [1.04102920332607,
1.09086415407343,
1.2418949863598,
1.49949352441474,
1.93950565736037,
]
lattice2_y = [4.80608444754841,
6.22087578147966,
4.04148418878713,
4.45467839268429,
9.77960354476739,
]
lattice2_stat = [0.827511828685804,
0.8275118286858,
1.26110735597276,
0.157638419496596,
4.01977969716318,
]
lattice2_sys = [(-1.61552417882614,	3.27117695189699),
(-2.20684799928101,	3.94131998210016),
(-1.41865590179804,	4.25650694742203),
(-1.45806550667218,	2.71917286264494),
(-5.911350857451,	6.6604928447451),
]

def plot(specie, ax):
	M = 1.3 if specie == 'charm' else 4.2 if specie =='bottom' else 10.0
	Tc = 0.154
	e = np.linspace(M+0.01, 50, 30)
	t = np.linspace(0.15, 1.0, 20)
	E, T = np.meshgrid(e, t)
	E = E.T
	T = T.T
	w = (t[2]-t[0])/Tc/1.5
	
	for k, Eid in enumerate([0]):	
		for nPDF, color, shift in zip(['EPS09', 'nCTEQ'], ['g', 'b'], [-1, 1]):
			parameters = np.loadtxt(nPDF+'-sample-parameter.txt').T
			mu, A, B = parameters
			fo = h5py.File('kappa_{}_pQCD'.format(specie), 'r')
			res = []
			res0 = []
			print('E = ', e[Eid])
			for i, (m, a, b) in enumerate(zip(mu, A, B)):
				qhat_pQCD = fo['{}/{}/Qq2Qq/qxx'.format(nPDF, i)].value\
							+fo['{}/{}/Qg2Qg/qxx'.format(nPDF, i)].value
				qhat = qhat_pQCD + a + b/E/T
				res.append(4*np.pi/qhat[Eid, :] )
				res0.append(4*np.pi/qhat_pQCD[Eid, :] )
			res = np.array(res).T
			res0 = np.array(res0).T

			violin = ax.violinplot(list(res)[:10:2], (t/Tc+shift*w/4.)[:10:2], widths=w/2., showextrema=False, showmedians=True)
			for b in violin['bodies']:
				b.set_color(color)
			for partname in ['cmedians']:
				vp = violin[partname]
				vp.set_edgecolor(color)
				vp.set_linewidth(1)
			# for pQCD
			m = np.median(res0, axis=1)
			m95 = np.percentile(res0, 95, axis=1)
			m5 = np.percentile(res0, 5, axis=1)
			#ax.plot(t/Tc, m, '--', color=color, alpha=0.8, label=nPDF+', pQCD median' if k==3 else '')
			#ax.plot(t/Tc, m5, '-', color=color, alpha=0.6)
			#ax.plot(t/Tc, m95, '-', color=color, alpha=0.6)

			if k==3:
				ax.fill_between([],[],[],color=color, alpha=0.3, label=nPDF+', both')
				ax.legend(framealpha=0., fontsize=10)


		ax.set_title(r'$E = {:1.1f}$ [GeV]'.format(e[Eid]), fontsize=10)
		if k==0:
			ax.errorbar(lattice1_x, lattice1_y,  yerr=lattice1_stat, fmt='rD', label='LQCD, charm')
			for x, y, ysys in zip(lattice1_x, lattice1_y, lattice1_sys):
				h, l = ysys
				ax.fill_between([x-.02, x+.02], [y+l, y+l], [y+h, y+h],color='r', alpha=0.3)

			ax.errorbar(lattice2_x, lattice2_y,  yerr=lattice2_stat, fmt='kD', label='LQCD, static')
			for x, y, ysys in zip(lattice2_x, lattice2_y, lattice2_sys):
				l, h = ysys
				ax.fill_between([x-.02, x+.02], [y+l, y+l], [y+h, y+h],color='k', alpha=0.3)
			ax.legend(framealpha=0., fontsize=15, loc='upper left')
		if ax.is_last_row():
			ax.set_xlabel(r'$T/T_c$', fontsize=15)
		else:
			ax.set_xticks([])

		if ax.is_first_col():
			ax.set_ylabel(r'$2\pi T D$', fontsize=15)
		else:
			ax.set_yticks([])
		ax.set_ylim(0., 17)
		ax.set_xlim(0.6, 3.)
		ax.set_title("M = {:1.1f} GeV".format(M), fontsize=15)

figure, axes = plt.subplots(1,3, figsize=(12,4))
plot('charm', axes[0])
plot('bottom', axes[1])
plot('heavy', axes[2])
plt.tight_layout(True)
plt.subplots_adjust(hspace=0.15, wspace=0., top=0.9)

plt.show()
