# Déclaration seule

Il est possible de déclarer une variable dans un premier temps, pour l'initialiser dans un second temps. Cependant, cette forme est rarement utilisée puisqu'elle peut conduire à l'utilisation de variables qui ne sont pas initialisées (et donc à faire des erreurs).

```rust,editable
fn main() {
    // On déclare une variable.
    let a_binding;

    {
        let x = 2;

        // On initialise la variable.
        a_binding = x * x;
    }

    println!("a binding: {}", a_binding);

    let another_binding;

    // Erreur! Utilisation d'une variable non-initialisée.
    // println!("another binding: {}", another_binding);
    // FIXME ^ Décommentez cette ligne pour voir l'erreur.
    another_binding = 1;

    println!("another binding: {}", another_binding);
}

```

Comme l'utilisation d'une variable, qui n'a pas été initialisée au préalable, peut mener à des comportements imprévisibles à l'exécution, le compilateur vous interdit de les utiliser.
