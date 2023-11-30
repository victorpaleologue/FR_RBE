# Les tuples

Un tuple est une collection de valeurs de différents types (ou pas). Les tuples peuvent être construits en utilisant les parenthèses `()` et chaque tuple est lui-même un type possédant sa propre signature `(T1, T2, …)`, où `T1, T2` sont les types de ses membres. Les fonctions peuvent se servir des tuples pour renvoyer plusieurs valeurs, puisque ces derniers peuvent être extensibles à volonté.

```rust,editable
// Les tuples peuvent être utilisés comme arguments passés à une fonction 
// et comme valeurs de renvoi.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` peut être utilisé pour assigner, lier les membres d'un tuple à des 
    // variables.
    let (integer, boolean) = pair;

    (boolean, integer)
}

// La structure suivante est dédiée à l'activité.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // Un tuple composé de différents types
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // Les valeurs peuvent être extraites depuis le tuple en utilisant son 
    // indexation.
    println!("long tuple first value: {}", long_tuple.0);
    println!("long tuple second value: {}", long_tuple.1);

    // Les tuples peuvent être eux-même des membres d'un tuple.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Les tuples peuvent être affichés avec Debug.
    println!("tuple of tuples: {:?}", tuple_of_tuples);

    let pair = (1, true);
    println!("pair is {:?}", pair);

    println!("the reversed pair is {:?}", reverse(pair));

    // Pour créer un élément de tuple, une virgule est requise pour différencier 
    // un élément de tuple d'un simple litéral entouré de parenthèses.
    println!("one element tuple: {:?}", (5u32,));
    println!("just an integer: {:?}", (5u32));

    // Les tuples peuvent être "déstructurés" (i.e. décomposés pour créer de 
    // nouvelles assignations).
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix)

}

```

## Activité

1. Récapitulatif : Implémentez les services du trait `fmt::Display` pour la structure `Matrix` dans l'exemple ci-dessus. Donc si vous passez de l'affichage de débogage `{:?}` à l'affichage plus « user friendly » `{}`, vous devriez voir le résultat suivant :

```text
( 1.1 1.2 )
( 2.1 2.2 )
```

Vous pouvez vous référer à l'exemple précédemment donné pour [l'implémentation du trait Display][display].

2. Ajoutez une fonction `transpose()`, en vous appuyant sur l'implémentation de la fonction `reverse()`, qui accepte une matrice en paramètre et renvoie une matrice dans laquelle deux éléments ont été inversés. Exemple :

```bash
println!("Matrix:\n{}", matrix);
println!("Transpose:\n{}", transpose(matrix));
```

Affiche:

```text
Matrix:
( 1.1 1.2 )
( 2.1 2.2 )
Transpose:
( 1.1 2.1 )
( 1.2 2.2 )
```

[display]: ../chapitre1/display.html
