#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import math
import matplotlib.pylab as plt

def  find_rdf(r,L,pbc,Ng,rc):
	N=len(r)
	L_times_pbc=L*pbc
	L1=L[0]*L[1]*L[2]
	rho=N/L1
	dr=rc/Ng
	#accumulate
	g=np.zeros([Ng,1])
	for i in range(N-1):
		for j in range(i+1,N):
			r12= r[j,:]-r[i,:]
			r12=r12-np.round(r12/L)*L_times_pbc
			d12=math.sqrt(sum(r12*r12))
			if d12<rc:
				index=math.ceil(d12/dr)
				g[index-1]=g[index-1]+1
	for i in range(Ng):
		g[i]=g[i]/N*2
		dV=4*(math.pi)*((dr*(i+1))**2)*dr
		g[i]=g[i]/dV
		g[i]=g[i]/rho
	return g


if __name__ == '__main__':
	r=np.loadtxt('r.txt')	
	D=3
	n0=4
	N=256
	nxyz=np.array([4,4,4])
	a=np.array([4.57,4.57,4.57])
	pbc=np.array([1,1,1])
	L=5.60*nxyz
	Ng=100
	rc=np.min(L)/2
	dr=rc/Ng
	Ns=len(r)/N
	g=np.zeros([Ng,1])
	for i in range(int(Ns)):
		r1=r[(i*N+1):((i+1)*N),:]
		g=g+find_rdf(r1,L,pbc,Ng,rc)
	g=g/Ns 
	r=[(i+1)*dr/3.405 for i in range(Ng)]
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot(r, g,'o-')
	ax.set_xlim(0, 3.5)
	ax.set_ylim(0, 3.5)
	ax.set_title("Radical distribution function")
	ax.set_xlabel('r*')
	ax.set_ylabel('g(r)')
	plt.show()
