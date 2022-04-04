// # define CODE_IS_IN_DEBUG_MODE
#ifdef CODE_IS_IN_DEBUG_MODE
	#define MACRO_FLAG cerr <<">>>>>HERE:"<<__FILE__<<"\t\t@"<<__LINE__<<endl;
	#define MACRO_PRINT (x) cerr<<"!  DATA:\t"<<#x<<"\t:"<<x<<endl;
#else
	#define MACRO_FLAG
	#define MACRO_PRINT(x)
#endif