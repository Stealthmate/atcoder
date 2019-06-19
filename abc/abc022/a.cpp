#include<iostream>
using namespace std;

int main() {
  int n, s, t, w;
  cin >> n >> s >> t >> w;

  int ans = w >= s && w <= t;
  for(int i=0; i < n - 1; i++) {
    int d;
    cin >> d;
    w += d;
    ans += w >= s && w <= t;
  }

  cout << ans << endl;
}
