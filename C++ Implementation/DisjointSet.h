// Disjoint Set in c++
#include <vector>
#include <iostream>
#include <numeric>
#include <bits/stdc++.h>
// #in
using namespace std;

namespace DisjointSet{
	class DISJOINTSET;
}

// std::vector<int> second (4,100);                       // four ints with value 100

class DisjointSet::DISJOINTSET{
	private:
		vector<int> Par;
		int NumberOfSets;
		int NumberOfElements;
	public:
		DISJOINTSET(int n){
			Par = vector<int> (n,-1);
			NumberOfSets = n;
			NumberOfElements = n;
		}
		int Parent(int p){
			if (Par[p] == -1) return p;
			return Par[p]=Parent(Par[p]);
		}
		void Join(int a, int b){
			if (Parent(a) != Parent(b)){
				Par[Parent(a)] = Parent(b);
				NumberOfSets--;
			}
		}
		int NumOfSets(){
			return NumberOfSets;
		}
		int DisjointnessOfElements(vector<int> indexes){
			vector<int> dsize (NumberOfElements, 0);
			for(unsigned int i = 0; i < indexes.size(); i++){
				dsize[Parent(indexes[i])]++;
			}
			return accumulate(dsize.begin(),dsize.end(),0) - *max_element(dsize.begin(),dsize.end());
		}
};

int main(){
	DisjointSet::DISJOINTSET joon(5);
	joon.Join(1,4);
	joon.Join(1,3);
	cout <<joon.Parent(4)<<" "<<joon.DisjointnessOfElements({0,1,2,3,4})<< endl;

	return 0;
}
