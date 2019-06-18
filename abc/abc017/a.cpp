#include<iostream>
using namespace std;

int main() {
  int score = 0;
  for(int i = 0; i < 3; i++) {
    int s, e;
    cin >> s >> e;
    score += s * e;
  }
  cout << score / 10 << endl;
}
