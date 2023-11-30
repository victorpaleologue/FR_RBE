# Les primitifs

Le langage Rust offre une grande variété de primitifs. Liste non-exhaustive :


* Les entiers signés : `i8`, `i16`, `i32`, `i64` et `isize` (dépend de l'architecture de la machine) ;
* Les entiers non-signés : `u8`, `u16`, `u32`, `u64`, `usize` (dépend de l'architecture de la machine) ;
* Les réels : `f32`, `f64`;
* Les caractères (Unicode) : `‘a'`, `‘α'`, `‘∞'`. Codés sur 4 octets;
* Les booléens : `true` ou `false`;
* L'absence de type `()`, qui n'engendre qu'une seule valeur : `()`;
* Les tableaux : `[1, 2, 3]`;
* Les tuples : `(1, true)`.

Le type des variables peut toujours être spécifié. Les nombres peuvent également être typés grâce à un suffixe, ou par défaut (laissant le compilateur les typer). Les entiers, par défaut, sont typés `i32` tandis les réels sont typés `f64`.

```rust,editable
fn main() {
    // Le type des variables peut être spécifié, annoté.
    let logical: bool = true;

    let a_float: f64 = 1.0;  // typage classique
    let an_integer   = 5i32; // Typage par suffixe

    // Le type par défaut peut également être conservé.
    // typage implicite
    let default_float   = 3.0; // `f64`
    let default_integer = 7;   // `i32`

    let mut mutable = 12; // Entier signé codé sur 4 octets (i32).

    // Erreur! Le type d'une variable ne peut être modifié en cours de route.
    // mutable = true;
}
```

## Voir aussi

[La bibliothèque standard][std].

[std]: https://doc.rust-lang.org/std/
