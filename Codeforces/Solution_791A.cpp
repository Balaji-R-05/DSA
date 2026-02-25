#include <iostream>
 
int main() 
{
  int a, b;
  std::cin >> a >> b;
  int years = 0;
  while (a <= b) {
    a *= 3;
    b *= 2;
    years += 1;
  }
  std::cout << years;
  return 0;
}

// Time complexity: O(log(b/a))
// Space complexity: O(1)