#include <iostream>
#include <math.h>

using namespace std;

double fun(double x);
double dfun(double x);

int main()
{
  double x0,eps,x;

  x0=-1;
  eps=pow(10,-10);

  while(abs(fun(x0))>eps){

    x=x0-fun(x0)/dfun(x0);
    x0=x;

  }

  printf("%f",x);

  return 0;

}

double fun(double x)
{
  return pow(x,2)-2;
}

double dfun(double x)
{
  return 2*x;
}