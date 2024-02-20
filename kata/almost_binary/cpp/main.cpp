
#include <cmath>
#include <iostream>
#include <string>

int main() {
  for (std::string line; std::getline(std::cin, line);) {
    auto index = line.length() - 1;
    auto count = 0;
    for (auto i : line) {
      if (i == '#') {
        count += std::pow(2, index);
      }
      index -= 1;
    }
    std::cout << count << std::endl;
  }
}
