#include <iostream>
#include <tuple>
#include <unordered_map>
using namespace std;

typedef long long Result;
typedef pair<long long, long long> Argument;

typedef Result (*Operation)(Argument);

Result addition(Argument arg) {
  return arg.first + arg.second;
}

Result subtraction(Argument arg) {
  return arg.first - arg.second;
}

unordered_map<char, Operation> OPS =
  {
   { '+', addition },
   { '-', subtraction }
  };


int main() {
  char op;
  long long a, b;

  cin >> a >> op >> b;

  Argument arg = {a, b};
  Result r;

  auto opi = OPS.find(op);
  if(opi == OPS.end()) {
    cout << "Bad op" << endl;
  }
  else {
    cout << opi->second(arg) << endl;;
  }
}
