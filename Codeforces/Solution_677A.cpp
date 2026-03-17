#include<iostream>
#include<string>
 
int main() {
  int N, H, curr=0;
  std::cin >> N >> H;
  int res = 0;
  for(int i=0; i<N; i++) {
    std::cin >> curr;
    if (curr > H) {
      res += 2;
    } else {
      res++;
    }
  }
  std::cout << res;
  return 0;
}

// Time Complexity: O(N)
// Space Complexity: O(1)