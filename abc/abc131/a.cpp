#include<bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  bool ans = (s[0] == s[1]) || (s[1] == s[2]) || (s[2] == s[3]);
  cout << (ans ? "Bad" : "Good") << endl;
}
