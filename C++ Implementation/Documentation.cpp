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

// vector<int> vect{ 10, 20, 30 };   //to make vectors
// vaghti mikhay ye zahre mari ro initialize koni vali chizi toosh narizi, esmeclass(){} faramoosh nashe!!!!!
// friend: too tarife ye class, ye seri tabe' ro friend mikonim ke oona mitoonan hameye private ha ro bebinan!
// template <typename T> void sum(T a, T b) ... vase har call ke 2 no' type bashe, ye bar tabe' ro misaze o mikone too code
// foreach = for(Subspace::SUBSPACE ss : Subspace) ss.Print();
// agar iterator ma Random Access bashe, mishe oono +8 ya -85 kard! (mesle it haye vector) vali too set o ina nemishe
//  std::cout <<typeid(a).name(); nekbat typeid hatta to std ham nist! hast kollan


        // for (map<int,vector<int>>::iterator it = minXs.begin(); it!=minXs.end(); it++){
        //  cout<< it->first<<":";
        //  for (unsigned int i = 0; i < it->second.size(); i++){
        //      cout <<(it->second)[i]<<" ";
        //  }
        //  cout <<endl;
        // }