#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  int x, a, b;
  cin >> x >> a >> b;

  if(b - a <= 0) cout << "delicious";
  else if(b - a <= x) cout << "safe";
  else cout << "dangerous";
  cout << endl;
}
