#include <stdio.h>

int main(void)
{
    int i = 0, n;
    scanf("%d", &n);
    double arr[n];
    while(i < n)
    {
        scanf("%lf", &arr[i]);
        i++;
    }
    for(int j = 0; j < n; j++)
        printf("%0.2lf\n", arr[j]);
    return 0;
}