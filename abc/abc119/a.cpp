#include<bits/stdc++.h>
using namespace std;

int main() {
  int y, m, d;
  scanf("2019/%d/%d", &m, &d);

  bool ans = m <= 4;
  cout << (ans ? "Heisei" : "TBD") << endl;
}
