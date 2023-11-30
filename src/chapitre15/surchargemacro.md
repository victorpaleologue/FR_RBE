# Surcharge

Les macros peuvent être surchargées pour accepter différentes combinaisons d'arguments. Dans cet esprit, `macro_rules!` peut fonctionner de la même manière qu'un bloc `match`:

```rust,editable
// `test!` va comparer `$left` et `$right` de différentes 
// manières suivant son utilisation à l'invocation:
macro_rules! test {
    // Il n'est pas nécessaire de séparer les arguments par des virgules.
    // N'importe quel modèle peut être utilisé !
    ($left:expr; and $right:expr) => (
        println!("{:?} and {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left && $right)
    );
    // ^ Chaque branche doit se terminer par un point-virgule.
    ($left:expr; or $right:expr) => (
        println!("{:?} or {:?} is {:?}",
                 stringify!($left),
                 stringify!($right),
                 $left || $right)
    );
}

fn main() {
    test!(1i32 + 1 == 2i32; and 2i32 * 2 == 4i32);
    test!(true; or false);
}

```
