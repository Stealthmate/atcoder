#include<iostream>
#include<cmath>
using namespace std;

int ndigs(long long n) {
  int nd = 0;
  while(n > 0) {
    nd += 1;
    n /= 10;
  }

  return nd;
}

int main() {
  long long L, A, B, M;
  cin >> L >> A >> B >> M;

  long long rem = 0;
  long long remA = A % M;
  long long remB = B % M;
  long long si, nd, p, a;
  for(long long i = 0; i < L; i++) {
    si = (remA + (i * rxemB)) % M;
    nd = ndigs(A + i*B);
    p = pow(10, nd);
    a = (rem * (p % M)) % M;
    rem = (a + si) % M;
  }

  cout << rem;
}
