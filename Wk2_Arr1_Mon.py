#Insert a given value at the beginning of the given array, without using any built-in array methods.

def PushFront(arr,valToInsert):
	#Insert a given value at the beginning of the given array, without using any built-in array methods.
	#recast value to insert as string
	valToInsert = str(valToInsert)
	#iterate the array
	for i in range (0,len(arr)):
		#concatenate value to insert with values from array, comma seperated
		valToInsert += ("," + str(arr[i]))
	#split the comma seperatev variable, convert to integer and reload array
	arr = [int(e) for e in valToInsert.split(',')]

	return arr


def InsertAt(arr,ndx,val):
	#initialize string to hold comma separated values from array
 	valToInsert = ""
 	#iterate the array up to the passed index
 	for i in range (0,ndx):
 		#concatenate elements from array as comma separated strings
 	 	if i == 0:
 	 		valToInsert += str(arr[i])
 	 	else:
	 		valToInsert += ("," + str(arr[i]))
	#concatenate value to add to string
	valToInsert += ("," + str(val))
	#iterate remaining elements from array after index
	for i in range (ndx,len(arr)):
		#concatenate remaining values to variable
		valToInsert += ("," + str(arr[i]))
	#split the comma seperatev variable, convert to integer and reload array
	arr = [int(e) for e in valToInsert.split(',')]
	return arr


def PopFront(arr):
	front = arr.pop(0)
	return front


def RemoveAt(arr,ndx):
	remove = arr.pop(ndx)
	return remove


print "\n############# Push Front #################"
arr = [34, 57, 89, 35,21]	#starting array
valToInsert = 53			#value to insert
print "Before insert:",arr
print "Value to insert:",valToInsert
print "After insert:",PushFront(arr,valToInsert)


print "\n############## Insert At ##################"
arr = [34, 57, 89, 35,21]	#starting array
ndx = 4						#index to add val
valToInsert = 66					#value to insert
print "Before insert:",arr
print "Value to insert:",valToInsert
print "Insert at index:",ndx
print "After insert:",InsertAt(arr,ndx,valToInsert)


print "\n############# Pop Front #################"
arr = [34, 57, 89, 35,21]	#starting array
print "Remove first value:",PopFront(arr)


print "\n############# Remove At #################"
arr = [34, 57, 89, 35,21]	#starting array
ndx = 3						#index to remove
print "Remove:",RemoveAt(arr,ndx),"from index:",ndx
