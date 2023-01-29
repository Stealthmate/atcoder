#include<bits/stdc++.h>
using namespace std;

int main() {
  int N, K;
  cin >> N >> K;

  int possible = false;
  int s, l;
  int all;
  for(s=1; s < K; s++) {
    l = N - 1 - s;
    all = (s * (s - 1) / 2) + l;
    if(all == K) {
      possible = 1;
      break;
    }
    if(all + 2 == K && l > 1) {
      possible = 2;
      break;
    }

  }

  if(possible == 0) {
    cout << -1 << endl;;
    return 0;
  }

  int m = s + l;
  if(possible == 2) m += 1;

  cout << m << endl;

  for(int i=2; i <= s + 1; i++) {
    cout << 1 << " " << i << endl;
  }
  for(int i=s + 1; i < N; i++) {
    cout << i << " " << i + 1 << endl;
  }
  if(possible == 2) {
    cout << N << " " << 1 << endl;
  }
}
