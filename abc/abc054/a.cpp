#include<iostream>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;
  a = (a == 1) ? 14 : a;
  b = (b == 1) ? 14 : b;

  if(a == b) cout << "Draw";
  else if(a > b) cout << "Alice";
  else cout << "Bob";
  cout << endl;
}
