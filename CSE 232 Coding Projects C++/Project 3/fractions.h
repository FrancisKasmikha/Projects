#ifndef FRACTIONS_H
#define FRACTIONS_H


#include <iostream>
#include <iomanip>
#include <string>
using std::string;
#include <algorithm>
using std::for_each;
#include <vector>
using std::vector;
#include <sstream>
using std::istringstream;
#include <istream>
using std::istream;
using std::ostream;
#include <algorithm>
using std::for_each;
using std::endl;
#include <string.h>
using std::ostringstream;
#include <ios>
using std::ios;
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>     /* srand, rand */
#include <time.h>
#include <random>
#include <stdexcept>
using std::out_of_range;
#include <iterator>
using namespace std;

struct Fractions{
public:
    Fractions()= default;
    Fractions(string fracvalue);
    void reduce();
    void add(Fractions);
    void sub(Fractions);
    void div(Fractions);
    void mult(Fractions);
    void divint(int);
    void multint(int);
    string fractostr();
    Fractions &operator=(Fractions const &);
    int num = 0;
    int den = 1;
    int whole = 0;
    string aa = "";

    friend int gcd(int,int);
    friend ostream &operator<<(ostream &, Fractions const &);
};
Fractions &Fractions::operator=(Fractions const&f){
    num = f.num;
    den = f.den;
    whole = f.whole;
    return *this;
}
string Fractions::fractostr(){
    stringstream out;
    Fractions firstval("0/1");
    firstval.num = num;
    firstval.den = den;
    firstval.whole = firstval.num / firstval.den;
    firstval.num = firstval.num % firstval.den;
    firstval.reduce();
    if (firstval.whole == 0)
    {
        out<<firstval.num<<"/"<<firstval.den;
    }
    else if ((firstval.num == 0) &&(firstval.den == 1))
    {
        out<<firstval.whole;
    }
    else {
        out<<firstval.whole<<"-"<<firstval.num<<"/"<<firstval.den;
    }
    string final = out.str();
    return final;
}
ostream& operator<<(ostream &out, Fractions const&f){
    Fractions firstval("0/1");
    firstval.num = f.num;
    firstval.den = f.den;
    firstval.whole = firstval.num / firstval.den;
    firstval.num = firstval.num % firstval.den;
    if (firstval.whole == 0)
    {
        out<<firstval.num<<"/"<<firstval.den;
    }
    else if ((firstval.num == 0) &&(firstval.den == 1))
    {
        out<<firstval.whole;
    }
    else {
        out<<firstval.whole<<"-"<<firstval.num<<"/"<<firstval.den;
    }
    return out;
}
void Fractions::add(Fractions f2)
{
    num = (num * f2.den) + (f2.num *den);
    den= den * f2.den;
    reduce();  //don't forget to reduce!
}
void Fractions::sub(Fractions f2){
    num = (num * f2.den) - (f2.num *den);
    den= den * f2.den;
    reduce();  //don't forget to reduce!
}
void Fractions::mult(Fractions f2){
    num = num *f2.num;
    den= den * f2.den;
    reduce();  //don't forget to reduce!
}
void Fractions::div(Fractions f2){
    num = num *f2.den;
    den= den * f2.num;
    reduce();  //don't forget to reduce!
}
void Fractions::divint(int s1){
    den = den * s1;
    reduce();
}
void Fractions::multint(int s2){
    num = num * s2;
    reduce();
}
void Fractions::reduce()
{
    int divisor = gcd(num, den);
    num /= divisor;
    den /= divisor;
}
int gcd(int a, int b)
{
    if(b == 0)
        return a;
    else
        return gcd(b, a%b);
}
Fractions::Fractions(string fracvalue){
    string b = fracvalue;
    string wholenum = "";
    string nums = "";
    string dems= "";
    string placement;
    string::iterator dash = find(fracvalue.begin(),fracvalue.end(),'-');
    string::iterator slash = find(fracvalue.begin(), fracvalue.end(),'/');
    if ((slash != fracvalue.end()) && (dash != fracvalue.end()))
    {
        std::for_each(fracvalue.begin(),dash,[&wholenum](auto fracvalue){
            char b = fracvalue;
            wholenum.push_back(b);
        });
        std::for_each(dash+1,slash,[&nums](auto fracvalue){
            char b = fracvalue;
            nums.push_back(b);
        });
        std::for_each(slash+1,fracvalue.end(),[&dems](auto fracvalue){
            char b = fracvalue;
            dems.push_back(b);
        });
        whole = stoi(wholenum);
        num = stoi(nums);
        den = stoi(dems);
    }
    else if (slash != fracvalue.end())
    {
        std::for_each(fracvalue.begin(),slash,[&nums](auto fracvalue){
            char b = fracvalue;
            nums.push_back(b);
        });
        std::for_each(slash+1,fracvalue.end(),[&dems](auto fracvalue){
            char b = fracvalue;
            dems.push_back(b);
        });
        num = stoi(nums);
        den = stoi(dems);
    }
    else 
    {
        std::for_each(fracvalue.begin(),fracvalue.end(),[&wholenum](auto fracvalue){
            char b = fracvalue;
            wholenum.push_back(b);
        });
        whole = stoi(wholenum);
    }
    int newnum = whole *den;
    num = newnum + num;
    whole = 0;
}

#endif