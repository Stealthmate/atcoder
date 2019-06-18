#include<iostream>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;

  bool possible = (a + b == c) || (a + c == b) || (b + c == a);
  cout << (possible ? "Yes" : "No") << endl;
}
