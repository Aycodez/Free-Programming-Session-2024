# include <stdio.h>
# include <math.h>

// NewtonRapshon method
void NRmethod(double init_approx)
{
    float present_x = init_approx;
    float epsilon = 0.00001;
    
    float fx = (pow(present_x, 3))- (5 * present_x) + 1;
    float diff = (3 * pow(present_x, 2)) - 5;
    float nextx = present_x - fx / diff;
    int i = 1;
    

    while (fabs(present_x - nextx) > epsilon && i < 100){
        printf("%i iteration: %lf\n", i, nextx);
        i += 1;
        present_x = nextx;
        fx = (pow(present_x, 3)) - (5 * present_x) + 1;
        diff = (3 * pow(present_x, 2)) - 5;
        nextx = present_x - fx / diff;
        
    }
        

    printf("%i iteration: %lf\n", i, nextx);
}

// Chebyshev successive method
void CBmethod(double init_approx)
{
    float present_x = init_approx;
    float epsilon = 0.00001;
    
    float fx = (pow(present_x, 3))- (5 * present_x) + 1;
    float diff = (3 * pow(present_x, 2)) - 5;
    float diff2 = 6 * present_x;
    float nextx = present_x - ((fx / diff) - (0.5 * (pow(fx, 2) / pow(diff, 3))) * diff2);
    int i = 1;
    

    while (fabs(present_x - nextx) > epsilon && i < 100){
        printf("%i iteration: %lf\n", i, nextx);
        i += 1;
        present_x = nextx;
        fx = (pow(present_x, 3)) - (5 * present_x) + 1;
        diff = (3 * pow(present_x, 2)) - 5;
        diff2 = 6 * present_x;
        nextx = present_x - ((fx / diff) - (0.5 * (pow(fx, 2) / pow(diff, 3))) * diff2);

        
    }
        

    printf("%i iteration: %lf\n", i, nextx);
}
    

// Main program
int main()
{
    printf("......Newton Raphsom method.....\n");
    NRmethod(0.5);
    printf("......Chebyshev method.....\n");
    CBmethod(0.5);
}