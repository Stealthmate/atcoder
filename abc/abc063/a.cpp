#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  if(a + b >= 10) cout << "error";
  else cout << a + b;
  cout << endl;
}
