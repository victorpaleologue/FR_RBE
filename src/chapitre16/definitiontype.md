# Définition d'un type d'erreur

Rust nous permet de définir nos propres types d'erreur. En général, un "bon" type d'erreur:

* Représente différentes erreurs avec le même type;
* Présente un message d'erreur intelligible pour l'utilisateur;
* Est facilement comparable aux autres types;
    * Bien: `Err(EmptyVec)`,
    * Pas bien: `Err("Please use a vector with at least one element".to_owned())`.
* Peut supporter l'ajout d'informations à propos de l'erreur;
    * Bien: `Err(BadChar(c, position))`,
    * Pas bien: `Err("+ cannot be used here".to_owned())`.

Notez qu'une `String` (que nous utilisions jusqu'ici) remplit les deux premiers critères, mais pas les deux derniers. 
Cela rend la création d'erreurs, simplement en utilisant `String`, verbeuse et difficile à maintenir. Il ne devrait pas être nécessaire de polluer la logique du code avec le formattage des chaînes de caractères pour avoir un affichage intelligible.

```rust,editable
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
// On définit nos propres types d'erreur. Ces derniers peuvent être personnalisés pour
// notre gestion des cas.
// Maintenant nous serons capables d'écrire nos propres erreurs et nous reporter
// à leur implémentation.
enum DoubleError {
    // Il n'est pas nécessaire de collecter plus d'informations
    // pour détailler cette erreur.
    EmptyVec,
    // Nous allons nous reporter à l'implémentation couvrant l'erreur de conversion pour ce type.
    // Soumettre des informations supplémentaires nécéssite l'ajout de données pour le type.
    Parse(ParseIntError),
}

// La génération d'une erreur fait abstraction de la manière dont elle est affichée,
// nul besoin de s'occuper de la mécanique sous-jacente.
//
// Notez que nous ne stockons aucune information supplémentaire à propos de l'erreur.
// Cela signifie que nous ne pouvons préciser quelle chaîne de caractères n'a pas pu être
// convertie, sans modifier nos types pour apporter cette information.
impl fmt::Display for DoubleError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match *self {
            DoubleError::EmptyVec => write!(f, "please use a vector with at least one element"),
            // Ceci est un wrapper, donc référrez-vous à l'implémentation de `fmt` respective
            // à chaque type.
            DoubleError::Parse(ref e) => e.fmt(f),
        }
    }
}

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
       // On remplace l'erreur par notre nouveau type.
       .ok_or(DoubleError::EmptyVec)
       .and_then(|s| s.parse::<i32>()
            // On met également à jour le nouveau type d'erreur ici.
            .map_err(DoubleError::Parse)
            .map(|i| 2 * i))
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
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

[`Result`][result] et 
[`io::Result`][io_result].

[result]: https://doc.rust-lang.org/std/result/enum.Result.html
[io_result]: https://doc.rust-lang.org/std/io/type.Result.html
