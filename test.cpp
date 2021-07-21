/* g++ test.cpp -fdump-tree-cfg */
#include <assert.h>

class A {
public:
	 int c;
};

class B {
public:
	A b[10];
};

B d(int i, int j, int k, int l)
{

}

int main()
{
	B a;
	int r1 = a.b[1].c;
	int r2;
	int array[10];
//	int array2[10+101];

	if (r1 > 0)
		r2 = d(1+r1,1,2,3).b[2+r1].c;

	r2 += 10 * r1;
	array[1] += 1;
	
	r1 = ~(-r1);
	r2 = -r1;
	r1 = -(r1 + r2);
	assert(r2 > 0);

	if (r2 > 3)
		r2 = 1;
	else
		r2 = 2;

	return -(r1 + -r2);
}
