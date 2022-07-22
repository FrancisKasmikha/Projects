#ifndef RECIPE_H
#define RECIPE_H

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
#include "fractions.h"

class Recipe{
    public:
    string recipe = "";
    int servings = 0;
    string SetInstruction = "";
    map<string,Fractions> ingredients;
    map<string,vector<string>> ingredientss;
    map<string,string> units;
    map<string,Fractions> Pantry;
    map<string,string> Pantryunits;
    vector<string> ordered;
    vector<string> setin;
    stringstream interstream;

    Recipe()= default;
    Recipe(string recipe,int servings);

    void AddIngredient(string s1);
    void SetInstructions(string s1);
    string IngredientInOneServing(string s1);
    void ChangeServings(int ss);
    friend std::ostream & operator<<(std::ostream &, Recipe const &);
};

const std::string WHITESPACE = " \n\r\t\f\v";

std::string ltrim(const std::string &s)
{
	size_t start = s.find_first_not_of(WHITESPACE);
	return (start == std::string::npos) ? "" : s.substr(start);
}

std::string rtrim(const std::string &s)
{
	size_t end = s.find_last_not_of(WHITESPACE);
	return (end == std::string::npos) ? "" : s.substr(0, end + 1);
}

std::string trim(const std::string &s) {
	return rtrim(ltrim(s));
}

Recipe::Recipe(string recipes,int servingss){
    recipe = recipes;
    servings = servingss;
}
void Recipe::AddIngredient(string s1){
    stringstream ss(s1);
    int count = 1;
    int counts =1;
    string fraction;
    string unit;
    string foodname;
    string foodword;
    string foodwords;
    stringstream sss;
    while (count!=4)
    {
        string thirdval;
        if (count ==1)
        {
            ss>>fraction;
        }
        if (count ==2)
        {
            ss>>unit;
        }
        if (count >2)
        {
        // ss>>foodword;
        std::getline(ss,foodword);
        foodwords = trim(foodword);
        if (foodword.empty())
        {
            break;
        }
        if (counts == 50)
        {
            foodname = foodword;
        }
        if (counts>50)
        {
            foodname = foodname + " ";
        }
        foodword = "";
        }
        count ++;
    }
    Fractions f1(fraction);
    ingredients.insert({foodwords,f1});
    units.insert({foodwords,unit});
    ingredientss.insert({foodwords,{fraction,unit}});
    ordered.push_back(foodwords);
}
void Recipe::SetInstructions(string s1){
    stringstream ss(s1);
    string newwords;
    while (std::getline(ss,newwords, '\n'))
    {
        if (newwords.empty())
        {
            continue;
        }
        string finalwords = trim(newwords);
        setin.push_back(finalwords);
    }
}
string Recipe::IngredientInOneServing(string s1){
    auto it = ingredientss.find(s1);
    if (it != ingredientss.end()){
    string fraction = ingredientss.at(s1).at(0);
    string unit = ingredientss.at(s1).at(1);
    Fractions frac(fraction);
    frac.divint(servings);
    string final = frac.fractostr();
    string finalss = final +" "+ unit+" " + s1;
    return finalss;
    }
    else
    {
        throw std::invalid_argument("");
    }
    
    
    // string fraction = ingredientss.at(s1).at(0);
    // string unit = ingredientss.at(s1).at(1);
    // Fractions frac(fraction);
    // frac.divint(servings);
    // string final = frac.fractostr();
    // string finalss = final +" "+ unit+" " + s1;
    // return finalss;
}
void Recipe::ChangeServings(int ss){
    for(auto var : ordered)
    {
        auto fraction = ingredientss.at(var).at(0);
        Fractions simpl(fraction);
        simpl.divint(servings);
        simpl.multint(ss);
        string reduced = simpl.fractostr();
        ingredientss.at(var).at(0) = reduced;
    }
    servings = ss;
}


std::ostream & operator<<(std::ostream & out, Recipe const & Re){
    stringstream ssss;
    ssss<<"Recipe for: "<<Re.recipe<<"\n";
    ssss<<"Serves "<<Re.servings<<"\n";
    ssss<<"Ingredients:"<<"\n";
    int count = 0;
    for(auto var : Re.ordered)
    {
        auto fraction = Re.ingredientss.at(var).at(0);
        Fractions simpl(fraction);
        string reduced = simpl.fractostr();
        auto unit = Re.ingredientss.at(var).at(1);
        ssss<<reduced<<" "<<unit<< " "<<var<<"\n";
    }
    // for(auto var : Re.ingredientss)
    // {
    //     string name = var.first;
    //     vector<string> vects;
    //     vects = var.second;
    //     string fraction = var.second.at(0);
    //     string unit= var.second.at(1);
    //     ssss<<fraction<<" "<<unit<< " "<<name<<"\n";
    // }
    ssss<<"\n"<<"Instructions:"<<"\n";
    for(auto var : Re.setin)
    {
        ssss<<var<<"\n";
    }
    
    ssss<<"\n";
    string final= ssss.str();
    out<<final;
    return out;
}

#endif