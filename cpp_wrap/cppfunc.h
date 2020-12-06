#ifndef CPPFUNC_H
#define CPPFUNC_H

#include <string>
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
  vector <int> remove_nan(vector <vector <double> > data, int num);

  bool is_number(const string& s);

  // destructor
  virtual ~cppfunc ();
};

#endif
