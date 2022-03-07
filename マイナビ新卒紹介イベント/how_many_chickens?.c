#include<stdio.h>
    
int main()
{
	int i,N;
	unsigned long sum;
	
	/*read value of N*/
	
	scanf("%d",&N);
	
	/*set sum by 0*/
	sum=0;
	
	/*calculate sum of the series*/
	for(i=1;i<=N;i++)
		sum= sum+ (2*i);
	
	/*print the sum*/
	
	printf("%ld", sum);
	
	return 0;
}
