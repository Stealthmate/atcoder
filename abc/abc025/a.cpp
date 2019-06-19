#include<iostream>
using namespace std;

int main() {
  string a;
  int n;
  cin >> a >> n;

  cout << a[(n - 1) / 5] << a[(n - 1) % 5] << endl;
}
