#include <iostream>
using namespace std;

int main() {
  string S;
  cin >> S;

  int nAs = 0;
  long long total = 0;

  for (int i = 0; i < S.size() - 1; i++) {

    if(S[i] == 'A') nAs += 1;
    else if(S[i] == 'B' && S[i + 1] == 'C') { total += nAs; i += 1; }
    else nAs = 0;
  }

  cout << total << endl;
}
