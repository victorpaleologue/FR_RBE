# `Box`ing des erreurs

En implémentant `Display` et `Form` pour notre type d'erreur, nous avons usé de *presque* tous les outils dédiés à la gestion d'erreur de la bibliothèque standard. Nous avons cependant oublié quelque chose: la capacité à simplement `Box` notre type.

La bibliothèque standard convertit n'importe quel type qui implémente le trait `Error` et sera pris en charge par le type `Box<Error>`, via `From`. Pour l'utilisateur d'une bibliothèque, ceci permet aisément une manoeuvre de ce genre:

```rust,ignore
fn foo(...) -> Result<T, Box<Error>> { ... }
```

Un utilisateur peut utiliser nombre de bibliothèques externes, chacune fournissant leurs propres types d'erreur. Pour définir un type de `Result<T, E>` valide, l'utilisateur a plusieurs options:

* Définir un nouveau wrapper englobant les types d'erreur de la bibliothèque;
* Convertir les types d'erreur en `String` ou vers un autre type intermédiaire;
* `Box` les types dans `Box<Error>`.

Le "boxing" du type d'erreur est un choix plutôt habituel. Le problème est que le type de l'erreur sous-jacente est connu à l'exécution et n'est pas [déterminé statiquement][static_dispatch]. Comme mentionné plus haut, tout ce qu'il y a à faire c'est d'implémenter le trait `Error`:

```rust,ignore
trait Error: Debug + Display {
    fn description(&self) -> &str;
    fn cause(&self) -> Option<&Error>;
}
```

Avec cette implémentation, jetons un oeil à notre exemple récemment présenté. Notez qu'il est tout aussi fonctionnel avec le type `Box<Error>` qu'avec `DoubleError`:

```rust,editable
use std::error;
use std::fmt;
use std::num::ParseIntError;

// On modifie l'alias pour ajouter `Box<error::Error>`.
type Result<T> = std::result::Result<T, Box<error::Error>>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    Parse(ParseIntError),
}

impl From<ParseIntError> for DoubleError {
    fn from(err: ParseIntError) -> DoubleError {
        DoubleError::Parse(err)
    }
}

impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec =>
                write!(f, "please use a vector with at least one element"),
            DoubleError::Parse(ref e) => e.fmt(f),
        }
    }
}

impl error::Error for DoubleError {
    fn description(&self) -> &str {
        match *self {
            // Courte description de l'erreur.
            // Vous n'êtes pas obligé de renseigner la même description que 
            // pour `Display`.
            DoubleError::EmptyVec => "empty vectors not allowed",
            // Ceci implémente déjà `Error`, on se reporte à sa propre implémentation.
            DoubleError::Parse(ref e) => e.description(),
        }
    }

    fn cause(&self) -> Option<&error::Error> {
        match *self {
            // Pas de cause (i.e. pas d'autre erreur) 
            // sous-jacente au déclenchement de cette erreur, donc on renvoie `None`.
            DoubleError::EmptyVec => None,
            // La cause est l'implémentation sous-jacente du type d'erreur. 
            // Il (le type) est implicitement casté en `&error::Error`. 
            // Ca fonctionne parce que le type en question a déjà implémenté le trait `Error`.
            DoubleError::Parse(ref e) => Some(e),
        }
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = try!(vec.first().ok_or(DoubleError::EmptyVec));
    let parsed = try!(first.parse::<i32>());

    Ok(2 * parsed)
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let numbers = vec!["93", "18"];
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(numbers));
    print(double_first(empty));
    print(double_first(strings));
}

```

## Voir aussi

[Distribution dynamique][static_dispatch] et 
[le trait `Error`][error_trait].

[static_dispatch]: https://doc.rust-lang.org/book/trait-objects.html#dynamic-dispatch
[error_trait]: https://doc.rust-lang.org/std/error/trait.Error.html
