#include<bits/stdc++.h>
using namespace std;

int main() {
  int a, b, x;
  cin >> a >> b >> x;
  bool ans = x <= (a + b) && x >= a;
  cout << (ans ? "YES" : "NO") << endl;
}
