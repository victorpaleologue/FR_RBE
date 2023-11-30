# L'enum `Option` et la méthode `unwrap`

Dans le dernier exemple, nous avons montré qu'il était possible de mettre en échec le programme quand bon nous semble. Nous disions que notre programme pouvait "paniquer" si la princesse recevait un présent inapproprié - un serpent. Mais qu'en est-il du cas où la princesse attendait un cadeau mais n'en reçoit pas ? Ce cas de figure serait tout bonnement irrecevable, donc inutile d'être géré.

Nous pourrions tester ce cas contre une chaîne de caractères vide (`""`), comme nous l'avons fait avec le serpent. Puisque nous utilisons Rust, laissons plutôt le compilateur gérer les cas où il n'y pas de cadeau.

Une `enum` nommée `Option<T>` dans la bibliothèque standard est utilisée lorsque "l'absence de" est une possibilité. Elle-même est représentée par deux variantes:

* `Some(T)`: Un élément de type `T` a été trouvé;
* `None`: Aucun élément n'a été trouvé.

Ces cas peuvent être explicitement gérés par le biais de `match` ou implicitement avec `unwrap`. La gestion implicite renverra l'élément contenu en cas de succès, sinon un `panic` sera lancé.

Notez que s'il est possible de personnaliser manuellement le message d'erreur de `panic`, ce n'est pas le cas pour `unwrap` qui nous laissera avec des informations moins intelligibles qu'une gestion explicite. Dans l'exemple suivant, la gestion explicite offre un plus grand contrôle sur le résultat tout en permettant l'utilisation de `panic`, si désiré.

```rust,editable
// Le roturier a déjà tout vu et accepte de bon coeur n'importe quel présent.
// Tous les présents sont gérés explicitement en utilisant `match`.
fn give_commoner(gift: Option<&str>) {
    // On définit une action pour chaque cas.
    match gift {
        Some("snake") => println!("Yuck! I'm throwing that snake in a fire."),
        Some(inner)   => println!("{}? How nice.", inner),
        None          => println!("No gift? Oh well."),
    }
}

// Notre précieuse princesse va `panic` à la vue des serpents.
// Tous les présents sont gérés implicitement en utilisant `unwrap`.
fn give_princess(gift: Option<&str>) {
    // `unwrap` renvoie un `panic` lorsqu'il reçoit la variante `None`.
    let inside = gift.unwrap();
    if inside == "snake" { panic!("AAAaaaaa!!!!"); }

    println!("I love {}s!!!!!", inside);
}

fn main() {
    let food  = Some("cabbage");
    let snake = Some("snake");
    let void  = None;

    give_commoner(food);
    give_commoner(snake);
    give_commoner(void);

    let bird = Some("robin");
    let nothing = None;

    give_princess(bird);
    give_princess(nothing);
}

```
