#include<bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<long long> a;
  for(int i=0;i<n;i++) {
    long long x;
    cin >> x;
    a.push_back(x);
  }

  bool ans = false;
  long long s = a[0];
  long long x = s;
  long long y = a[1];
  a.erase(a.begin());
  a.erase(a.begin());
  while(a.size() > 0) {
    long long r = x ^ y;
    auto xx = find(a.begin(), a.end(), r);
    if(xx != a.end()) {
      a.erase(xx);
      x = y;
      y = r;
    } else {
      break;
    }
  }

  if(a.size() == 0) {
    ans = x ^ y == s;
  }

  if(ans) {
    cout << "Yes";
  }
  else {
    cout << "No";
  }
  cout << endl;
}
