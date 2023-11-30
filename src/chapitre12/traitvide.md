# Exemple d'utilisation : Traits sans services

Puisqu'il est possible d'imposer des conditions aux types génériques grâce aux traits, même si ces derniers ne possèdent aucune fonctionnalité (i.e. aucun service, aucune méthode), il est toujours possible de vous en servir comme simple « filtre ». `Eq` et `Ord` font partie de ces traits « vides » fournis par la bibliothèque standard.

```rust,editable
struct Cardinal;
struct BlueJay;
struct Turkey;

trait Red {}
trait Blue {}

impl Red for Cardinal {}
impl Blue for BlueJay {}

// Ces fonctions ne prendront en entrée que des ressources 
// ayant implémenté les traits `Red` ou `Blue`.
// Le fait que ces derniers soient vides n'a que peu d'importance.
fn red<T: Red>(_: &T)   -> &'static str { "red" }
fn blue<T: Blue>(_: &T) -> &'static str { "blue" }

fn main() {
    let cardinal = Cardinal;
    let blue_jay = BlueJay;
    let _turkey   = Turkey;

    // La fonction `red()` ne fonctionnera pas sur une instance 
    // de la structure `BlueJay`, et vice versa, à cause des 
    // restrictions imposées par les fonctions (i.e. `red()` et `blue()`).
    println!("A cardinal is {}", red(&cardinal));
    println!("A blue jay is {}", blue(&blue_jay));
    //println!("A turkey is {}", red(&_turkey));
    // ^ TODO: Essayez de décommenter cette ligne.
}

```

## Voir aussi

La documentation du trait [Eq][eq], la documentation du trait [Ord][ord] et [les traits][traits].

[eq]: http://doc.rust-lang.org/std/cmp/trait.Eq.html
[ord]: http://doc.rust-lang.org/std/cmp/trait.Ord.html
[traits]: ../chapitre14/traits.html
