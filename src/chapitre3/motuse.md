# Le mot-clé use

Grâce au mot-clé `use`, il n'est pas toujours obligatoire de spécifier le contexte d'une ressource à chaque utilisation.

```rust,editable
// Masque les avertissements du compilateur concernant le code mort.
#![allow(dead_code)]

enum Status {
    Rich,
    Poor,
}

enum Work {
    Civilian,
    Soldier,
}

fn main() {
    // Nous précisons que ces variantes de l'énumération sont utilisées, donc 
    // il n'est plus nécessaire de préciser leur conteneur.
    use Status::{Poor, Rich};
    // On utilise automatiquement toutes les variantes de l'enum `Work`.
    use Work::*;

    // Equivalent à `Status::Poor`.
    let status = Poor;
    // Equivalent à `Work::Civilian`.
    let work = Civilian;

    match status {
        // Notez la disparition du conteneur lors de la recherche de pattern.
        Rich => println!("The rich have lots of money!"),
        Poor => println!("The poor have no money..."),
    }

    match work {
        // Une fois encore, le conteneur a disparu.
        Civilian => println!("Civilians work!"),
        Soldier  => println!("Soldiers fight!"),
    }
}
```

## Voir aussi

[Le mot-clé match][match] et [la déclaration use][use].

[match]: ../chapitre7/match.html
[use]: ../chapitre9/usedeclaration.html
