# D'autres cas d'utilisation de `try!`

Vous avez remarqué, dans l'exemple précédent, que notre réaction immédiate à l'appel de `parse` "était" de passer l'erreur de la bibliothèque dans notre nouveau type:

```rust,ignore
.and_then(|s| s.parse::<i32>()
    .map_err(DoubleError::Parse)
```

Puisque c'est une opération plutôt commune, il ne serait pas inutile qu'elle soit élidée. Hélas, `and_then` n'étant pas suffisamment flexible pour cela, ce n'est pas possible. Nous pouvons, à la place, utiliser `try!`.

La macro `try!` a été précédemment présentée comme permettrant la récupération de la ressource (`unwrap`) ou le renvoi prématuré, si une erreur survient (`return Err(err)`). C'est plus ou moins vrai. En réalité, elle utilise soit `unwrap` soit `return Err(From::from(err))`.  Puisque `From::from` est un utilitaire permettant la conversion entre différents types, cela signifie que si vous utilisez `try!` où l'erreur peut être convertie au type de retour, elle le sera automatiquement.

Ici, nous réécrivons l'exemple précédent en utilisant `try!`. Résultat, la méthode `map_err` disparaîtra lorsque `From::from` sera implémenté pour notre type d'erreur:

```rust,editable
use std::num::ParseIntError;
use std::fmt;

type Result<T> = std::result::Result<T, DoubleError>;

#[derive(Debug)]
enum DoubleError {
    EmptyVec,
    Parse(ParseIntError),
}

// On implémente la conversion du type `ParseIntError` au type `DoubleError`.
// La conversion sera automatiquement appelée par `try!` si une instance `ParseIntError`
// doit être convertie en `DoubleError`.
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

// La même structure qu'avant mais, plutôt que de chaîner les instances `Result` 
// et `Option` tout du long, nous utilisons `try!` pour récupérer immédiatement 
// la valeur contenue.
fn double_first(vec: Vec<&str>) -> Result<i32> {
    // Convertit toujours en `Result` tout en renseignant comment convertir 
    // un `None`.
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

C'est effectivement plus acceptable. Comparé à l'original `panic`, en remplaçant les appels de `unwrap` par `try!` nous conservons une utilisation assez familière, à l'exception que `try!` renvoie les types dans un conteneur `Result`, rendant leur déstructuration plus abstraite.

Notez toutefois que vous ne devriez pas systématiquement gérer les erreurs de cette manière pour remplacer les appels de `unwrap`. Cette méthode de gestion d'erreur a triplé le nombre de lignes de code et ne peut pas être considéré comme "simple" (même si la taille du code n'est pas énorme).

En effet, modifier une bibliothèque de 1000 lignes pour remplacer des appels de `unwrap` et établir une gestion des erreurs plus "propre" pourrait être faisable en une centaine de lignes supplémentaires. En revanche, le recyclage nécessaire en aval ne serait pas évident.

Nombreuses sont les bibliothèques qui pourraient s'en sortir en implémentant seulement `Display` et ajouter `From` comme base pour la gestion. Cependant, pour des bibliothèques plus importantes, l'implémentation de la gestion des erreurs peut répondre à des besoins plus spécifiques.

## Voir aussi

[`From::from`][from] 
et [`try!`][try].

[from]: https://doc.rust-lang.org/std/convert/trait.From.html
[try]: https://doc.rust-lang.org/std/macro.try!.html
