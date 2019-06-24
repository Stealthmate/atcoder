#include<bits/stdc++.h>
using namespace std;

int main() {
  int a1, a2, a3;
  cin >> a1 >> a2 >> a3;

  int as[3] = {a1, a2, a3};
  sort(as, as + 3);

  cout << as[2] - as[0] << endl;
}
