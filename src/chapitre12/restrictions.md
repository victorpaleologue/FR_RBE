# Les restrictions

Lorsque nous travaillons avec la généricité, il est courant d'assigner une « restriction » à un type générique pour spécifier quel trait il doit implémenter. Dans l'exemple suivant, nous utilisons le trait `Display` pour afficher quelque chose en console, il est alors assigné au type `T`. Autrement dit, `T` doit implémenter `Display`.

```rust,ignore
// On déclare une fonction nommée `printer` qui prend, en entrée, 
// un type générique `T` qui doit implémenter le trait `Display`.
fn printer<T: Display>(t: T) {
    println!("{}", t);
}
```

Les ressources passées en paramètre sont toutes soumises à ces restrictions et doivent forcément remplir les conditions:

```rust,ignore
struct S<T: Display>(T);

// Erreur! `Vec<T>` n'implémente pas le trait `Display`.
let s = S(vec![1]);
```

Les instances des types génériques peuvent également accéder aux méthodes appartenant au(x) trait(s) présent(s) dans les restrictions du type. Par exemple :

```rust,editable
// Un trait qui implémente le marqueur `{:?}`.
use std::fmt::Debug;

trait HasArea {
    fn area(&self) -> f64;
}

impl HasArea for Rectangle {
    fn area(&self) -> f64 { self.length * self.height }
}

#[derive(Debug)]
struct Rectangle { length: f64, height: f64 }
#[allow(dead_code)]
struct Triangle  { length: f64, height: f64 }

// Le type générique `T` doit implémenter le trait `Debug`.
// Qu'importe le type de `T`, cela fonctionnera.
fn print_debug<T: Debug>(t: &T) {
    println!("{:?}", t);
}

// `T` doit implémenter le trait `HasArea`. N'importe quelle 
// structure remplissant les conditions d'entrée peut accéder 
// à la méthode `area` du trait `HasArea`.
fn area<T: HasArea>(t: &T) -> f64 { t.area() }

fn main() {
    let rectangle = Rectangle { length: 3.0, height: 4.0 };
    let _triangle = Triangle  { length: 3.0, height: 4.0 };

    print_debug(&rectangle);
    println!("Area: {}", area(&rectangle));

    // print_debug(&_triangle);
    // println!("Area: {}", area(&_triangle));
    // ^ TODO: Essayez de décommenter ces lignes.
    // | Erreur: N'implémente pas l'un de ces traits: `Debug` ou `HasArea`.
}

```

Les conditions d'entrée pour les paramètres génériques peuvent également être spécifiées en utilisant le mot-clé [where](../chapitre12/where.html), les rendant plus explicites, plus lisibles.

## Voir aussi

Les traits dédiés à l'affichage et le formatage [std::fmt](../chapitre1/affichage.html), [les structures](../chapitre3/struct.html) et [les traits](../chapitre14/traits.html).
