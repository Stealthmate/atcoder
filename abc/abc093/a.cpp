#include<bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  bool ans = (s.find('a') != string::npos) + (s.find('b')  != string::npos) + (s.find('c') != string::npos) == 3;
  cout << (ans ? "Yes" : "No") << endl;
}
