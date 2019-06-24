#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  string a, b, c;
  cin >> a >> b >> c;

  bool ans = a[a.size() - 1] == b[0] && b[b.size() - 1] == c[0];
  cout << (ans ? "YES" : "NO") << endl;
}
