#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>

// #include <string_view>

using namespace std;

// namespace kiri{
// 	int aaa;
// 	class patt;
// }

namespace plangooz{
	class plan{
		int a,b,c;
	public:
		void set(int n){
			a = n + 1;
			b = n + 4;
			c = a + b;
		}
		void print(){
			cout <<a <<' ' <<b <<c;
		}
		void dool(plan gg);
		class patt;
	};
}

// namespace plangooz{
void plangooz::plan::dool(plangooz::plan gg){
	cout << gg.a;
}

class plangooz::plan::patt{
	plangooz::plan gg;
	public:
	patt() = default;
	void a1(){
		gg.a = 5;
		gg.b = 33;
		gg.c = 4;
	}
	void a2(plangooz::plan dd){
		dd.a = 4;
	}
};
// }

// namespace plangooz{
// 	class plan;
// }

int main(){

	int a,b;
	cin >>a >>b;
	cout <<a*b<<endl;
	plangooz::plan::patt d;
	d.a1();

	// std::set<int> a{1,2,4,5};
	// set<int> b{3,5,6,7,2};
	// set<int> c(a);
	// a.merge();

	// for(auto& aa:c) cout<<aa<<" ";
	// cout<<endl;


	// Features::FEATURES Features(300, 300, {1, 1, 1}, 6, 0.5 );
	// PlanMaker::PLAN pp(&Features, NumericDataMaker::RandomNumericData(16), NULL, -1);
	return 0;
	// PlanMaker::PLAN t(Features,)
}


