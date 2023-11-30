# Multiples types d'erreur

Les exemples précédents ont toujours été très basiques; Les (instances de) `Result` interagissent avec d'autres (instances de) `Result` et les `Option`s interagissent avec d'autres `Option`s.

Parfois une instance d'`Option` a besoin d'interagir avec un `Result` ou encore un `Result<T, Error1>` devant interagir avec un `Result<T, Error2>`. Dans ces cas, nous souhaitons gérer nos différents types de manière à pouvoir interagir simplement avec eux.

Dans le code suivant, deux instances de la méthode `unwrap()` génèrent deux types d'erreur différents. `Vec::first` renvoie une instance de `Option`, alors que `parse::<i32>` renvoie une instance de `Result<i32, ParseIntError>`:

```rust,editable
fn double_first(vec: Vec<&str>) -> i32 {
    let first = vec.first().unwrap(); // Génère la première erreur.
    2 * first.parse::<i32>().unwrap() // Génère la seconde erreur.
}

fn main() {
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    println!("The first doubled is {}", double_first(empty));
    // Erreur 1: Le vecteur passé en entrée est vide.

    println!("The first doubled is {}", double_first(strings));
    // Erreur 2: L'élément ne peut pas être converti en nombre.
}

```

En utilisant notre connaissance des combinateurs, nous pouvons réécrire ce qu'il y a au-dessus pour gérer explicitement les erreurs. Puisque deux types différents peuvent être rencontrés, nous nous devons de les convertir en un type commun tel que `String`.

Pour ce faire, nous convertissons les instances d'`Option` et de `Result` en `Result`s puis nous convertissons leurs erreurs respectives sous le même type:

```rust,editable
// Nous utiliserons `String` en tant que type d'erreur.
type Result<T> = std::result::Result<T, String>;

fn double_first(vec: Vec<&str>) -> Result<i32> {
    vec.first()
       // On convertit l'`Option` en un `Result` s'il y a une valeur.
       // Autrement, on fournit une instance `Err` contenant la `String`.
       .ok_or("Please use a vector with at least one element.".to_owned())
       .and_then(|s| s.parse::<i32>()
                      // On convertit n'importe quelle erreur, générée par `parse`,
                      // en `String`.
                      .map_err(|e| e.to_string())
                      // `Result<T, String>` est le nouveau type de valeur,
                      // et nous pouvons doubler le nombre se trouvant dans le conteneur.
                      .map(|i| 2 * i))
}

fn print(result: Result<i32>) {
    match result {
        Ok(n)  => println!("The first doubled is {}", n),
        Err(e) => println!("Error: {}", e),
    }
}

fn main() {
    let empty = vec![];
    let strings = vec!["tofu", "93", "18"];

    print(double_first(empty));
    print(double_first(strings));
}

```

Dans la prochaine section, nous allons voir une méthode pour la gestion explicite de ces erreurs.

## Voir aussi

[`Option::ok_or`][ok_or], 
[`Result::map_err`][map_err].

[ok_or]: https://doc.rust-lang.org/std/option/enum.Option.html#method.ok_or
[map_err]: https://doc.rust-lang.org/std/result/enum.Result.html#method.map_err
