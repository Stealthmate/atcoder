#include<iostream>
using namespace std;

int main() {
  double a, b, c, d;
  cin >> a >> b >> c >> d;

  if((b / a) > (d / c)) cout << "TAKAHASHI";
  else if((b / a) < (d / c)) cout << "AOKI";
  else cout << "DRAW";
  cout << endl;
}
