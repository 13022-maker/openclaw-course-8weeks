#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    long long lines = 0;
    long long words = 0;
    long long bytes = 0;

    while (std::getline(cin, line)) {
        lines++;
        bytes += (long long)line.size() + 1; // +1 for \n
        bool in_word = false;
        for (unsigned char ch : line) {
            if (isspace(ch)) {
                if (in_word) in_word = false;
            } else {
                if (!in_word) {
                    in_word = true;
                    words++;
                }
            }
        }
    }

    cout << "lines=" << lines << "\n";
    cout << "words=" << words << "\n";
    cout << "bytes=" << bytes << "\n";
    return 0;
}
