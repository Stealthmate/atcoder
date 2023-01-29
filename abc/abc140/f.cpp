#include<bits/stdc++.h>
using namespace std;


typedef long long ll;
typedef pair<int,int> P;
typedef vector<int> VI;

#define _rep(i,n) repi(i,0,n)
#define repi(i,a,b) for(int i=int(a);i<int(b);++i)
#define all(x) (x).begin(),(x).end()

int main() {
  int n;
  cin >> n;

  vector<long long> s(1 << n);
  for(int i=0;i<n;i++) {
    cin >> s[i];
  }

  sort(s.begin(), s.end());

  vector< long long > slimes = {s[0]};
  for(int i=0;i<n;i++) {
    vector<long long> newslimes;
    for(int j=slimes.size() - 1;j>0;j--) {

      newslimes.push_back(slimes[j]);
      if(s[s.size() - 1] < slimes[j]) {
        newslimes.push_back(s[s.size() - 1]);
        s.pop_back();
      }
      else {
        cout << "No" << endl;
        return 0;
      }
    }

    slimes = newslimes;
    sort(slimes.begin(), slimes.end());
  }

  cout << "Yes" << endl;
}
