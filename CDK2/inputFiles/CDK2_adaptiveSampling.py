# step 1
# raw plot

import glob
import pickle
import numpy as np
from matplotlib import pyplot as plt
from msmbuilder.decomposition import tICA
n_components = 2
lag_time = 50
sysName = 'cdk2'
alldist = []

for f in glob.glob('dists-cdk/Cdk*_dist1_LYS-GLU.npy'):
	print(f)
	x = np.load(f)
	x2 = np.load(f.replace('_dist1_LYS-GLU.npy','_dist3_aloop_ploop-dist.npy'))
	x3 = np.load(f.replace('_dist1_LYS-GLU.npy','_dist3_aloop_rmsd.npy'))
	dist1 = x[:,0]
	dist2 = x[:,1]
	dist3 = x2[:,0]
	dist4 = x3
	alldist.append(np.array([[dist1[i], dist2[i], dist3[i], dist4[i]] for i in range(len(dist4))]))

dataset = alldist
tica = tICA(n_components=n_components , lag_time=lag_time)
tica.fit(dataset)
tica_traj = tica.transform(dataset)
pickle.dump(tica, open('tica.pkl','wb'))
np.save('tica_traj', tica_traj)

# step 2
# project only list one on the tICs
import glob
import pickle
import numpy as np
from matplotlib import pyplot as plt
from msmbuilder.decomposition import tICA
n_components = 2
lag_time = 50
sysName = 'cdk2-list1'
alldist = []
list = []
for f in glob.glob('dists-list1/Cdk*_dist1_LYS-GLU.npy'):
	print(f)
	list.append(f)
	x = np.load(f)
	x2 = np.load(f.replace('_dist1_LYS-GLU.npy','_dist3_aloop_ploop-dist.npy'))
	x3 = np.load(f.replace('_dist1_LYS-GLU.npy','_dist3_aloop_rmsd.npy'))
	dist1 = x[:,0]
	dist2 = x[:,1]
	dist3 = x2[:,0]
	dist4 = x3
	alldist.append(np.array([[dist1[i], dist2[i], dist3[i], dist4[i]] for i in range(len(dist4))]))
dataset_list = alldist
tica = pickle.load(open('tica.pkl','rb'))
tica_traj_list = tica.transform(dataset_list)
np.save('tica_traj_list1', tica_traj_list)
np.savetxt('list', list)

# step 3

import glob
import numpy as np
from matplotlib import pyplot as plt
import pickle

sysName = 'cdk_0'
Flag =True
list = np.load('list.npy')
tica_traj = np.load('tica_traj_list1.npy')
num = 0
init_list =[]

for j in range(len(tica_traj)):
	x = tica_traj[j][:,0]
	y = tica_traj[j][:,1]

	for i in range(len(x)):
        	comp = x[i]
        	if comp<0.12:
            		plt.plot(x[i], y[i],'*', c='red')
            		num = num+1
            		init_list.append([list[j], i])
            		print(list[j], i)
	if Flag:
        	dist1 = x
        	dist2 = y
        	Flag = False
	else:
        	dist1 = np.concatenate((dist1,x))
        	dist2 = np.concatenate((dist2,y))
		
print(num)
figName = sysName+'_tics'
plt.hexbin(dist1, dist2, bins='log', mincnt=1, vmin = 0, vmax=3)
plt.xlabel('tIC1', fontsize = 14)
plt.ylabel('tIC2', fontsize = 14)
plt.xlim([-2, 1.5])
plt.ylim([-4, 3])
plt.colorbar()
pickle.dump(init_list, open('init_list', 'wb'))
plt.savefig(figName, dpi=300, bbox_inches='tight')
plt.show()


# step 4
import numpy as np
import mdtraj as md

inits_f = open('inits_md9.txt','rb')
inits = inits_f.readlines()

count = 0
stride = 1
this_round = '9'

for init in inits:
	init = init.decode()
	trj = init.split()[0]
	round = trj.split('.')[0][-1]       
	print(round)
	top = 'MD'+ round +'-rwTop/' + trj.replace('.mdcrd','.prmtop').replace('raw_cdk','cdk')
	rawTrj = 'MD'+ round +'-rwTrj/' + trj
	frame = init.split()[1]
	newTop = 'cdk'+str(count)+'_md'+this_round+'.prmtop'
	newrst = 'cdk'+str(count)+'_md'+this_round+'.rst'
	f = open('cppASample_'+str(count)+'.in', 'w')
	f.write('parm ' + top + '\n')
	f.write('trajin ' + rawTrj  + '\n')
	f.write('parmbox alpha 90 beta 90 gamma 90\n')
	f.write('autoimage origin \n')
	f.write('trajout ' + newrst + ' restart onlyframes ' + str((int(frame)*stride)+1) +'\n')
	f.write('parmwrite out ' + newTop +'\n')
	f.write('run \n')
	f.write('quit')
	f.close()
	count = count+1
	
