# Répétition

Les macros peuvent utiliser le quantificateur `+` dans la liste des arguments pour indiquer qu'un argument peut être répété au moins une(1) fois ou `*` pour indiquer que l'argument peut être répété zéro(0) ou plusieurs fois.

Dans l'exemple suivant, entourer le matcher avec `$(...),+` va permettre la capture d'une ou plusieurs expressions, séparées par des virgules. Notez également que le point-virgule est optionnel dans le dernier cas (i.e. la dernière expression capturée).

```rust,editable
// `min!` va calculer le minimum entre chaque argument passé, peu importe le nombre.
macro_rules! find_min {
    // Expression de base:
    ($x:expr) => ($x);
    // `$x` suivi par au moins un `$y,`.
    ($x:expr, $($y:expr),+) => (
        // On appelle `find_min` sur les $y suivants`.
        std::cmp::min($x, find_min!($($y),+))
    )
}

fn main() {
    println!("{}", find_min!(1u32));
    println!("{}", find_min!(1u32 + 2 , 2u32));
    println!("{}", find_min!(5u32, 2u32 * 3, 4u32));
}

```
