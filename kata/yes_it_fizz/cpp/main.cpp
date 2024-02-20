#include <cstdio>
#include <iostream>

void fizzbuzz(unsigned i) {
  auto mod_3 = i % 3;
  auto mod_5 = i % 5;
  if (mod_3 == 0 && mod_5 == 0) {
    std::cout << "FizzBuzz" << std::endl;
  } else if (mod_3 == 0) {
    std::cout << "Fizz" << std::endl;
  } else if (mod_5 == 0) {
    std::cout << "Buzz" << std::endl;
  } else {
    std::cout << i << std::endl;
  }
}

int main() {
  unsigned n, m;
  scanf("%d %d", &n, &m);
  for (auto i = n; i <= m; ++i) {
    fizzbuzz(i);
  }
}
