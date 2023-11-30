# Les méthodes

Les méthodes sont annotées de la même manière que les fonctions :

```rust,editable
struct Owner(i32);

impl Owner {
    // On déclare et annote les lifetimes comme 
    // dans une fonction traditionnelle.
    fn add_one<'a>(&'a mut self) { self.0 += 1; }
    fn print<'a>(&'a self) {
        println!("`print`: {}", self.0);
    }
}

fn main() {
    let mut owner  = Owner(18);

    owner.add_one();
    owner.print();
}

```

## Voir aussi

[Les méthodes][methodes].

[methodes]: ../chapitre8/methodes.html
