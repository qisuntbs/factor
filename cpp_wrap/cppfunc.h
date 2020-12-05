#ifndef CPPFUNC_H
#define CPPFUNC_H

// #include <fstream>
// #include <iostream>
// #include <sstream>
#include <string>
// #include <cstring>
#include <vector>

using namespace std;

class cppfunc{
public:
  // attribute
  // vector <vector <string> > data;

  // constructor:
  cppfunc();

  // methods:
  vector <vector <string> > data_as_string (string file_name);
  vector <vector <double> > data_as_double (string file_name);
  bool is_number(const string& s);
  virtual ~cppfunc ();  // destructor
};

#endif
