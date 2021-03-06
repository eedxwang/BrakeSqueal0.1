# This file reads the component matrices and displays there sparsity pattern
# no of non-zeros, 1-norm and matrix rank.

#----------------------------------Standard Library Imports---------------------------------------
import timeit
import numpy
import os
import logging
import matplotlib.pylab as plt
from scipy.sparse.linalg import onenormest, aslinearoperator
from scipy.linalg.interpolative import estimate_rank
#----------------------------Application Specific Imports-----------------------------------------
import brake
import createBrakeClassObject
from brake.initialize import load


begin_program = timeit.default_timer()


#----------------------------Create Object--------------------------------------------------------
obj = createBrakeClassObject.returnObject(20)

if not os.path.exists(obj.output_path+'dataAnalysis'): os.makedirs(obj.output_path+'dataAnalysis')

hdlr_i = logging.FileHandler(obj.output_path+'dataAnalysis/dataAnalysisReport.log',mode='w')    
obj.logger_i.addHandler(hdlr_i)

obj.logger_i.info("\n"+"\n"+'Beginning Data Analysis')
obj.logger_i.info('------------------------------------------------------------------------')

print "\n"+"\n"+'Beginning Data Analysis'

sparse_list = load.load_matrices(obj)

obj.logger_i.info("\n"+'Matrices in CSC format converted to CSR')

obj.logger_i.info("\n\n"+'Properties of various component matrices'+"\n")

for i in range(0,len(sparse_list)):
	componentMatrix = sparse_list[i]
	
	csrForm = componentMatrix.tocsr()
	normMatrix = onenormest(csrForm, t=3, itmax=5, compute_v=False, compute_w=False)
	
	#diffFlag = numpy.allclose(csrForm.data, csrForm.transpose().data)
       	#symmFlag = 'symmetric' if diffFlag else 'not symmetric'
	
	eps = pow(10,-9)
	rank = estimate_rank(aslinearoperator(componentMatrix), eps)
	#print 'Approximate rank with relative error of(', eps, ')for numerical rank definition = ',rank
	
	print obj.data_file_list[i],obj.data_file_name[i],componentMatrix.shape,' NonZeros = ',componentMatrix.nnz,' 1-Norm = ',normMatrix,' rank ',rank
	obj.logger_i.info(obj.data_file_list[i]+' '+obj.data_file_name[i]+str(componentMatrix.shape)+' NonZeros = '+str(componentMatrix.nnz)+' 1-Norm = '+str(normMatrix)+' rank '+str(rank))
	
	#saving the sparsity pattern
	fig = plt.figure(figsize=(24.0, 15.0))
	fig.clf()
	fig.gca().add_artist(plt.spy(componentMatrix))
	brake.save(obj.output_path+'dataAnalysis/'+obj.data_file_name[i], ext="png", close=True, verbose=False)
        

end_program = timeit.default_timer()

print "\n","\n","\n",'Total Run Time = : '+"%.2f" % (end_program-begin_program)+' sec'

if(obj.log_level):
    obj.logger_i.info('\nNote: The rank obtained using python estimate_rank utility') 
    obj.logger_i.info('is observed to be lower than the rank obtained using MATLAB')
    obj.logger_i.info('\nNote: The norm computed is a lower bound of the 1-norm of the sparse matrix.')
    obj.logger_i.info("\n"+"\n"+'Finished Data Analysis')

    #----------------Logging Time Complexity-----
    obj.logger_i.info('Time Taken for data analysis: '+"%.2f" % (end_program-begin_program)+' sec')
