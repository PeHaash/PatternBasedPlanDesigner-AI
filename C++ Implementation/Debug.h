// # define CODE_IS_IN_DEBUG_MODE
#ifdef CODE_IS_IN_DEBUG_MODE
	#define __DEBUG cerr <<">>>>>HERE:"<<__FILE__<<"\t\t@"<<__LINE__<<endl;
	#define __PRINT(x) cerr<<"!  DATA:\t"<<#x<<"\t:"<<x<<endl;
#else
	#define __DEBUG
	#define __PRINT(x)
#endif