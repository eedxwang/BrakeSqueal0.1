r"""
This module defines the following functions::

  - residual_qevp:
  
    Calculates the relative residual of the Quadratic Eigenvalue Problem (lamda^2 M + lamda C + K) X = 0
  
  - residual_gevp
  
    Calculates the relative residual of the Generalized Eigenvalue Problem (A - lamda B) X = 0

"""

import numpy
from scipy import sparse
from numpy import linalg

import scipy.sparse.linalg as norm

def residual_qevp(M,C,K,la,evec):
        r"""
        :param M: Mass Matrix
        :param C: Damping Matrix
        :param K: Stiffness Matrix
        :param la: eigenvalues
        :param evec: eigenvectors
        :return: res - residual
        """
        
        n = la.shape[0]
        res = numpy.zeros(n,numpy.complex_)   
        for i in range(0, n):
            vec = evec[:,i:i+1]
            A = la[i]*la[i]*M + la[i]*C + K
            res[i] = linalg.norm(A.dot(vec))
            #calculate relative residual
            if(sparse.issparse(A)):
                 A_norm=norm.onenormest(A, t=3, itmax=5, compute_v=False, compute_w=False)
            else:
                 A_norm=linalg.norm(A)
            
            res[i] = res[i]/(A_norm*linalg.norm(vec))
        return res;             

def residual_gevp(A,B,la,evec):
        r"""
        :param A: left matrix
        :param B: right matrix 
        :param la: eigenvalues
        :param evec: eigenvectors
        :return: res - residual
        """
        
        n = la.shape[0]
        res = numpy.zeros(n,numpy.complex_)   
        for i in range(0, n):
            vec = evec[:,i:i+1]
            AB = A - la[i]*B 
            res[i] = linalg.norm(AB.dot(vec))
            #calculate relative residual
            if(sparse.issparse(AB)):
                 AB_norm=norm.onenormest(AB, t=3, itmax=5, compute_v=False, compute_w=False)
            else:
                 AB_norm=linalg.norm(AB)
                 
            res[i] = res[i]/(AB_norm*linalg.norm(vec)) 
        return res;
