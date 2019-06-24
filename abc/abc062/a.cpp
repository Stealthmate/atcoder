#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  int x, y;
  cin >> x >> y;
  int seq1[] = {1, 3, 5, 7, 8, 10, 12};
  int seq2[] = {4, 6, 9, 11};

#define in(a, xs) (find(xs, xs + (sizeof xs / sizeof(int)), a) < (xs + sizeof xs / sizeof(int)))

  bool ans = (in(x, seq1) && in(y, seq1)) || (in(x, seq2) && in(y, seq2));
  cout << (ans ? "Yes" : "No") << endl;
}
