#include <iostream>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;

  int f, s;

  f = (a == 5) + (b == 5) + (c == 5);
  s = (a == 7) + (b == 7) + (c == 7);

  if(f == 2 && s == 1) {
    cout << "YES";
  }
  else
    cout << "NO";
  cout << endl;
}
