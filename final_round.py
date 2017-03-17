import scipy.io as sio
from math import ceil,floor
from statistics import mean
from numpy import square,sqrt,absolute
matfile = sio.loadmat( 'changed_param_2.mat' )
old_mat = sio.loadmat( 'learned_all_param_2.mat' )

#for i in range( 15 ):
#print matfile['p'][[11 ,67 ,225,336,357,444,635,679],0],old_mat['p'][[11 ,67 ,225,336,357,444,635,679],0]

count = 0
mea_ceil = []
mea_floor = []
mea_old_ceil = []
mea_round = []
mea_old_round = []

mea_old_floor = []
for a in matfile['new_ratings']:
    if int( a ) > 0:
	original_rating = matfile[count,0]
	old_rating = old_mat['p'][count,0]
	mea_ceil.append( absolute( int( a ) - ceil( original_rating ) ) )
	mea_round.append( absolute( int( a ) - round( original_rating ) ) )
	mea_floor.append( absolute( int( a ) - floor( original_rating ) ) )
	mea_old_ceil.append( absolute( int( a ) - ceil( old_rating ) ) )
	mea_old_floor.append( absolute( int( a ) - floor( old_rating ) ) )
	mea_old_round.append( absolute( int( a ) - round( old_rating ) ) )
	
	#print count,a,original_rating,old_rating
    count = count + 1

print mean( mea_ceil ),mean( mea_floor ), mean(mea_round)
print mean( mea_old_ceil ),mean( mea_old_floor ),mean(mea_old_round)

print sqrt( mean( square( mea_ceil ) ) ),sqrt( mean( square( mea_floor ) ) ),sqrt( mean( square( mea_round ) ) )
print sqrt( mean( square( mea_old_ceil ) ) ),sqrt( mean( square( mea_old_floor ) ) ),sqrt( mean( square( mea_old_round ) ) )

print mea_ceil.count( 0 )/len(mea_ceil),mea_floor.count( 0 )/len(mea_floor),mea_round.count( 0 )/len(mea_round)
print mea_old_ceil.count( 0 )/len(mea_old_ceil),mea_old_floor.count( 0 )/len(mea_old_floor),mea_old_round.count( 0 )/len(mea_old_round)

