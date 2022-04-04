#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <map>
#include <string_view>
#include <experimental\string_view>

using namespace std;

int gooz(int a,int b){
	return a + b;
}

// class tbge{
// 	vector<string> A;
// 	public:
// 	tbge& operator << (string ss){
// 		A.push_back(ss);
// 		return *this;
// 	}
// 	void Print(){
// 		for(unsigned int i = 0; i < A.size(); i++){
// 			cout << A[i] << " -- ";
// 		}
// 	}

// };

// class TBGE {
// private:
// 	string Address;
// 	vector<string> Output;
// public:
// 	TBGE(string Folder, string FileName){
// 		Address = "./" + Folder + "/" + FileName + ".TBGE";
// 	}

// 	int SetFrame(int FrameNumber){
// 		Output.push_back("FRAME: Code=" + FrameNumber + '\n');
// 	}

// 	// template <typename T,typename B>
// 	int AddLine(int x0, int y0, int x1, int y1){


// 	}


	



// };

#include "TextBasedGraphicExport.h"

int main(){
	int a = 5;
	cout <<a++ <<endl;
	cout <<++a <<endl;

	TextBasedGraphicExport::TBGE ddd ("1 C++ Implementation" , "gooz");
	ddd.SetFrame(34);
	cout <<ddd.AddLine(34,53,12,53) <<endl;
	cout <<ddd.AddLine(434.5,5.3,2.3,53.0) <<endl;
	vector<int> fd;
	fd.push_back(34);
	fd.push_back(34);
	fd.push_back(342);
	fd.push_back(445);
	cout <<ddd.AddRectangle(fd) <<endl;
	ddd.AddArgument(2,"sdf",3);
	ddd.AddArgument(2,"wsdfsdf",34);
	ddd.End();

	// cout <<std::format();
	// TBGE AA("sdf","sdfsdf");
	// AA.SetFrame(34);

	// AA.AddLine(3,5,3,5,TBGE_ARGS(53,"444"));
	

	// AA <<"GGGG";
	// AA << "12" << "er" << "3242 ";
	// AA.Print();
	// cout << ("SHIT!",4) <<endl;
	// int a;
	// for (int i = 0; i < 100; i++){
	// 	cout << random() << endl;
	// }
	// cout << gooz(a=3, b=5) <<endl;
	// cin >>a;
	// cout <<(a + 5)<<endl;
	return 0;
}
