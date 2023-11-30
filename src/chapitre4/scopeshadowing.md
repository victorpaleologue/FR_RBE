# Scope et shadowing

Les assignations possèdent un contexte dans lequel elles persisteront et qui sera représenté par un « bloc ». Un bloc est une suite d'instructions et de déclarations englobées par des accolades `{}`. Le [shadowing][shadowing] est également permis.

```rust,editable
fn main() {
    // Cette assignation vit dans la fonction `main`.
    let long_lived_binding = 1;

    // Ceci est un bloc, il possède un contexte plus petit que celui de la fonction 
    // `main`.
    {
        // Cette assignation existe seulement dans ce bloc.
        let short_lived_binding = 2;

        println!("inner short: {}", short_lived_binding);

        // Cette assignation *masque* l'assignation du contexte supérieur (la fonction 
        // `main`).
        let long_lived_binding = 5_f32;

        println!("inner long: {}", long_lived_binding);
    }
    // Fin du bloc.

    // Erreur! `short_lived_binding` n'existe pas dans ce contexte.
    // println!("outer short: {}", short_lived_binding);
    // FIXME ^ Décommentez cette ligne pour voir l'erreur.

    println!("outer long: {}", long_lived_binding);

    // Cette assignation *masque* également l'assignation précédente.
    let long_lived_binding = 'a';

    println!("outer long: {}", long_lived_binding);
}

```

[shadowing]: https://en.wikipedia.org/wiki/Variable_shadowing
