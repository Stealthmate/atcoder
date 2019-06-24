#include<bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c, d;
  cin >> a >> b >> c >> d;

  int x = a + b, y = c + d;

  if(x == y) cout << "Balanced";
  else if(x < y) cout << "Right";
  else cout << "Left";

  cout << endl;
}
