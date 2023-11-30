# while let

Ayant un fonctionnement similaire à `if let`, `while let` peut alléger la syntaxe de `match` lorsqu'il n'est pas nécessaire de passer par le *pattern matching*. Voici une séquence qui incrémente `i` :

```rust,editable
// Crée une valeur optionnelle de type `Option<i32>`.
let mut optional = Some(0);

// On répète le test.
loop {
    match optional {
        // Si il est possible de déstructurer `optional`, 
        // le bloc sera exécuté.
        Some(i) => {
            if i > 9 {
                println!("Plus grand que 9, on quitte!");
                optional = None;
            } else {
                println!("`i` est égal à `{:?}`. On réitère.", i);
                optional = Some(i + 1);
            }
            // ^ Nécessite trois niveaux d'indentations.
        },
        // On quitte la boucle si la déstructuration 
        // a échoué:
        _ => { break; }
        // ^ Pourquoi cette instruction devrait être nécessaire ?
        // Il doit y avoir une solution plus adaptée!
    }
}
```

En utilisant `while let`, cela rend la séquence plus lisible :

```rust,editable
fn main() {
    // Crée une valeur optionnelle de type `Option<i32>`.
    let mut optional = Some(0);

    // Fonctionnement: "`while let` déstructure `optional` pour assigner sa valeur 
    // à Some(i) puis exécute le bloc (`{}`). Sinon, on sort de la boucle."
    while let Some(i) = optional {
        if i > 9 {
            println!("Plus grand que 9, on quitte!");
            optional = None;
        } else {
            println!("`i` est égal à `{:?}`. On réitère.", i);
            optional = Some(i + 1);
        }
        // Moins explicite, il n'est plus nécessaire de gérer 
        // le cas où la déstructuration échoue.
    }
    // ^ `if let` permet d'ajouter des branches `else`/`else if` 
    // optionnelles. `while let` ne le permet pas, en revanche.
}
```

## Voir aussi

[Les énumérations][enums], [l'énumération `Option`][option] et [la RFC de while let][rfc].

[enums]: ../chapitre3/enum.html
[option]: ../chapitre17/enumoption.html
[rfc]: https://github.com/rust-lang/rfcs/pull/214
