#include<bits/stdc++.h>
using namespace std;

long long MOD = 1000000007ll;

int main() {
  long long n, m;
  cin >> n >> m;
  vector<int> s(n), t(m);
  for(int i=0;i<n;i++) cin >> s[i];
  for(int i=0;i<m;i++) cin >> t[i];

  vector< vector<long long> > ans(n + 1, vector<long long>(m + 1, 0ll));
  for(int i=0;i<n;i++) {
    for(int j=0;j<m;j++) {
      ans[i][j] = 0;
    }
  }

  for(int i=1;i<n+1;i++) {
    for(int j=1;j<m+1;j++) {
      ans[i][j] = ans[i-1][j] + ans[i][j-1] - ans[i-1][j-1] + MOD;

      if(s[i-1] == t[j-1]) {
        ans[i][j] += ans[i-1][j-1] + 1;
      }
      ans[i][j] %= MOD;

    }
  }

  cout << (ans[n][m] + 1) % MOD << endl;
}
