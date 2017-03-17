import scipy.io as sio
import math
import statistics
matfile = sio.loadmat('changed_param_2.mat')
old_mat = sio.loadmat('learned_all_param_2.mat')

#for i in range(15):
#print matfile['p'][[11 ,67 ,225,336,357,444,635,679],0],old_mat['p'][[11 ,67 ,225,336,357,444,635,679],0]

count = 0
mea_ceil = []
mea_floor = []
mea_old_ceil = []
mea_old_floor = []
for a in matfile['new_ratings']:
    if int(a) > 0:
	original_rating = matfile['p'][count,0]
	old_rating = old_mat['p'][count,0]
	mea_ceil.append(int(a) - math.ceil(original_rating))
	mea_floor.append(int(a) - math.floor(original_rating))
	mea_old_ceil.append(int(a) - math.ceil(old_rating))
	mea_old_floor.append(int(a) - math.floor(old_rating))
	#print count,a,original_rating,old_rating
    count = count + 1

print statistics.mean(mea_ceil),statistics.mean(mea_floor)
print statistics.mean(mea_old_ceil),statistics.mean(mea_old_floor)


print mea_ceil.count(0),mea_floor.count(0)
print mea_old_ceil.count(0),mea_old_floor.count(0)

print len(mea_ceil)

