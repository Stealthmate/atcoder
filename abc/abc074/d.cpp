#include<bits/stdc++.h>
using namespace std;

vector< vector<int> > warshallFloyd(vector< vector<int> > dist) {
  int n = dist.size();
  for(int k=0;k<n;k++) {
    for(int i=0;i<n;i++) {
      for(int j=0;j<n;j++) {
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }

  return dist;
}

int main() {
  long long n;
  cin >> n;

  vector< vector<int> > a(n, vector<int>(n));
  for(int i=0;i<n;i++) {
    for(int j=0;j<n;j++) {
      cin >> a[i][j];
    }
  }

  auto dist = warshallFloyd(a);
  for(int i=0;i<n;i++) {
    for(int j=0;j<n;j++) {
      if(a[i][j] != dist[i][j]) {
        cout << -1 << endl;
        return 0;
      }
    }
  }

  long long ans = 0;
  for(int i=0;i<n;i++) {
    for(int j=0;j<i;j++) {
      int needed = 1;
      for(int k=0;k<n;k++) {
        if(a[i][k] + a[k][j] == a[i][j] && i != k and j != k) {
          needed = 0;
          break;
        }
      }
      ans += needed * a[i][j];
    }
  }

  cout << ans << endl;
}
