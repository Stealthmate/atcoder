#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  string s;
  cin >> s;
  bool ans = s.substr(0, s.size() / 2) == s.substr(s.size() / 2 + 1);
  cout << (ans ? "Yes" : "No") << endl;
}
