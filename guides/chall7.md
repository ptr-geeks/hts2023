|[<<](/guides/chall6.md)|[START](/guides/main.md)|[0](/guides/chall0.md)|[1](/guides/chall1.md)|[2](/guides/chall2.md)|[3](/guides/chall3.md)|[4](/guides/chall4.md)|[5](/guides/chall5.md)|[6](/guides/chall6.md)|[7](/guides/chall7.md)|[8](/guides/chall8.md)|[9](/guides/chall9.md)|[10](/guides/chall10.md)|[END](/guides/end.md)|[>>](/guides/chall8.md)|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|:-|

#### Piškotek / Cookie = XPOPInHgyRf7cFQKiXyJBz0hycrlMiUxSKScVAqL4xeNcbJCnvXiFueadG75fm4T

# Problem 7 / Challenge 7

![Image](/guides/images/image7.png)

```py
def validate_flags(request_data):
    flags = get_current_flags()
    for i in range(1, 8):
        flags[i] = flags[i] ^ flags[i - 1]
    for i in range(8):
        if flags[i] != request_data[i]:
            return False
    return True
```

# Namigi / Hints

<details>
<summary>
    <i>Namig 1</i> 
</summary>
    Ti ne moreš napisati 8 flagov v 3 sekundah, ampak kdo pa jih lahko?
</details>

<details>
<summary>
    <i>Namig 2</i> 
</summary>
    Ne pozabi na validiranje flagov :)
</details>
<details>
<summary>
    <i>Namig 3</i> 
</summary>

    Kako lahko s programom dobiš flage? (spomni se na API)
</details>
<br>

# Rešitev / Solution

<details>
<summary><b>
    Rešitev
</b></summary>

    Narediš program, ki prebere flage in jih vrne.
    Dobiš cookie za naslednjo nalgo
</details>
<details>
<summary><b>
    Opis
</b></summary>

## Pridobitev flagov
```python
import requests  

url = "https://hts.ptr.si" 

# nastavimo piškotek    
cookie = {'c': 'XPOPInHgyRf7cFQKiXyJBz0hycrlMiUxSKScVAqL4xeNcbJCnvXiFueadG75fm4T'}

def get_flags():
    flags = []
    # ponovimo 8x za 8 flagov
    for i in range(8):
        # pridobimo flag in ga shranimo kot int v seznam
        resp = requests.get(f"{url}/s/flag{i+1}", cookies=cookie).text
        flags.append(int(resp))
    return flags

flags = get_flags()

# XOR operacija z flagi
for i in range(1, 8):
    flags[i] = flags[i] ^ flags[i - 1]
```
## Vrnitev podatkov

### Pyautogui
```python
import pyautogui as pag
for i in range(8):
    pag.typewrite(str(flags[i]))
    pag.press("tab")
    
pag.press("enter")
```
ali 

### Pošljemo request s flagi

```python
PAYLOAD = "flag1={}&flag2={}&flag3={}&flag4={}&flag5={}&flag6={}&flag7={}&flag8={}&submit=Prove+you%27re+a+robot"

resp = requests.post(f"{url}/challenge", data = PAYLOAD.format(*flags), cookies = cookie, headers={"Content-Type": "application/x-www-form-urlencoded"}, allow_redirects = False).headers

print(resp)
print("-------")
print(resp["Set-Cookie"])

```

</details>

