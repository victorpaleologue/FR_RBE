# Les littéraux et les opérateurs

Les entiers (`1`), les réels (`1,2`), les caractères (`'a'`), les chaînes de caractères (`"abc"`), les booléens (`true`) et l'absence de type `()` (un tuple vide) peuvent être représentés en utilisant les littéraux.

Les entiers peuvent également être exprimés sous différentes bases : hexadécimal, octal ou binaire en utilisant, respectivement, les préfixes : `0x`, `0o` ou `0b`.

Des underscores peuvent être insérés à l'intérieur des littéraux numériques pour soigner la lisibilité (e.g. `1_000` est équivalent à `1000` et `0.000_001` est équivalent à `0.000001`).

Nous devons renseigner le compilateur quant au type de littéral que nous utilisons. Pour le moment, nous allons utiliser le suffixe `u32` pour indiquer que le littéral est un entier non-signé codé sur 32 bits et le suffixe `i32` pour indiquer que c'est un entier signé codé sur 32 bits.

Les opérateurs et leur priorité [dans le langage Rust][operators] peuvent être retrouvés dans [les langages « C-like »][clike].

```rust,editable
fn main() {
    // Addition d'entiers
    println!("1 + 2 = {}", 1u32 + 2);

    // Soustraction d'entiers
    println!("1 - 2 = {}", 1i32 - 2);
    // TODO ^ Essayez de changer `1i32` par `1u32` pour prendre conscience de l'importance du type

    // Logique booléenne
    println!("true AND false is {}", true && false);
    println!("true OR false is {}", true || false);
    println!("NOT true is {}", !true);

    // Opérations bit-à-bit
    println!("0011 AND 0101 is {:04b}", 0b0011u32 & 0b0101);
    println!("0011 OR 0101 is {:04b}", 0b0011u32 | 0b0101);
    println!("0011 XOR 0101 is {:04b}", 0b0011u32 ^ 0b0101);
    println!("1 << 5 is {}", 1u32 << 5);
    println!("0x80 >> 2 is 0x{:x}", 0x80u32 >> 2);

    // Utilisez des underscores pour améliorer la lisibilité !
    println!("One million is written as {}", 1_000_000u32);
}
```

[operators]: http://doc.rust-lang.org/reference.html#operator-precedence
[clike]: https://en.wikipedia.org/wiki/Operator_precedence#Programming_languages
