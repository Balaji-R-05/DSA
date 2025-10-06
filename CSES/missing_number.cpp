#include <iostream>
#include <vector>

using namespace std;

int main() {
    long long n;
    cin >> n;
    vector<long long> arr(n - 1);

    for (long long i = 0; i < n - 1; i++) {
        cin >> arr[i];
    }

    long long total = n * (n + 1) / 2;
    long long sum = 0;
    for (long long num : arr) sum += num;

    cout << total - sum << endl;
    return 0;
}
