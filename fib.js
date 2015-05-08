var k=0;
var sum=0;
for(var i=1;i<50;){
  if(i==1)i=2,k=1;
  i+=k;
  k=i-k;

  if (i%2==0)sum+=i;
}
sum+=2;
console.log(sum);
