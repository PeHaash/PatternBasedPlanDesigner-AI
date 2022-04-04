#include "TBGE.h"

nTBGE::TBGE::TBGE(std::string Folder, std::string FileName){
	Address = Root + Folder + "/" + FileName + ".TBGE";
	size = 0;
	Output.clear();
}

int nTBGE::TBGE::SetFrame(int FrameNumber){
	// cout <<"dfd"<<endl;
	Output.push_back("FRAME: Code=" + std::to_string(FrameNumber));
	return size++;
}

int nTBGE::TBGE::AddArgument(int line, std::string arg){
	Output[line]+= " " + arg + " ";
	return line;
}

/*
template <typename T> int nTBGE::TBGE::AddArgument(int line, std::string arg, T state){
	Output[line]+= " " + arg + "=" + std::to_string(state) + " ";
	return line;
}*/

void nTBGE::TBGE::Clear(){
	Output.clear();
	size=0;
}

void nTBGE::TBGE::End(){
	std::ofstream fout(Address);
	for(int i = 0; i < size; i++){
		fout << Output[i] <<'\n';
	}
	fout.close();
}
