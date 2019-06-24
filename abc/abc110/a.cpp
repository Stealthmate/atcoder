#include<bits/stdc++.h>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;

  int m = max({a, b, c});
  int x = 0;
  if(m == a) x = b + c;
  else if(m == b) x = a + c;
  else x = a + b;

  cout << m * 10 + x << endl;
}
