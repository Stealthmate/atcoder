#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  string n;
  cin >> n;
  bool same = all_of(n.cbegin(), n.cend(), [n](char x)->bool { return x == n[0]; });
  cout << (same ? "SAME" : "DIFFERENT") << endl;
}
