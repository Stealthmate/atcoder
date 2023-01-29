#include<bits/stdc++.h>
#include <numeric>
using namespace std;

long long gcd(long long a, long long b) {
  if (a == 0) return b;
  return gcd(b % a, a);
}

int main() {
  long long a, b, c, d;
  cin >> a >> b >> c >> d;

  long long count_c = (b / c) - (a / c) + (a % c == 0);
  long long count_d = (b / d) - (a / d) + (a % d == 0);
  long long g = gcd(c, d);
  long long e = g * (c / g) * (d / g);
  long long count_cd = (b / e) - (a / e) + (a % e == 0);
  // cout << "C  " << count_c << endl;
  // cout << "D  " << count_d << endl;
  // cout << "CD " << count_cd << endl;

  cout << b - a - count_c - count_d + count_cd + 1 << endl;
}
