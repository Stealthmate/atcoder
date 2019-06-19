#include<iostream>
using namespace std;

int main() {
  int a, d;

  cin >> a >> d;

  int p1 = (a + 1) * d;
  int p2 = a * (d + 1);
  cout << (p1 > p2 ? p1 : p2) << endl;
}
