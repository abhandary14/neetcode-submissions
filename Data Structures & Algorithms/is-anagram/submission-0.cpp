class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length())
            return false;

        unordered_map<char, int> mp_s;
        unordered_map<char, int> mp_t;
        for(int i=0; i<s.size();i++)
            mp_s[s[i]]++;
        for(int i=0; i<t.size();i++)
            mp_t[t[i]]++;

        return mp_s == mp_t;
    }
};
