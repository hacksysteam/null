/* HackSys Team - http://hacksys.vfreaks.com/
 * Github       - https://github.com/hacksysteam/
 * Twitter      - @HackSysTeam
 */

#include<stdio.h>

int main(int argc, char *argv[])
{
     char buffer[4];
     
     // Stack Overflow
     strcpy(buffer, argv[1]);
     printf("Please enter only four letter password: %s", buffer);
     
     return 0;
}
     
