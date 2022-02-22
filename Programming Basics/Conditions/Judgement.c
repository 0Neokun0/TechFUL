#include <stdio.h>
int main() {
    int x;
	
	scanf("%d", &x);

	
	   if(x == 0){
			printf("even");
		} 
		else if(x < 0 && (x%2) != 0) 
		{
			printf("odd");
		} 
		else if(x < 0 && (x%2) == 0) 
		{
			printf(" even");
		} 
		else if(x > 0 && (x%2) != 0) 
		{
			printf("odd");
		} 
		else if(x > 0 && (x%2) == 0) 
		{
			printf("even");
		} 	
	
	return 0;
}