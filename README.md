# Zadání

Do souboru `sleva.py` napište v Pythonu funkci `zlevni` tak, aby na vstupu měla:
- povinný parametr `cena`: cena, ze které se bude zlevňovat
- parametr `procento`: může nabývat hodnoty 0-99, celočíselný, budeme optimisticky očekávat, že rozsah 0-99 uživatel funkce vždy dodrží (nedělejte žádné extra kontroly)

Na výstupu bude funkce vracet zlevněnou cenu.

Napište funkci tak, aby jí šlo volat i bez druhého parametru. V takovém případě bude default sleva `10%`.

Funkci musí jít zavolat následujícími způsoby:

```
# vrátí 36
zlevni(45, 20)

# vrátí 90
zlevni(100)

# vrátí 1490.5
zlevni(1490.5,0)
```

# Co hodnotím

- linter mypy nesmí ukazovat žádnou chybu (čistota kódu)
- správnost implementace: dodržení zadání
- čitelnost vašeho kódu
