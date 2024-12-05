#include <bits/stdc++.h>
using namespace std;

using ll = int64_t;
typedef long double ld;
#define endl "\n"
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define pb push_back

void local(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
}

void printArr(vector<int> &arr){
    for (int i = 0; i < arr.size(); ++i)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void printSet(set<int> a){
    for(auto n : a){
        cout << n << " ";
    }
    cout << endl;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	local();

	std::vector<string> lines;
	string s;
	while(cin >> s){
		lines.pb(s);
	}

	unordered_map<int, set<int>> rules;
	int line_break;
	for (int i = 0; i < lines.size(); ++i)
	{
		if(lines[i][2] != '|'){
			line_break = i;
			break;
		}
		int a, b;
		a = (lines[i][0] - '0')*10 + lines[i][1] - '0';
		b = (lines[i][3] - '0')*10 + lines[i][4] - '0';
		
        if(rules.count(a) > 0){
            rules[a].insert(b);
        }
        else{
            rules.emplace(a, set<int>());
            rules[a].insert(b);
        }
	}

    vector<vector<int>> updates;

    for (int i = line_break; i < lines.size(); ++i)
    {
        vector<int> update;
        for (int j = 0; j < lines[i].size(); j+=3)
        {
            int a = (lines[i][j] - '0')*10 + lines[i][j+1] - '0';
            update.pb(a);
        }
        updates.pb(update);
    }

    //Bubble sort - fine since our arrays are small enough
    auto sort_arr = [&] (vector<int> & arr){
        for (int i = 0; i < arr.size(); ++i)
        {
            int swaps = 0;
            for (int j = 0; j < arr.size()-1; ++j)
            {
                //If arr[j+1] is not in the hashmap "rules", empty
                //set is returned. So program still works 
                const set<int> & after_set_j_n = rules[arr[j+1]];

                if (after_set_j_n.count(arr[j]) > 0){
                    //j should come after j+1
                    std::swap(arr[j+1], arr[j]);
                    swaps++;
                    continue;
                }
            }
            if(swaps == 0){
                if(i == 0){
                    return false; //array already sorted
                }
                else return true;
            }
        }
        return true; //array was not sorted
    };

    ll sum = 0;
    for (int i = 0; i < updates.size(); ++i)
    {
        bool flag = sort_arr(updates[i]);
        if(flag){
            int j = updates[i].size() / 2;
            sum += updates[i][j]
        }
    }
    cout << sum << endl;


	return 0;
}
