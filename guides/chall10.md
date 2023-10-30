|[<<](/guides/chall9.md)|[START](/guides/main.md)|[0](/guides/chall0.md)|[1](/guides/chall1.md)|[2](/guides/chall2.md)|[3](/guides/chall3.md)|[4](/guides/chall4.md)|[5](/guides/chall5.md)|[6](/guides/chall6.md)|[7](/guides/chall7.md)|[8](/guides/chall8.md)|[9](/guides/chall9.md)|[10](/guides/chall10.md)|[END](/guides/end.md)|>>|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|

#### Piškotek / Cookie = 0to2KqU2E6c0JAbOQzuiMo27G2BysanpeXA0zp6j3RsA1rG3avTLtfEexGoCDRP6

# Problem 10 / Challenge 10
Offline

![Image](/guides/images/image10.png)

# Namigi / Hints
<details >
<summary>
    <i>Namig 1</i> 
</summary>
    ghidra
</details>
<details >
<summary>
    <i>Namig 2</i> 
</summary>
    kaj naredi prva zanka?
</details>
<details>
<summary>
    <i>Namig 3</i> 
</summary>
    Rešitev je skrita v seznamu, ki je potem obdelan z XOR-jem.
</details>
<br>

# Rešitev / Solution

<details>
<summary><b>
    Rešitev
</b></summary>
    __j4N3z$N0vaK=123!__
</details>
<details>
<summary><b>
    Opis
</b></summary>
orginalna koda:

```cpp
#include<stdio.h>

char flag[] = {
	0, 53, 94, 122, 125, 73, 94, 106, 126, 70, 23, 42, 118, 12, 3, 1, 18, 126, 0, 54
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
```
</details>

