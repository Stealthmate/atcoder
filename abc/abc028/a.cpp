#include<iostream>
using namespace std;

int main() {
  int n;
  cin >> n;
  if(n <= 59) cout << "Bad";
  else if(n <= 89) cout << "Good";
  else if(n <= 99) cout << "Great";
  else cout << "Perfect";

  cout << endl;
}
