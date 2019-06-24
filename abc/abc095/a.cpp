#include<bits/stdc++.h>
using namespace std;

int main() {
  string s;
  cin >> s;
  cout << ((s[0] == 'o') + (s[1] == 'o') + (s[2] == 'o')) * 100 + 700 << endl;
}
