#include<bits/stdc++.h>
using namespace std;

int main() {
  string w;
  cin >> w;

  cout << regex_replace(w, regex("a|i|u|e|o"), "") << endl;
}
