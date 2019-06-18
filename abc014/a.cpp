#include<iostream>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  int r = a % b;
  cout << (r == 0 ? 0 : b - r) << endl;
}
