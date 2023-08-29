|[<<](/guides/chall5.md)|[START](/guides/main.md)|[0](/guides/chall0.md)|[1](/guides/chall1.md)|[2](/guides/chall2.md)|[3](/guides/chall3.md)|[4](/guides/chall4.md)|[5](/guides/chall5.md)|[6](/guides/chall6.md)|[7](/guides/chall7.md)|[8](/guides/chall8.md)|[9](/guides/chall9.md)|[10](/guides/chall10.md)|[END](/guides/end.md)|[>>](/guides/chall7.md)|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|

#### Piškotek / Cookie = MoZrXv6VIc2K2AlFJOqSImyYcnasay1UfPm1xi4fyUzREBw6ZNa3igOvyyNze6p1

# Problem 6 / Challenge 6
(Non-blockchain) Kriptosistemi

![Image](/guides/images/image6.png)


# Namigi / Hints

<details>
<summary>
    <i>Namig 1</i> 
</summary>
    Poiskusi si poenostaviti problem
</details>

<details>
<summary>
    <i>Namig 2</i> 
</summary>
    Ali dolžina, drugačne črke vplivajo na izhod?
</details>
<details >
<summary>
    <i>Namig 3</i> 
</summary>
    Torej kriptograf samo zamenja črke ne glede na besedilo?
</details>
<br>

# Rešitev / Solution

<details>
<summary><b>
    Rešitev
</b></summary>
    monada je monoid v kategoriji endofunktorjev
</details>
<details>
<summary><b>
    Opis
</b></summary>

```py
# sortirano
sortirano = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQR'
# vrnjeno iz "kriptosistem"
zakodirano = 'miBhFyvDHgCKAosGtcMLJuEzPQfNjkRdqnOwbraIxlep'
# šifra
koda = 'nejjnot o inii dkntkuaerjeao mva oreovmfgodd'

vrni = ""
for crka in sortirano:
    zakodiran_index = zakodirano.index(crka)
    # v vrni dodamo dekodirano crko
    vrni = vrni + koda[zakodiran_index]
    
print(vrni)
```
</details>

