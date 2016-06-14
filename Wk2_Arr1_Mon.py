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


print "\n############# Push Front #################"
arr = [34, 57, 89, 35,21]	#starting array
valToInsert = 53			#value to insert
print "Before insert:",arr
print "Value to insert:",valToInsert
print "After insert:",PushFront(arr,valToInsert)
