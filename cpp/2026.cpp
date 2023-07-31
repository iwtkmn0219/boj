#include <iostream>
#include <vector>
#define max(a, b) a > b ? a : b
#define min(a, b) a < b ? a : b

using namespace std;

int k, n, f;
bool relation[901][901];

void show_vector(vector<int> &v)
{
    for (int i = 1; i < v.size(); i++)
        cout << v[i] << "\n";
}

bool correct(vector<int> &v)
{
    for (int i = 1; i < v.size() - 2; i++)
        for (int j = i + 2; j < v.size(); j++)
            if (!relation[v[i]][v[j]])
                return false;
    return true;
}

bool permutation(vector<int> &picked)
{
    // 길이를 충족하는 지 확인한다.
    if (picked.size() == k + 1)
    {
        // 조건에 성립하는 지 확인한다.
        if (correct(picked))
        {
            show_vector(picked);
            return true;
        }
        return false;
    }
    int current = picked.back();
    for (int next = 0; next < n + 1; next++)
    {
        if (relation[current][next])
        {
            picked.push_back(next);
            bool condition = permutation(picked);
            if (condition)
                return true;
            picked.pop_back();
        }
    }
    return false;
}

int main()
{
    // 입력
    cin >> k >> n >> f;
    for (int i = 0; i < f; i++)
    {
        int x, y;
        cin >> x >> y;
        if (y < x)
        {
            swap(x, y);
        }
        relation[x][y] = true;
    }

    // k가 1인 경우, 경우의 수는 한 가지
    if (k == 1)
    {
        cout << 1;
        return 0;
    }

    // 0에서 모든 곳은 연결되어 있다
    for (int i = 1; i <= n; i++)
        relation[0][i] = true;
    // 기록용 벡터 생성 및 초기화
    vector<int> v;
    v.push_back(0);
    // 순열 확인
    if (!permutation(v))
        cout << -1;
}