/* HackSys Team - http://hacksys.vfreaks.com/
 * Github       - https://github.com/hacksysteam/
 * Twitter      - @HackSysTeam
 */

#include<stdio.h>

int main(void)
{
    // uninitialized variable
    int num;
    
    // Use of Uninitialized variable
    printf("Address num: 0x%x\n", &num);
    printf("Value num  : %d\n", num);
    
    return 0;
}
