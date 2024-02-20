
#include <iostream>
#include <stack>
#include <string>

void process_line(const std::string &line) {
  std::stack<char> stack{};
  for (auto i : line) {
    if (i == ')') {
      if (stack.empty() || stack.top() != '(') {
        std::cout << "no" << std::endl;
        return;
      }
      stack.pop();
    } else {
      stack.push(i);
    }
  }
  if (!stack.empty()) {
    std::cout << "no" << std::endl;
    return;
  }
  std::cout << "yes" << std::endl;
}

int main() {
  for (std::string line; std::getline(std::cin, line);) {
    process_line(line);
  }
}
