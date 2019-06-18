#include<iostream>
using namespace std;

int main() {
  int N, K, X, Y;
  cin >> N >> K >> X >> Y;

  int f = X * (N > K ? K : N);
  int s = Y * (N > K ? (N - K) : 0);

  cout << f + s << endl;
}
