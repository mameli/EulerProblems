var num=600851475143;
var max=0;
function isPrime(x){
  for(var i=2;i<x;i++){
    if(x%i==0)return false;
  }
  return true;
}
function isMax(x){
  if(max<x)max=x;
}

var b=Date.now();
for (var i=2;i<=num;i++){
  if(isPrime(i)){
    if(num%i==0){
      while(num%i==0)num=num/i,isMax(i);
    }
  }
}
var e=Date.now()-b;
console.log("End "+e+"ms");
console.log(max);
