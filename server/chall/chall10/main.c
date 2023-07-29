#include<stdio.h>

char flag[] = {
	0,
	53,
	94,
	122,
	125,
	73,
	94,
	106,
	126,
	70,
	23,
	42,
	118,
	12,
	3,
	1,
	18,
	126,
	0,
	54
};

int main()
{
	char input[21];
	printf("Vpisi geslo: ");
	fgets(input, 21, stdin);

	char prev = 0x69;
	for (int i = 19; i >= 0; i--)
	{
		char tmp = input[i];
		input[i] ^= prev;
		prev = tmp;
	}

	for (int i = 0; i < 20; i++)
	{
		if (input[i] != flag[i])
		{
			printf("Napacno geslo :(\n");
			return 1;
		}
	}

	printf("Bravo!\n");
	return 0;
}
