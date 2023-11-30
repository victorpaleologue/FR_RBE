# Les alias de `Result`

Quid lorsque nous souhaitons réutiliser un type de `Result` bien précis ? Rappelez-vous que Rust nous permet de créer des [alias][alias]. Nous pouvons alors aisément en définir un pour le type de `Result` en question.

À l'échelle d'un module, la création d'alias peut être salvatrice. Les erreurs pouvant être trouvées dans un module pécis ont souvent le même type (wrappé par `Err`), donc un seul alias peut définir *l'intégralité* des `Result`s associés. C'est tellement utile que la bibliothèque standard en fournit un: `io::Result` !

Voici un petit exemple pour présenter la syntaxe:

```rust,editable
use std::num::ParseIntError;

// On définit un alias générique pour un type de `Result` avec le type d'erreur 
// `ParseIntError`.
type AliasedResult<T> = Result<T, ParseIntError>;

// On utilise l'alias ci-dessus pour faire référence à notre 
// `Result`.
fn double_number(number_str: &str) -> AliasedResult<i32> {
    number_str.parse::<i32>().map(|n| 2 * n)
}

// Ici, l'alias nous permet encore d'épargner de l'espace.
fn print(result: AliasedResult<i32>) {
    match result {
        Ok(n)  => println!("n is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    print(double_number("10"));
    print(double_number("t"));
}

```

## Voir aussi

[`Result`][result] et [`io::Result`][io_result].

[alias]: ../chapitre5/alias.html
[result]: https://doc.rust-lang.org/std/result/enum.Result.html
[io_result]: https://doc.rust-lang.org/std/io/type.Result.html
