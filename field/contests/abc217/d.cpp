#include <bits/stdc++.h>
using namespace std;

int main()
{
    int L, Q;
    int c, x;

    cin >> L >> Q;
    vector<int> sep = {0, L};

    for (int i = 0; i < Q; i++)
    {
        cin >> c >> x;

        auto iter = lower_bound(sep.begin(), sep.end(), x);
        unsigned int idx = distance(sep.begin(), iter);

        if (c == 1)
        {
            sep.insert(iter, x);
        }
        else
        {
            cout << sep[idx] - sep[idx - 1] << endl;
        }
    }
}
