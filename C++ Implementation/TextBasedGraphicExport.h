#ifndef TEXTBASEDGRAPHICEXPORT_H
#define TEXTBASEDGRAPHICEXPORT_H

#include <vector>
#include <string>
#include <fstream>
// #include <iostream>
// #include <sstream>



namespace TextBasedGraphicExport{
	class TBGE;
}

class TextBasedGraphicExport::TBGE {
private:
	std::string Address;
	int size;
	std::vector<std::string> Output;
	const std::string Root = "E:/PBPDAI/";
public:
	TBGE(){};
	TBGE(std::string Folder, std::string FileName){
		Address = Root + Folder + "/" + FileName + ".TBGE";
		size = 0;
		Output.clear();
	}

	int SetFrame(int FrameNumber){
		// cout <<"dfd"<<endl;
		Output.push_back("FRAME: Code=" + std::to_string(FrameNumber));
		return size++;
	}

	template <typename T>
	int AddLine(T x0, T y0, T x1, T y1){
		Output.push_back("LINE: x0=" + std::to_string(x0) +
			" y0=" + std::to_string(y0) +
			" x1=" + std::to_string(x1) +
			" y1=" + std::to_string(y1)
			);
		return size++;
	}

	template <typename T>	
	int AddRectangle(std::vector<T> Pos){
		Output.push_back(
			"RECTANGLE: x0=" + std::to_string(Pos[0]) +
			" y0=" + std::to_string(Pos[1]) +
			" x1=" + std::to_string(Pos[2]) +
			" y1=" + std::to_string(Pos[3])			
			);
		return size++;
	}

	int AddArgument(int line, std::string arg, std::string state){
		Output[line]+= " " + arg + "=\"" + state + "\" ";
		return line;
	}

	template <typename T>
	int AddArgument(int line, std::string arg, T state){
		Output[line]+= " " + arg + "=" + std::to_string(state) + " ";
		return line;
	}

	void Clear(){
		Output.clear();
		size=0;
	}

	void End(){
		std::ofstream fout(Address);
		for(int i = 0; i < size; i++){
			fout << Output[i] <<'\n';
		}
		fout.close();
	}

};


#endif
