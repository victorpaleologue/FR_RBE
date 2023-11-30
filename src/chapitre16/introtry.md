# Introduction à `try!`

Parfois nous voulons la simplicité de `unwrap()` sans la possibilité de faire planter le programme. Jusqu'ici, `unwrap()` nous a dévié de ce que nous voulions vraiment: *récupérer la variable*. C'est exactement le but de `try!` que de régler ce souci.

Une fois l'instance `Err` trouvée, il y a deux actions possibles:

1. `panic!` que nous avons choisi d'éviter, si possible, avec `try!`;
2. `return` parce qu'une `Err` ne peut être traitée.

La macro `try!` est *presque*<sup>[1](#note0)</sup> équivalent à la méthode `unwrap()` mais effectue un renvoi prématuré au lieu de planter lorsqu'un conteneur `Err` est récupéré. Voyons comment nous pouvons simplifier l'exemple précédent qui utilisait les combinateurs: 

```rust,editable
// On utilise une `String` comme type d'erreur.
type Result<T> = std::result::Result<T, String>;

fn double_first(vec: Vec<&str>) -> Result<i32> {
    let first = try!(vec.first().ok_or(
        "Please use a vector with at least one element.".to_owned(),
    ));

    let value = try!(first.parse::<i32>().map_err(|e| e.to_string()));

    Ok(2 * value)
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

Notez que, jusqu'ici, nous avons utilisé les `String`s pour les erreurs. Cependant, elles sont quelque peu limitées en tant que type d'erreur. Dans la prochaine section, nous apprendrons à créer des erreurs plus structurées, plus riches, en définissant leur propre type.

<blockquote id="note0">
	<sup>1</sup>. Consultez <a href="../chapitre16/othersuses.html">cette section</a> pour plus de détails.
</blockquote>

## Voir aussi

[`Result`][result] et 
[`io::Result`][io_result].

[result]: https://doc.rust-lang.org/std/result/enum.Result.html
[io_result]: https://doc.rust-lang.org/std/io/type.Result.html
