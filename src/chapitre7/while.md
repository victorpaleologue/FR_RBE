# La boucle while

Le mot-clé `while` peut être utilisé pour itérer jusqu'à ce qu'une condition soit remplie.

Écrivons les règles de l'infâme [FizzBuzz][fizzbuzz] en utilisant une boucle `while`:

```rust,editable
fn main() {
    // Un compteur.
    let mut n = 1;

    // Itère sur `n` tant que sa valeur est strictement inférieure 
    // à 101.
    while n < 101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }

        // Incrémente le compteur.
        n += 1;
    }
}
```

[fizzbuzz]: http://en.wikipedia.org/wiki/Fizz_buzz
