#include "./read_csv.h"
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

table::table(){
  // if you want wrap this into python
  // there should be no contents here by default
  // cerr << "ERROR: Make sure you have the right file name!" << endl;
  // exit(2);
}

table::table(string file_name){
  this->file_name = file_name;
  this->data = data_as_string(file_name);
  // cout << data[0][0] << endl;
  // cout << data.size() << " lines of data" << endl;
}

table::~table (){ }

vector <vector <string> > table::data_as_string(string file_name)
  {
  vector <vector <string> > data;
  ifstream infile( file_name );
  while (infile)
    {
      string s;
      if (!getline( infile, s )) break;
      istringstream ss( s );
      vector <string> record;
      while (ss)
	{
	  string s;
	  if (!getline( ss, s, ',' )) break;
	  record.push_back( s );
	}
      data.push_back( record );
    }
  if (!infile.eof())
    {
      std::cerr << "ERROR: No such file - " <<
	file_name << std::endl;
      exit(2);
    }
  return data;
}


vector <vector <double> > table::data_as_double(string file_name)
  {
  vector <vector <double> > data;
  ifstream infile( file_name );
  while (infile)
    {
      string s;
      if (!getline( infile, s )) break;
      istringstream ss( s );
      vector <double> record;
      while (ss)
	{
	  string s;
	  if (!getline( ss, s, ',' )) break;
	  record.push_back( stod(s) );
	}
      data.push_back( record );
    }
  if (!infile.eof())
    {
      std::cerr << "ERROR: No such file - " <<
	file_name << std::endl;
      exit(2);
    }
  return data;
}
