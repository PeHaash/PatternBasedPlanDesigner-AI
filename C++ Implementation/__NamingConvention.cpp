// Naming Conventions:
#ifndef NAME_OF_HEADER_LIKE_THIS_H
#define NAME_OF_HEADER_LIKE_THIS_H

#include <firstc++libraries>
//enter
#include <thenotherlibraries>
//enter
#include "ThenMyHeaders.h"


namespace nNamespace{
    class NameOfClass{
        int PrivateThing;
        int *pPointer;

    public:
        void RunAMethod(){
            int alocalvariable;
        }


    };
}                                                                                                   // Comments Are Here

nNamespace::NameOfClass classobject;
classobject.RunAMethod();

#endif

// header                       --> UpperCamelCase
// namespace                    --> n + HeaderName = nHeaderName
// class                        --> UpperCamelCase
// class objects                --> flatcase
// methods of class             --> UpperCamelCase (StartsWithAVerb) at least two word
// variables of class           --> UpperCamelCase (DoNotStartWithAVerb)
// local variable               --> flatcase
// pointers                     --> p + name
// static                       --> s + ...
