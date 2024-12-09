# Парсер многочленов

## Задание

Каноническая запись многочлена с целыми коэффициентами. Операции с 0 и 1 упрощены.
Пример. Правильные записи: `x^2-28x^120+467x^2+x-1200` `-x^25`  
Неправильные записи: `1x^3` `x+0` `x^0` `x^1` `x^-25`

## Описание

Программа проверяет корректность введенного многочлена и выводит его синтаксическое дерево.

## Примеры

```bash
$ python main.py
Welcome to the polynomial parser
Enter a polynomial to parse or press CTRL + C to quit
Enter a polynomial: 2x
Result syntax tree:
{
  "type": "Polynom",
  "first_term": {
    "type": "FirstTerm",
    "opt_sign": null,
    "factor": {
      "type": "Factor",
      "proper_integer": {
        "type": "ProperInteger",
        "starts_with_2_to_9": "2",
        "digits": []
      },
      "maybe_x_part": {
        "type": "MaybeXPart",
        "x": true,
        "power_part": {
          "type": "PowerPart",
          "epsilon": true
        }
      }
    }
  },
  "more_terms": {
    "type": "MoreTerms",
    "epsilon": true
  }
}
Parsed successfully!
...
```

## Требования

- Python 3.10-3.12

## Установка

Скопируйте репозиторий и перейдите в папку с проектом:

```bash
git clone
```

```bash
cd polynomial-parser
```

Запустите программу:

```bash
$ python main.py
Welcome to the polynomial parser
Enter a polynomial to parse or press CTRL + C to quit
Enter a polynomial:
```
