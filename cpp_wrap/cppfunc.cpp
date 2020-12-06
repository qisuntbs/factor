/*
  Copyright (C) 2019, 2020 by Qi Sun

  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
*/

#include "./cppfunc.h"
#include <math.h>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

cppfunc::cppfunc(){
  // if you want wrap this into python
  // there should be no contents here by default
  // cerr << "ERROR: Make sure you have the right file name!" << endl;
  // exit(2);
}

// we don't need this constructor as 
// the main the purpose is to import cpp functions/methods:
// cppfunc::cppfunc(string file_name){
//   this->file_name = file_name;
// }

cppfunc::~cppfunc (){ }

vector <vector <string> > cppfunc::data_as_string(string file_name)
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


vector <vector <double> > cppfunc::data_as_double(string file_name)
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
	  if (is_number(s)) {
	    record.push_back( stod(s) );}
	  else record.push_back( NAN );  // math.h
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

bool cppfunc::is_number(const std::string& s)
{
  std::string::const_iterator it = s.begin();
  while (it != s.end() &&
	 (std::isdigit(*it) || *it=='-' || *it=='.')) ++it;
  // include '+'?
  return !s.empty() && it == s.end();
}

vector <int> cppfunc::remove_nan(vector <vector <double> > data,
					      int num)
{
  vector <int> out;
  int security_len = data.size();
  int time_len = data[0].size();
  for (int i = 0; i < security_len; ++i) {
    int c = 0;
    for (int j = 0; j < time_len; ++j) {
      if (isnan(data[i][j])) c++;
    }
    // remove ALL columns with nans by setting num = 1:
    if (c < num) out.push_back(i);
  }
  return out;
}
