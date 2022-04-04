#include <functional> // For std::function

bool IsGreaterThan(int a, int b){
    return a > b;
}

int main()
    {
    // 1. Create a lambda function that can be reused inside main()
    const auto sum = [](int a, int b) { return a + b;};

    int result = sum(4, 2); // result = 6

    // 2. Use std::function to use a function as a variable
    std::function<bool(int, int)> func = IsGreaterThan;

    bool test = func(2, 1); // test = true because 2 > 1
    }
