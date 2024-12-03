#include <bits/stdc++.h>

void local(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#endif
}

long long numOccur(std::vector<int> & list, int num){
	long long ans = 0;
	for (int i = 0; i < list.size(); ++i)
	{
		if(list[i] == num) ans++;
	}
	return ans;
}

int main(){
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	local();

	std::vector<int> left, right;
	int x, y;
	while(std::cin >> x >> y){
		left.push_back(x);
		right.push_back(y);
	}

	std::sort(left.begin(), left.end());
	std::sort(right.begin(), right.end());


	long long max = std::numeric_limits<long long int>::max();

	//For part 1:
	// long long sum = 0
	// for (int i = 0; i < left.size(); ++i)
	// {
	// 	int diff = abs(right[i] - left[i])
	// 	assert(sum <= max - diff);
	// 	sum += diff
	// }


	//For part 2:
	long long similarity = 0;
	for (int i = 0; i < left.size(); ++i)
	{
		long long score = numOccur(right, left[i]) * left[i];
		assert(similarity <= max - score);
		
		similarity += score;
	}

	std::cout << similarity << std::endl;


	return 0;
}
