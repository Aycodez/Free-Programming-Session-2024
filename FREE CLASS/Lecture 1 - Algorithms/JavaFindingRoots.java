package com.aycodez;

public class JavaFindingRoots {
    public static void NRmethod(double init_approx){

        double present_x = init_approx;
        float epsilon = 0.00001F;

        double fx = Math.pow(present_x, 3) - (5 * present_x) + 1;
        double diff = (3 * Math.pow(present_x, 2)) - 5;
        double nextx = present_x - fx / diff;
        int i = 1;

        while (Math.abs(present_x - nextx) > epsilon && i < 100){
            System.out.println(i + "iteration:" + nextx);
            i += 1;
            present_x = nextx;
            fx = Math.pow(present_x, 3) - (5 * present_x) + 1;
            diff = (3 * Math.pow(present_x, 2)) - 5;
            nextx = present_x - fx / diff;
        }
        System.out.println(i + "iteration:" + nextx);

    }

    public static void CBmethod(double init_approx){
        double present_x = init_approx;
        float epsilon = 0.00001F;

        double fx = Math.pow(present_x, 3) - (5 * present_x) + 1;
        double diff = (3 * Math.pow(present_x, 2)) - 5;
        double diff2 = 6 * present_x;
        double nextx = present_x - ((fx / diff) - (0.5 * (Math.pow(fx, 2) / Math.pow(diff, 3)) * diff2));
        int i = 1;

        while (Math.abs(present_x - nextx) > epsilon && i < 100){
            System.out.println(i + "iteration:" + nextx);
            i += 1;
            present_x = nextx;
            fx = Math.pow(present_x, 3) - (5 * present_x) + 1;
            diff = (3 * Math.pow(present_x, 2)) - 5;
            nextx = present_x - fx / diff;
        }
        System.out.println(i + "iteration:" + nextx);
    }

    public static void main(String[] args){
        System.out.println(".....Chebyshev method......");
        CBmethod(0.5);
        System.out.println("\n.....Newton-Raphson method......");
        NRmethod(0.5);
    }
}
