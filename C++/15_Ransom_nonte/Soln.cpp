#include <vector>
#include <unordered_map>

class Solution {
public:
    bool canConstruct(std::string ransomNote, std::string magazine) {
        std::unordered_map<char, int> rc;
        std::unordered_map<char, int> mc;

        // Count characters in ransomNote
        for (char c : ransomNote) {
            rc[c]++;
        }

        // Count characters in magazine
        for (char c : magazine) {
            mc[c]++;
        }

        // Check if the characters in ransomNote can be constructed from magazine
        for (const auto& entry : rc) {
            char character = entry.first;
            int count = entry.second;
            
            if (mc.find(character) == mc.end() || mc[character] < count) {
                return false;
            }
        }

        return true;
    }
};