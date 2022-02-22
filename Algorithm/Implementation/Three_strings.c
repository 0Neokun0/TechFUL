#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
    int i;
    int tot[20];
    int len; /*length of string*/
    char nam[20]; /*the variable the user will be entering*/
    char nnam[20]; /*new name variable.
                   where the longest is kept*/

    for (i = 0; i < 3; i++){ /*user input of 6 strings*/
        
        scanf("%s", nam);

        len = strcmp(nnam, nam); /*comparing length of input 
                                 to stored string*/

        if (strlen(nam) > strlen(nnam)){
            strcpy(nnam, nam);
}
    }

    printf("%s", nnam);
    

    return 0;
}