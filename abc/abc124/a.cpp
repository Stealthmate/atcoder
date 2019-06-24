#include<bits/stdc++.h>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  if(a > b + 1) cout << a + a - 1;
  else if(b > a + 1) cout << b + b - 1;
  else cout << a + b;
  cout << endl;
}
