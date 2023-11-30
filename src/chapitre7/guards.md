# Les gardes

Lorsque vous usez du *pattern matching*, un « garde » peut être ajouté dans chaque branche du `match`.

```rust,editable
fn main() {
    let pair = (2, -2);
    // TODO ^ Essayez de modifier les valeurs de `pair`.

    println!("Dites m'en plus à propos de: {:?}", pair);
    match pair {
        (x, y) if x == y => println!("Ils sont jumeaux!"),
        // La ^ condition if est un garde.
        (x, y) if x + y == 0 => println!("De l'antimatière, boom!"),
        (x, _) if x % 2 == 1 => println!("Le premier est étrange..."),
        _ => println!("Rien de spécial..."),
    }
}
```

## Voir aussi

[Les tuples][tuples].

[tuples]: ../chapitre2/tuples.html
