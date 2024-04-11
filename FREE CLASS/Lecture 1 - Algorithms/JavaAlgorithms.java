package com.aycodez;
import java.util.Arrays;
import java.util.Scanner;

public class JavaAlgorithms {

    public static boolean binarySearch(int[] array, int numSearch){
        return bSearch(array,numSearch,0,array.length -1 );
    }


    private static boolean bSearch(int[] array, int numSearch, int first , int last){
        if (Math.abs(last - first ) < 2)   {
            return array[first] ==  numSearch || array[last] == numSearch;
        }
        int mid = (last + first) / 2;
        if (array[mid] == numSearch){
            return true;
        }
        if (numSearch < array[mid]){
            return bSearch(array, numSearch, first, mid);

        }
        return bSearch(array,numSearch, mid, last);
    }

    public static int[] selectSort(int[] array){
        for (int i = 0; i < array.length-1; i++) {
            int min = i;
            for (int j = i + 1; j < array.length; j++) {
                if (array[min] > array[j]){
                    min = j;
                }

            }
            int temp = array[i];
            array[i] = array[min];
            array[min] = temp;

        }
        return array;
    }

      
    public static void main(String[] args){
        System.out.println(".........Staring binary search...........");
        int[] array = {1,2,3,4,5,6};
        int numSearch = 9;
        System.out.println("Found: " + binarySearch(array, numSearch));

        System.out.println("\n.......Selection sort.........");
        int[] unSortedArray = {3,2,65,1,0};
        System.out.println("Sorted Array: " + Arrays.toString(selectSort(unSortedArray)));

        

    }
}
