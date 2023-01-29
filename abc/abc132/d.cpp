#include<bits/stdc++.h>
using namespace std;

unsigned long long C(unsigned n, unsigned k) {
    if (n == k || k == 0) {
        return 1; // There's exactly one way to select n or 0 objects out of n
    }
    return C(n - 1, k - 1) * n / k;
}

int main() {
  int n, k;
  cin >> n >> k;

  for(int i=1;i<=k;i++) {
    cout << C(n - k + 1, i) << endl;
  }
}
