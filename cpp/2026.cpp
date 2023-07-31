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
    // ���̸� �����ϴ� �� Ȯ���Ѵ�.
    if (picked.size() == k + 1)
    {
        // ���ǿ� �����ϴ� �� Ȯ���Ѵ�.
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
    // �Է�
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

    // k�� 1�� ���, ����� ���� �� ����
    if (k == 1)
    {
        cout << 1;
        return 0;
    }

    // 0���� ��� ���� ����Ǿ� �ִ�
    for (int i = 1; i <= n; i++)
        relation[0][i] = true;
    // ��Ͽ� ���� ���� �� �ʱ�ȭ
    vector<int> v;
    v.push_back(0);
    // ���� Ȯ��
    if (!permutation(v))
        cout << -1;
}