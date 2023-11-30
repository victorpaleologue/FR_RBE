# Les traits

Bien entendu, les traits peuvent également être génériques. Dans cette section, nous allons en créer un qui ré-implémente le trait `Drop` qui proposera une méthode générique qui aura pour fonction de libérer l'instance qui l'appelle ainsi qu'un paramètre passé.

```rust,editable
// Types non-copiables.
struct Empty;
struct Null;

// Un trait générique qui reçoit un type générique `T`.
trait DoubleDrop<T> {
    // On déclare une méthode qui sera implémentée par la structure 
    // appelante (caller) et prendra un paramètre `T` en entrée mais n'en fera rien (juste le libérer). 
    fn double_drop(self, _: T);
}

// On implémente `DoubleDrop<T>` pour n'importe quel paramètre `T` et 
// n'importe quelle structure appelante (`U`).
impl<T, U> DoubleDrop<T> for U {
    // Cette méthode prend "possession" des deux paramètres (`U` et `T`),
    // et sont donc tous deux libérés.
    fn double_drop(self, _: T) {}
}

fn main() {
    let empty = Empty;
    let null  = Null;
    
    // `empty` et `null` sont désalloués.
    empty.double_drop(null);

    // empty;
    // null;
    // ^ TODO: Essayez de décommenter ces lignes.
}

```

## Voir aussi

[La documentation du trait Drop][drop], [le chapitre sur les structures][struct] et [les traits][traits].

[drop]: http://doc.rust-lang.org/std/ops/trait.Drop.html
[struct]: ../chapitre3/struct.html
[traits]: ../chapitre14/traits.html
