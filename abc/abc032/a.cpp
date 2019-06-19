#include<iostream>
using namespace std;

int main() {
  int a, b, n;
  cin >> a >> b >> n;

  int lcm = 0;
  while(n % a != 0 || n % b != 0) n += 1;

  cout << n << endl;

}
