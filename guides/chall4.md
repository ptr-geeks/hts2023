|[<<](/guides/chall3.md)|[START](/guides/main.md)|[0](/guides/chall0.md)|[1](/guides/chall1.md)|[2](/guides/chall2.md)|[3](/guides/chall3.md)|[4](/guides/chall4.md)|[5](/guides/chall5.md)|[6](/guides/chall6.md)|[7](/guides/chall7.md)|[8](/guides/chall8.md)|[9](/guides/chall9.md)|[10](/guides/chall10.md)|[END](/guides/end.md)|[>>](/guides/chall5.md)|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|

#### Piškotek / Cookie = MSNSWJy5UZecnE7GFxnP2pu1nXm46uA7V5seou3sIOsF31wMPzOIWazGmjPqbVeH

# Problem 4 / Challenge 4
Forbidden

![Image](/guides/images/image4.png)


# Namigi / Hints

<details >
<summary>
    <i>Namig 1</i> 
</summary>
    Base64, kako izgleda
</details>

<details >
<summary>
    <i>Namig 2</i> 
</summary>
🍪
</details>
<details >
<summary>
    <i>Namig 3</i> 
</summary>
Kje najdemo 🍪 in kaj se zgodi če jih pretvorimo iz base64?
</details>
<br>

# Rešitev / Solution

<details>
<summary><b>
    Rešitev
</b></summary>
    Spremeni piškotek <b>session</b> v <code>eyJpZCI6ICJyM2FuOXI4bGxzWTh2bzVpIiwgImFkbWluIjogdHJ1ZX0=</code>


</details>
<details>
<summary><b>
    Opis
</b></summary>
Če dekodiramo piškotek <code>session</code> iz base64 <b>{"id": "r3an9r8llsY8vo5i", "admin": false} </b> , in spremenimo false v true in zakodiramo v base64 ter zamenjano 🍪.

[Dekodirnik](https://www.base64decode.org/), [Kodirnik](https://www.base64encode.org/)

</details>