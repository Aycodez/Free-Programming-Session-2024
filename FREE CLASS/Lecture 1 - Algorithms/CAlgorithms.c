# include <stdio.h>
# include <stdlib.h>
# include <math.h>



int binarysearch(int array[], int numSearch,int first,int last )
{
    
    if (abs(last - first) < 2)
    {
        if (array[first] == numSearch || array[last] == numSearch)
        {   printf("Found: True\n");
            return 0;
        }
        else{
            printf("Found: False\n");
            return -1;
        }
    
    }

    
    int mid = (last + first) / 2;
    
    if (array[mid] == numSearch)
    {
        printf("Found: True\n");
        return 0;
    }
    if (numSearch > array[mid])
    {
        return binarysearch(array, numSearch, mid, last);
    }
    else{
        return binarysearch(array, numSearch, first, mid);
    }
    
}


int *selectsort(int array[], int length)
{
    
    for (int i = 0; i < length-1; i ++ )
    {
        
        int minIndex = i;
        for (int j = i + 1; j < length; j ++)
        {
            if (array[minIndex] > array[j])
            {
                minIndex = j;
                
            }
        }

        
        int temp = array[i];
        array[i] = array[minIndex];
        array[minIndex] = temp;

       
    }
    printf("Sorted array: [");
    for (int num = 0; num < length; num++)
    {
        printf("%i,", array[num]);
    }
    printf("]\n");
    return array;

    
}



