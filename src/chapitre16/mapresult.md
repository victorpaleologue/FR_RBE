# La méthode `map` pour `Result`

Nous avons noté dans l'exemple précédent que le message d'erreur affiché lorsque le programme "panique" ne nous était pas d'une grande aide. Pour éviter cela, nous devons être plus précis concernant le type de renvoi. Ici, l'élément est de type `i32`.
Pour déterminer le type de `Err`, jetons un oeil à la documentation de la méthode [`parse()`][parse], qui est implémentée avec le trait [`FromStr`][from_str] pour le type [`i32`][i32]. Dans un résultat, le type de `Err` est [`ParseIntError`][parse_int_error].

Dans l'exemple ci-dessous, utiliser directement `match` mène à coder quelque chose de relativement lourd. Heureusement, la méthode `map` de `Option` est l'un de ces nombreux combinateurs ont également été implémentés pour `Result`. [enum.Result][enum_result] en tient une liste complète.

```rust,editable
use std::num::ParseIntError;

// Maintenant que le type de renvoi a été réécrit, nous utilisons le pattern matching 
// sans la méthode `unwrap()`.
fn double_number(number_str: &str) -> Result<i32, ParseIntError> {
    match number_str.parse::<i32>() {
        Ok(n)  => Ok(2 * n),
        Err(e) => Err(e),
    }
}


// Tout comme avec `Option`, nous pouvons utiliser les combinateurs tels que `map()`.
// Cette fonction possède le même fonctionnement que celle ci-dessus et se lit comme suit:
// Modifie n si la valeur est valide, sinon renvoie une erreur.
fn double_number_map(number_str: &str) -> Result<i32, ParseIntError> {
    number_str.parse::<i32>().map(|n| 2 * n)
}

fn print(result: Result<i32, ParseIntError>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    // Ceci fournit toujours une réponse valable.
    let twenty = double_number("10");
    print(twenty);

    // Ce qui suit fournit désormais un message d'erreur plus intelligible.
    let tt = double_number_map("t");
    print(tt);
}

```

[parse]: https://doc.rust-lang.org/std/primitive.str.html#method.parse
[from_str]: https://doc.rust-lang.org/std/str/trait.FromStr.html
[i32]: https://doc.rust-lang.org/std/primitive.i32.html
[parse_int_error]: https://doc.rust-lang.org/std/num/struct.ParseIntError.html
[enum_result]: https://doc.rust-lang.org/std/result/enum.Result.html
