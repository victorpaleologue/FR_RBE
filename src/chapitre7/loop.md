# Le mot-clé loop

Rust fournit le mot-clé `loop` pour créer une boucle infinie.

Le mot-clé `break` peut être utilisé pour sortir de la boucle n'importe où tandis que le mot-clé `continue` peut être utilisé pour ignorer le reste de l'itération en cours et en débuter une nouvelle.

```rust,editable
fn main() {
    let mut count = 0u32;

    println!("Comptons jusqu'à l'infini!");

    // Boucle infinie.
    loop {
        count += 1;

        if count == 3 {
            println!("trois");

            // Ignore le reste de l'itération.
            continue;
        }

        println!("{}", count);

        if count == 5 {
            println!("Ok, ça suffit!");

            // Sort de la boucle.
            break;
        }
    }
}
```

