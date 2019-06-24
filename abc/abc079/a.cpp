#include<bits/stdc++.h>
using namespace std;

int main() {
  string n;
  cin >> n;
  bool ans = (n[0] == n[1] && n[1] == n[2]) || (n[1] == n[2] && n[2] == n[3]);
  cout << (ans ? "Yes" : "No") << endl;
}
