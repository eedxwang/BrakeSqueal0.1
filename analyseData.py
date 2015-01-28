# This file reads the component matrices and displays there sparsity pattern
# and other properties

#----------------------------------Standard Library Imports---------------------------------------
import timeit
import matplotlib.pylab as plt
import scipy.sparse.linalg as norm

#----------------------------Application Specific Imports-----------------------------------------
import createBrakeClassObject
from brake.initialize import load




begin_program = timeit.default_timer()


#----------------------------Create Object--------------------------------------------------------
obj = createBrakeClassObject.returnObject()

if(obj.log_level):
  obj.logger_i.info("\n"+"\n"+'Beginning Data Analysis')
  obj.logger_i.info('------------------------------------------------------------------------')

print "\n"+"\n"+'Beginning Data Analysis'

sparse_list = load.load_matrices(obj)

obj.logger_i.debug("\n"+'Matrices in CSC format converted to CSR')

obj.logger_i.debug("\n\n"+'Properties of various component matrices'+"\n")

for i in range(0,len(sparse_list)):
	componentMatrix = sparse_list[i]
	normMatrix = norm.onenormest(componentMatrix.tocsr(), t=3, itmax=5, compute_v=False, compute_w=False)
	print obj.data_file_list[i], obj.data_file_name[i], ' NonZeros = ', componentMatrix.nnz, ' 1-Norm = ', normMatrix
	obj.logger_i.debug(obj.data_file_list[i]+' '+obj.data_file_name[i]+' Nonzeros = '+str(componentMatrix.nnz)+' 1-Norm = '+str(normMatrix))
	
	#saving the sparsity pattern
	fig = plt.gcf()
	fig.clf()
	fig.gca().add_artist(plt.spy(componentMatrix))
        fig.savefig(obj.output_path+'dataAnalysis/'+obj.data_file_name[i]+'.png')


end_program = timeit.default_timer()

print "\n","\n","\n",'Total Run Time = : '+"%.2f" % (end_program-begin_program)+' sec'

if(obj.log_level):
    obj.logger_i.info("\n"+"\n"+'Finished Data Analysis')

    #----------------Logging Time Complexity-----
    obj.logger_t.info('Time Taken for data analysis: '+"%.2f" % (end_program-begin_program)+' sec')
