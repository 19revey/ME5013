#include <iostream.h>
#include "functions.h"

int main(){
    print_hello();
    int num;
    cout << endl;
    cout << "Enter your number " << endl;
    cin >> num;
    cout << "The factorial is " << factorial(num) << endl;
    return 0;
}
