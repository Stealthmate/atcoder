#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  string s;
  cin >> s;
  cout << (s[s.size() - 1] == 'T' ? "YES" : "NO") << endl;
}
