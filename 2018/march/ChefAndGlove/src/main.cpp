//
// Created by ratanparai on 3/11/18.
//

#include <iostream>

using namespace std;

int add(int numberOne, int numberTwo)
{
    return numberOne + numberTwo;
}

int main()
{
    cout << "Hello World!" << endl;
    int result;
    result = add(4,5);
    cout << "4 and 5 makes " << result << endl;

    return EXIT_SUCCESS;
}



