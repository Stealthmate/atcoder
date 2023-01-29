#include<bits/stdc++.h>
using namespace std;

int main() {
  long long s;
  cin >> s;

  long long LIM = 1000000000;
  long long a1 = -1, a2 = -1;
  for(long long i = 2; i <= LIM; i++) {
    if(s % i == 0) {
      cout << "ANSWER" << endl;
      a1 = i;
      a2 = s / i;
      break;
    }
  }

  cout << "0 " << a1 << " " << a2 << " 0 0 0" << endl;
}
