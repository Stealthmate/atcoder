#include<bits/stdc++.h>
using namespace std;

int main() {
  string s, t;
  cin >> s >> t;

  char CHARS[] = "atcoder@";
  auto END = (CHARS + sizeof CHARS / sizeof(char));

  bool ans = true;
  for(int i=0;i<s.size();i++) {
    if(s[i] != t[i]) {
      if(find(CHARS, END, s[i]) == END || find(CHARS, END, t[i]) == END) {
        ans = false;
        break;
      }
      if(s[i] != '@' && t[i] != '@') {
          ans = false;
          break;
      }
    }
  }

  cout << (ans ? "You can win" : "You will lose") << endl;
}
