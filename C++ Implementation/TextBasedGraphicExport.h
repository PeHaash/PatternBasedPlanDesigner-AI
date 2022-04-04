#ifndef TEXTBASEDGRAPHICEXPORT_H
#define TEXTBASEDGRAPHICEXPORT_H

#include <vector>
#include <string>
#include <fstream>
// #include <sstream>



using namespace std;

namespace TextBasedGraphicExport{
	class TBGE;
}

class TextBasedGraphicExport::TBGE {
private:
	string Address;
	int size;
	vector<string> Output;
public:
	TBGE(string Folder, string FileName){
		Address = "./" + Folder + "/" + FileName + ".TBGE";
		size = 0;
	}

	int SetFrame(int FrameNumber){
		Output.push_back("FRAME: Code=" + FrameNumber + '\n');
		return ++size;
	}

	template <typename T>
	int AddLine(T x0, T y0, T x1, T y1){
		Output.push_back("LINE: x0=" + to_string(x0) +
			"y0=" + to_string(y0) +
			"x1=" + to_string(x1) +
			"y1=" + to_string(y1)
			);
		return ++size;
	}

	template <typename T>	
	int AddRectangle(vector<T> Pos){
		Output.push_back(
			"RECTANGLE x0=" + to_string(Pos[0]) +
			"y0=" + to_string(Pos[1]) +
			"x1=" + to_string(Pos[2]) +
			"y1=" + to_string(Pos[3])			
			);
		return ++size;
	}

	template <typename T>
	int AddArgument(int line, string arg, T state){
		Output[line]+= arg + "=" + to_string(state) + " ";
		return line;
	}

	void Clear(){
		Output.clear();
		size=0;
	}

	void End(){
		fstream fin = fstream(Address);
		for(int i = 0; i < size; i++){
			fin << Output[i] <<'\n';
		}
		fin.close();
	}

	



};


#endif
