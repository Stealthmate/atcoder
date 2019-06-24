#include<bits/stdc++.h>
using namespace std;

int main() {
  int a[5], k;
  for(int i=0;i<5;i++) {
    cin >> a[i];
  }
  cin >> k;
  bool ans = a[4] - a[0] <= k;
  cout << (ans ? "Yay!" : ":(") << endl;
}
