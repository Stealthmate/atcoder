#include<bits/stdc++.h>
using namespace std;

int main() {
  string s1, s2;
  cin >> s1 >> s2;
  reverse(s2.begin(), s2.end());
  bool ans = s1 == s2;
  cout << (ans ? "YES" : "NO") << endl;
}