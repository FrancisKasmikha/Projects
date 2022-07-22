#pragma once

#include <iomanip>
#include <iostream>
using std::cin;
using std::cout;
using std::ifstream;
using std::ofstream;
using std::endl;
#include <map>
using std::map;
using std::pair;
using std::make_pair;
#include <iterator>
using std::iterator;
#include <string>
using std::string;
#include <algorithm>
#include <numeric>
#include <vector>
using std::vector;
#include <set>
using std::set;
#include <functional>
#include <fstream>

int GetPointTotalForStudent(map<string, string> student_info, string keyword);
int GetTopNHomeworkTotalForStudent(map<string, string> student_info,
                                   int keyword);
int GetNumberOfMissingLabsForStudent(map<string, string> student_info);
bool cmp(pair<string, int>& a, pair<string, int>& b);
vector<pair<string, int>> sort(map<string, int>& M);
int GetPointTotalForStudent(map<string, string> student_info);
map<string, double> GetIDToGrade(map<string, map<string, string>> student_info);
map<string, map<string, string>> GetIDToInfoFromCSV(string a);
std::set<std::string> GetStudentsEligibleForHonorsCredit(
    map<string, map<string, string>> student_info, int a);