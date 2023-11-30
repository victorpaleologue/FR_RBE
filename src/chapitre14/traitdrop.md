# Le trait Drop

Le trait [Drop](https://doc.rust-lang.org/std/ops/trait.Drop.html) ne possède qu'une seule méthode: `drop`; cette dernière est automatiquement appelée lorsqu'un objet sort du contexte. La fonction principale du trait `Drop` est de libérer les ressources que les instances, du type ayant implémenté le trait, possèdent.

`Box`, `Vec`, `String`, `File` et `Process` sont autant d'exemples de types qui implémentent le trait `Drop` pour libérer leurs ressources. Le trait `Drop` peut également être implémenté manuellement pour répondre aux besoins de vos propres types.

Dans l'exemple suivant, nous affichons quelque chose dans la console à partir de la méthode `drop` pour notifier chaque appel.

```rust,editable
struct Droppable {
    name: &'static str,
}

// Implémentation basique de `drop` qui affiche un message dans la console.
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // block A
    {
        let _b = Droppable { name: "b" };

        // block B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    // La variable peut être libérée manuellement en utilisant la fonction `(std::mem::)drop`.
    drop(_a);
    // TODO ^ Essayez de commenter cette ligne.

    println!("end of the main function");

    // `_a` ne *sera pas* libérée une seconde fois ici puisque nous l'avons déjà fait 
    // plus haut, manuellement.
}

```
