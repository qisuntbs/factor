#ifndef READ_CSV_H
#define READ_CSV_H

// #include <fstream>
// #include <iostream>
// #include <sstream>
#include <string>
// #include <cstring>
#include <vector>

using namespace std;

class table{
public:
  // attributes:
  string file_name;
  vector <vector <string> > data;

  // constructor:
  table ();
  table (string file_name);

  // methods:
  vector <vector <string> > data_as_string (string file_name);
  vector <vector <double> > data_as_double (string file_name);
  virtual ~table ();  // destructor
};

#endif
