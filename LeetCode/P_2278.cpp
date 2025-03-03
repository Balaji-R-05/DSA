// 2278. Percentage of Letter in String

class Solution
{
public:
    int percentageLetter(string s, char letter)
    {
        int count = 0;
        int n = s.length();
        for (int i = 0; i < n; i++)
        {
            if (s[i] == letter)
            {
                count++;
            }
        }
        return (int)(((double)count / n) * 100);
    }
};

// Time Complexity: O(n)
// Space Complexity: O(1)