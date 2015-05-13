num=13195;
max=0;
def isPrime(x)
  (2..x/2).each do |i|
    if x%i==0
      return false
    end
  end
  return true
end

def isMax(x,max)
  if max<x
    max=x
  end
  return max
end

(2..num).each do |i|
  if isPrime(i)
    if num%i==0
      while num%i==0
        num=num/i
        max=isMax(i,max)
      end
    end
  end
end
print max