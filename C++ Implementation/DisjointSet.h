#ifndef DISJOINT_SET_H
#define DISJOINT_SET_H

#include <vector>
#include <numeric>
#include <bits/stdc++.h>

namespace nDisjointSet{
	class DisjointSet;
}

class nDisjointSet::DisjointSet{
	private:
		std::vector<int> Par;
		int NumberOfSets;
		int NumberOfElements;
	public:
		DisjointSet() = default;  // vase in ke betoonam alaki tarifesh konam ke ba'dan kamel she
		DisjointSet(int n);
		int FindParent(int p);
		void Join(int a, int b);
		int GetNumOfSets();
		int GetDisjointnessOfElements(std::vector<int> indexes);
};

////////////////////////////////////////////////////////////////////////////////////////////////////


nDisjointSet::DisjointSet::DisjointSet(int n){
	Par = std::vector<int> (n,-1);
	NumberOfSets = n;
	NumberOfElements = n;
}

int nDisjointSet::DisjointSet::FindParent(int p){
	if (Par[p] == -1) return p;
	return Par[p]=FindParent(Par[p]);
}

void nDisjointSet::DisjointSet::Join(int a, int b){
	if (FindParent(a) != FindParent(b)){
		Par[FindParent(a)] = FindParent(b);
		NumberOfSets--;
	}
}

int nDisjointSet::DisjointSet::GetNumOfSets(){
	return NumberOfSets;
}

int nDisjointSet::DisjointSet::GetDisjointnessOfElements(std::vector<int> indexes){
	std::vector<int> dsize (NumberOfElements, 0);
	for(unsigned int i = 0; i < indexes.size(); i++){
		dsize[FindParent(indexes[i])]++;
	}
	return accumulate(dsize.begin(),dsize.end(),0) - *max_element(dsize.begin(),dsize.end());
}

#endif