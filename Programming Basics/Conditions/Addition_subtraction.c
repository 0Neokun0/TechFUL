#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n,m,sum,sub;

scanf("%d%d",&n,&m);
sum=n=m;
sub=n-m;
if(sum>sub)
{
  printf("Yes");
}
else
{
  printf("No");
}
return 0;
}