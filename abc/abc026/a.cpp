#include<iostream>
using namespace std;

int main() {
  int a;
  cin >> a;
  int ans = -1;
  for(int i=1; i * 2 <= a; i++) {
    if(ans < i * (a - i)) ans = i * (a - i);
  }

  cout << ans << endl;
}
