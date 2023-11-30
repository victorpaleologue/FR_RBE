# Retour prématuré

Dans l'exemple précédent, nous gérions explicitement les erreurs en utilisant les combinateurs. Une autre manière de répondre à cette analyse est d'utiliser une série de `match` et des *retours prématurés*.

Autrement dit, nous pouvons simplement mettre fin à l'exécution de la fonction et renvoyer l'erreur, s'il y en a une. 
Pour certains, cette manière de faire est plus simple à lire et écrire. Voici une nouvelle version de l'exemple précédent, réécrit en utilisant les retours prématurés:

```rust,editable
// On utilise `String` comme type d'erreur.
type Result<T> = std::result::Result<T, String>;

fn double_first(vec: Vec<&str>) -> Result<i32> {
    // On convertit l'`Option` en un `Result` s'il y a une valeur.
    // Autrement, on fournit une instance `Err` contenant la `String`.
    let first = match vec.first() {
        Some(first) => first,
        None => return Err("Please use a vector with at least one element.".to_owned()),
    };

    // On double le nombre dans le conteneur si `parse` fonctionne
    // correctement.
    // Sinon, on convertit n'importe quelle erreur, générée par `parse`,
    // en `String`.
    match first.parse::<i32>() {
        Ok(i) => Ok(2 * i),
        Err(e) => Err(e.to_string()),
    }
}

fn print(result: Result<i32>) {
    match result {
        Ok(n) => println!("The first doubled is {}", n),
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

À ce niveau, nous avons appris à gérer explicitement les erreurs en utilisant les combinateurs et les retours prématurés. Bien que, généralement, nous souhaitons éviter un plantage, la gestion explicite de toutes nos erreurs peut s'avérer relativement lourde.

Dans la section suivante, nous introduirons la macro `try!` pour couvrir les cas où nous souhaitons simplement utiliser `unwrap()` sans faire planter le programme.
