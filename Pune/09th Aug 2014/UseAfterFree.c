/* HackSys Team - http://hacksys.vfreaks.com/
 * Github       - https://github.com/hacksysteam/
 * Twitter      - @HackSysTeam
 */

#include<stdio.h>

int main(void)
{
    // malloc() returns pointer to start of the
    // allocated heap memory block
    char *buffer = malloc(8);
    strcpy(buffer, "AAAAAAAA");
    
    printf("\nBefore free\n");
    printf("char *buffer: 0x%x\n", buffer);
    printf("buffer      : %s\n", buffer);
    
    // free the allocated memory
    free(buffer);
    
    // Use After Free
    printf("\nAfter free\n");
    printf("char *buffer: 0x%x\n", buffer);
    printf("buffer      : %s\n", buffer);
    
    return 0;
}
