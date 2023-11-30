# Les fonctions d'ordre supérieur

Rust supporte les [fonctions d'ordre supérieur][hof] (HOF). Ces fonctions prennent en paramètre une ou plusieurs fonctions et renvoie une autre fonction. Ce sont les HOF ainsi que les « [itérateurs laxistes][lazy] » qui donnent cet aspect fonctionnel à Rust.

```rust,editable
fn is_odd(n: u32) -> bool {
    n % 2 == 1
}

fn main() {
    println!("Find the sum of all the squared odd numbers under 1000");
    let upper = 1000;

    // Approche impérative.
    // On déclare un accumulateur.
    let mut acc = 0; // 0, 1, 2, ... ∞
    for n in 0.. {
        // Le carré du nombre.
        let n_squared = n * n;

        if n_squared >= upper {
            // On sort de la boucle si le carré de `n_squared` 
            // dépasse la limite imposée par `upper`.
            break;
        } else if is_odd(n_squared) {
            // On accumule le carré de `n_squared` si c'est impair.
            acc += n_squared;
        }
    }
    println!("imperative style: {}", acc);

    // Approche fonctionnelle.
    let sum_of_squared_odd_numbers: u32 =
        (0..).map(|n| n * n)             // On calcule le carré de chaque nombre.
             .take_while(|&n| n < upper) // On vérifie que le carré se trouve toujours sous la limite de `upper`.
             .filter(|&n| is_odd(n))     // On récupère le nombre si il est impair.
             .fold(0, |sum, i| sum + i); // On accumule le carré du nombre impair.
    println!("functional style: {}", sum_of_squared_odd_numbers);
}

```

L'énumération [Option][option] et le trait [Iterator][iterator] implémentent leur lot d'HOF.

[hof]: https://fr.wikipedia.org/wiki/Fonction_d'ordre_supérieur
[lazy]: https://stackoverflow.com/questions/2155788/most-of-the-iterators-and-iterables-methods-are-lazy-what-does-this-mean/2155801#2155801
[option]: http://doc.rust-lang.org/core/option/enum.Option.html
[iterator]: http://doc.rust-lang.org/core/iter/trait.Iterator.html
