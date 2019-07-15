#include<bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> ps(n, 0);
  int ans = 0;
  for(int i=0; i<n; i++) {
    cin >> ps[i];
    if(i > 1) {
      if((ps[i-2] > ps[i-1] && ps[i] < ps[i-1]) || (ps[i-2] < ps[i-1] && ps[i] > ps[i-1])) {
        ans += 1;
      }
    }
  }

  cout << ans << endl;
}
