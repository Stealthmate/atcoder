#include<bits/stdc++.h>
using namespace std;

int main() {
  double m;
  cin >> m;

  cout << fixed << setprecision(0) << setfill('0') << setw(2);
  if(m < 100) cout << 0;
  else if(m <= 5000) cout << m / 100;
  else if(m >= 6000 && m <= 30000) cout << (m / 1000) + 50;
  else if(m >= 35000 && m <= 70000) cout << ((m / 1000) - 30) / 5 + 80;
  else cout << 89;
  cout << endl;
}
