/* HackSys Team - http://hacksys.vfreaks.com/
 * Github       - https://github.com/hacksysteam/
 * Twitter      - @HackSysTeam
 */

#include<stdio.h>

int main(void)
{
    unsigned int i = 0xFFFFFFFF;
    int j = 1;
    
    // 0xFFFFFFFF + 1 = 100000000
    int k = i + j;
    
    // Integer Overflow
    printf("========= Integer Overflow =========\n");
    printf("int i = 0x%x (%d)(%d bits)\n", i, i, sizeof(i) * 8);
    printf("int j = 0x%x (%d)(%d bits)\n", j, j, sizeof(j) * 8);
    printf("int k = 0x%x (%d)(%d bits)\n", k, k, sizeof(k) * 8);
    printf("====================================\n");
    
    int abc = 0xdeadbeef;
    short xyz = abc;
    
    // Integer Demoting
    printf("========= Integer Demotion =========\n");
    printf("int   abc = 0x%x (%d bits)\n", abc, sizeof(abc) * 8);
    printf("short xyz = 0x%x (%d bits)\n", xyz, sizeof(xyz) * 8);
    printf("====================================\n");
    
    return 0;
}
     
