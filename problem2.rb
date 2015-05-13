k=0
sum=2
i=1
while i<4*10**6
	if i==1
		i=2
		k=1
	end
	i=i+k
	k=i-k
	if i.even?
		sum=sum+i
	end
end
print sum