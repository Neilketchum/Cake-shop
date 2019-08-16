a = list(map(int,input("Enter parent Array").split()))
n = len(a)
contagsum = []
modarr = []
contagsum.append(0)
sum = 0
for i in a:
	sum += i
	contagsum.append(sum)
print(contagsum)
for i in range(len(contagsum)):
	contagsum[i] = contagsum[i] % n
print(contagsum)
no_of_good_arrays = 0
selected = []
for i in range(len(contagsum)):
	flag = 0 
	for j in range(i,len(contagsum)):
		if(a[j] not in selected):
			if(contagsum[i] == contagsum[j]):
				selected.append(a[j])
				flag = contagsum.count(a[j])
	print(flag)
	no_of_good_arrays += (flag * (flag-1))/2
print(no_of_good_arrays)

