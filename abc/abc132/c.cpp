#include<bits/stdc++.h>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<int> ds(n, 0);
  for (int i=0;i<n;i++) {
    cin >> ds[i];
  }

  sort(ds.begin(), ds.end());

  cout << ds[ds.size() / 2] - ds[(ds.size() / 2) - 1] << endl;

}
