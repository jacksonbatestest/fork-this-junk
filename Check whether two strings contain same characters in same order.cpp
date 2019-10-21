// C++ implementation of the approach 
#include <iostream> 
using namespace std; 

string getString(char x) 
{ 
	// string class has a constructor 
	// that allows us to specify size of 
	// string as first parameter and character 
	// to be filled in given size as second 
	// parameter. 
	string s(1, x); 

	return s; 
} 

// Function that returns true if 
// the given strings contain same 
// characters in same order 
bool solve(string s1, string s2) 
{ 
	// Get the first character of both strings 
	string a = getString(s1[0]), b = getString(s2[0]); 

	// Now if there are adjacent similar character 
	// remove that character from s1 
	for (int i = 1; i < s1.length(); i++) 
		if (s1[i] != s1[i - 1]) { 
			a += getString(s1[i]); 
		} 

	// Now if there are adjacent similar character 
	// remove that character from s2 
	for (int i = 1; i < s2.length(); i++) 
		if (s2[i] != s2[i - 1]) { 
			b += getString(s2[i]); 
		} 

	// If both the strings are equal 
	// then return true 
	if (a == b) 
		return true; 

	return false; 
} 

// Driver code 
int main() 
{ 
	string s1 = "Geeks", s2 = "Geks"; 

	if (solve(s1, s2)) 
		cout << "Yes"; 
	else
		cout << "No"; 

	return 0; 
} 
