# Les énumérations

Le mot-clé `enum` permet la création d'un type qui peut disposer d'une ou plusieurs variantes de lui-même. Toutes [les variantes des structures][struct] sont valides dans une énumération.

```rust,editable
// Masque les avertissements du compilateur lorsqu'il y a
// du code mort présent dans votre code.
#![allow(dead_code)]

// On créé une énumération pour définir des "classes" de personnes.
// Notez que chaque variante de l'énumération est indépendante de l'autre. 
// Aucune n'est égale à l'autre: `Engineer != Scientist` et 
// `Height(i32) != Weight(i32)`. 
enum Person {
    // Une variante peut être une structure unitaire,
    Engineer,
    Scientist,
    // un tuple
    Height(i32),
    Weight(i32),
    // ou simplement une structure classique.
    Info { name: String, height: i32 }
}

// Prend une variante de l'énumération `Person` en argument et 
// ne renvoie rien.
fn inspect(p: Person) {
    // En utilisant une énumération, vous devez analyser tous les cas 
    // possibles (obligatoire).
    // Le pattern matching permet de les couvrir efficacement.
    match p {
        Person::Engineer  => println!("Is an engineer!"),
        Person::Scientist => println!("Is a scientist!"),
        // On récupère l'attribut de l'instance `Height`.
        Person::Height(i) => println!("Has a height of {}.", i),
        Person::Weight(i) => println!("Has a weight of {}.", i),
        // Destructure `Info` into `name` and `height`.
        // On récupère les attributs 
        Person::Info { name, height } => {
            println!("{} is {} tall!", name, height);
        },
    }
}

fn main() {
    let person   = Person::Height(18);
    let amira    = Person::Weight(10);
    // La fonction `to_owned()` créé une instance de la structure `String` 
    // possédée par l'assignation `name` à partir d'une slice (i.e. &str).
    let dave     = Person::Info { name: "Dave".to_owned(), height: 72 };
    let rebecca  = Person::Scientist;
    let rohan    = Person::Engineer;

    inspect(person);
    inspect(amira);
    inspect(dave);
    inspect(rebecca);
    inspect(rohan);
}

```

## Voir aussi

[Les attributs][attributes], [le mot-clé match][match], [le mot-clé fn][fn], [les chaînes de caractères][string].

[struct]: ../chapitre3/struct.html
[attributes]: ../chapitre11/attributes.html
[match]: ../chapitre7/match.html
[fn]: ../chapitre8/fonctions.html
[string]: ../chapitre17/stringwrapper.html
