# Restrictions multiples

Il est possible d'additionner les conditions grâce à l'opérateur `+`. Tout comme les types concrets, les types génériques sont séparés par une virgule `,`.

```rust,editable
use std::fmt::{Debug, Display};

fn compare_prints<T: Debug + Display>(t: &T) {
    println!("Debug: `{:?}`", t);
    println!("Display: `{}`", t);
}

fn compare_types<T: Debug, U: Debug>(t: &T, u: &U) {
    println!("t: `{:?}", t);
    println!("u: `{:?}", u);
}

fn main() {
    let string = "words";
    let array = [1, 2, 3];
    let vec = vec![1, 2, 3];

    compare_prints(&string);
    // compare_prints(&array);
    // TODO ^ Essayez de décommenter cette ligne.

    compare_types(&array, &vec);
}

```

## Voir aussi

[std::fmt][fmt], [les traits][traits].

[fmt]: ../chapitre1/affichage.html
[traits]: ../chapitre14/traits.html
