#include "quad.h"
#include <stdio.h>

double quad(double *x, int nx, double *y, int ny)
{
    int i;
    double sum = 0.0;
    for (i=0; i<nx-1; i++){
        sum += (y[i+1] + y[i])*(x[i+1] - x[i])/2.;
    }
    return sum;
}
