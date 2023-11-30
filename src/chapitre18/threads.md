# Les fils d'exécution

Rust fournit un méchanisme de création de fils d'exécution natifs via la fonction `spawn`. L'argument de cette fonction est une closure transférable.

```rust,editable
use std::thread;

static NTHREADS: i32 = 10;

// Ceci est le thread `main`.
fn main() {
    // On créé un vecteur pour récupérer tous les threads 
    // enfants qui ont été créés.
    let mut children = vec![];

    for i in 0..NTHREADS {
        // On passe à un autre thread.
        children.push(thread::spawn(move || {
            println!("this is thread number {}", i)
        }));
    }

    for child in children {
        // On attend que le thread se termine. Renvoie un résultat.
        let _ = child.join();
    }
}

```

Ces threads seront programmés par le système d'exploitation.
