#include <iostream>
#include <vector>
using namespace std;

struct Node {
  int good, left, up, right, down;
};

vector< vector<Node> > nodes;

int ns(Node n) {
  return n.left + n.right + n.up + n.down + n.good;
}

int main() {
  int h, w;
  cin >> h >> w;
  string s;
  int lastLeft = 0;
  vector<int> lastUp = vector<int>(w, 0);

  for(int i = 0; i < h; i++) {
    cin >> s;
    nodes.push_back(vector<Node>());
    lastLeft = 0;

    for(int j = 0; j < w; j++) {
      char c = s[j];
      Node n;
      n.good = c == '.' ? 1 : 0;
      n.left = 0;
      n.up = 0;
      n.right = w - j - 1;
      n.down = h - i - 1;
      if(n.good == 1) {
        if(j > 0) {
          Node l = nodes[i][j - 1];
          n.left = l.left + l.good;
        }
        if(i > 0) {
          Node u = nodes[i-1][j];
          n.up = u.up + u.good;
        }
      }
      else {
        n.right = 0;
        n.down = 0;
        for(int k = lastLeft; k < j; k++) {
          nodes[i][k].right = j - k - 1;
        }
        for(int k = lastUp[j]; k < i; k++) {
          nodes[k][j].down = i - k - 1;
        }
        lastLeft = j + 1;
        lastUp[j] = i + 1;
      }

      nodes[i].push_back(n);
    }
  }

  int mx = -1;
  for(int i = 0; i < h; i++) {
    for(int j = 0; j < w; j++) {
      int nss = ns(nodes[i][j]);
      // cout << i << " " << j << " " << nss << endl;
      // cout << nodes[i][j].left << " " << nodes[i][j].right << " " << nodes[i][j].up << endl;
      if(nss > mx) {
        mx = ns(nodes[i][j]);
      }
    }
  }

  cout << mx << endl;
}
