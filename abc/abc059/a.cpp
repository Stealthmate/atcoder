#include<iostream>
#include<algorithm>
using namespace std;

int main() {
  string s1, s2, s3;
  cin >> s1 >> s2 >> s3;
  char d = 'a' - 'A';
  cout << (char) (s1[0] - d) << (char) (s2[0] - d) << (char)(s3[0] - d) << endl;
}
