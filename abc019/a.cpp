#include<iostream>
using namespace std;

int main() {
  int a, b, c;
  cin >> a >> b >> c;

#define midIsMedian(p, x, q) ((p <= x && x <= q) || (q <= x && x <= p))

  if(midIsMedian(a, b, c)) cout << b;
  else if(midIsMedian(b, a, c)) cout << a;
  else cout << c;

  cout << endl;
}
