#include <stdio.h>
#include<stdlib.h>
int main()
{
    char *str=(char *)malloc(100*sizeof(char));
    scanf("%s",str);
    if(str[0] == 'k')
    {

    str=&str[1];
    printf("%s",str);
}
  else
  printf("%s",str);
    return 0;
}