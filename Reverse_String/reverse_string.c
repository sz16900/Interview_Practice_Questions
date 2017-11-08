#include <stdio.h>
#include <stdlib.h>	

int main() {
    unsigned int len_max = 128;
    unsigned int current_size = 0;
    
    char *pStr = malloc(len_max);
    current_size = len_max;

    printf("\nPLease, type a string, it doesn't matter how long, I can always realloc ;)" \
    	" and it will be flipped!: ");

    if (pStr != NULL) {
		int c = EOF;
		int i = 0;
	    //accepts the user input 'till enter or enf od file
		while (( c = getchar() ) != '\n' && c != EOF) {
			pStr[i++]=(char)c;

			//if i reaches maximun size, the reallocate more memory
			if (i == current_size) {
	           	current_size = i+len_max;
				pStr = realloc(pStr, current_size);
			}
		}
		pStr[i] = '\0';

		// Lets reverse it!
    	char *pRever_Str = malloc(i);
    	int x = 0;
		for (i = i-1; i >= 0; i--) {
			pRever_Str[x++] = pStr[i];
		}
		printf("%s\n", pRever_Str);
		// Always free your mallocs, callocs and reallocs
		free(pStr);
		free(pRever_Str);
		pStr = NULL;
		pRever_Str = NULL;
    }

    return 0;
}