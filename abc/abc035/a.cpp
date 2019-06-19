#include<iostream>
using namespace std;

int main() {
  double w, h;
  cin >> w >> h;
  double r1 = 4.0 / 3.0, r2 = 16.0 / 9.0;
  cout << (w / h == r1 ? "4:3" : "16:9") << endl;
}
