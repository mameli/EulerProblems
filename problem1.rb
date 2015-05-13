x=0
(1..10).each do |i|
	if (i%3==0 || i%5==0)
		x=x+i
	end
end

print x