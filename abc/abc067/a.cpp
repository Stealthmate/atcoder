#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  int ps[] = {a, b, a + b};
  bool ans = any_of(ps, ps + 3, [](int i)->bool { return i % 3 == 0; });
  cout << (ans ? "Possible" : "Impossible") << endl;
}
