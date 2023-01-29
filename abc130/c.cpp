#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main() {
  long long W, H, x, y;

  cin >> W >> H >> x >> y;

  double S = W * H / 2.0;

  cout << fixed << showpoint;
  cout << setprecision(10) << S << " " << ((x * 2 == W) && (y * 2 == H) ? '1' : '0') << endl;
}
