#ifndef TEXTBASEDGRAPHICEXPORT_H
#define TEXTBASEDGRAPHICEXPORT_H

#include <vector>
#include <string>
#include <fstream>

namespace nTBGE{
	class TBGE;
}

class nTBGE::TBGE {
private:
	std::string Address;
	int size;
	std::vector<std::string> Output;
	const std::string Root = "E:/PBPDAI/";
	// int 
public:
	TBGE(){};
	TBGE(std::string Folder, std::string FileName);
	int SetFrame(int FrameNumber);
	template <typename T> int AddLine(T x0, T y0, T x1, T y1);
	template <typename T> int AddRectangle(std::vector<T> Pos);
	int AddArgument(int line, std::string arg);
	// template <typename T> int AddArgument(int line, std::string arg, T state);
	void Clear();
	void End();
};

template <typename T> int nTBGE::TBGE::AddLine(T x0, T y0, T x1, T y1){
	Output.push_back("LINE: x0=" + std::to_string(x0) +
		" y0=" + std::to_string(y0) +
		" x1=" + std::to_string(x1) +
		" y1=" + std::to_string(y1)
		);
	return size++;
}

template <typename T> int nTBGE::TBGE::AddRectangle(std::vector<T> Pos){
	Output.push_back(
		"RECTANGLE: x0=" + std::to_string(Pos[0]) +
		" y0=" + std::to_string(Pos[1]) +
		" x1=" + std::to_string(Pos[2]) +
		" y1=" + std::to_string(Pos[3])			
		);
	return size++;
}

#endif