![image](/guides/images/title.png)

# Hack This Site (HTS) 
is a series of Hacking challenges with each increasing in difficulty and a cake at the end.

# Hack this site
je spletna stran desetih hekerskih izzivov, ki se stopnjujejo v težavnosti.

Problemi so, ampak se ne omejujejo na:
1. Permutacijska šifra,
2. Šifre,
3. SQLI,
4. ...

<!-- 
basic challenges
00. Sanity check
01. HTML Comment
02. HTTP Headers
03. Cesar cipher
04. Base64 JSON admin:false
05. SQLI
06. Permutation cipher
07. OTP Automation
08. Image optimizer SSRF
09. Double Server
10. Rev-->

# "Navodila", namigi in ostale informacije

[Tukaj](/guides/main.md)

# Self host
Želiš pognati spletno stran sam, da bi se preiskusil?
(nekate funkcije mogoče ne bodo delovale)


```bash
git clone https://github.com/ptr-geeks/hts2023
cd hts2023/server
pip install -r requirements.txt
```

## Windows

```bash
py localhost.py
```

## Linux 
```bash
gunicorn -w 4 -b 0.0.0.0:8000 server:app
```