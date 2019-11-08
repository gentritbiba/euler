#pragma once

bool isPrime(double n) {
	if (fmod(n,2) == 0)return false;
	for (int i = 3; i <= sqrt(n); i++)
	{
		if (fmod(n,i) == 0)return false;
	}
	return true;
}
bool isPrime(int n) {
	if (n % 2 == 0)return false;
	for (int i = 3; i <= sqrt(n); i=i+2)
	{
		if (n%i == 0)return false;
	}
	return true;
}
bool isPandigital(string a) {
	for (int i = 0; i < a.length(); i++) {
		for (int j = i + 1; j < a.length(); j++) {
			if (a[i] == a[j])return false;
		}
	}
	return true;
}
double prob28() {
	
	double num = 1;
	long add = 2;
	int count = 0;
	double count2 = 0;
	double count3 = 0;
	double count4 = 0;
	for (int i = 1; true; i++) {
		num = num + add;
		count++;
		count2++;
		
		if (count % 4 == 0) {
			add = add + 2;
			count = 0;
			count4++;
		}
		if (isPrime(num)) { count3++; }
		if (count3 / count2 < 0.10)break; 
		cout << count3 << " " << count2 << " " << count3 / count2 << endl;


	}
	return count3;
}
bool isGoldbach(double m);
void oddComposite(int m) {
	bool isTrue = true;
	int count = 0;
	for (int i = 1; isTrue; i++) {
		for (int j = 1; j<=i; j++) {
			double s = 2 * (2 * i*j + (i + j)) + 1;
			if (isGoldbach(s)) {
				cout << s; isTrue = false;
			}
			count++; cout << i<<endl;
			if (count == m)isTrue=false;
		}
	}
}
bool isGoldbach(double m) {
	double a;
	for (int i = 3; i < m ; i = i + 2) {
		if (isPrime(i)) {
			a = (m - i)/2;
			if (fmod(sqrt(a),1) != 0.0) {
				return true;
			}
		}
	}
	return false;
}
