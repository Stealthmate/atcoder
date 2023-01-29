#include <iostream>
using namespace std;

int main() {

  int N, X;
  cin >> N >> X;
  int d = 0;
  int ans = 1;
  for(int i=0;i<N;i++) {
    int y;
    cin >> y;
    d += y;
    if(d <= X) ans++;
  }

  cout << ans << endl;
}
