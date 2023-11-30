# Les closures passées en paramètres

Alors que Rust se charge de choisir, pour les closures, la manière de capturer les variables sans forcer le typage, lorsque c'est possible, cette ambiguïté n'est pas permise au sein des fonctions. Lorsqu'une closure est passée en paramètre à une fonction, le type de ses paramètres ainsi que celui de sa valeur de retour doivent être précisés en utilisant des traits. Dans l'ordre du plus restrictif au plus « laxiste » :

1. `Fn` : La closure capture par référence (`&T`) ;
2. `FnMut` : La closure capture par référence mutable (`&mut T`) ;
3. `FnOnce` : La closure capture par valeur (`T`).

En se fiant au contexte, le compilateur va capturer les variables en privilégiant le « régime » le moins restrictif possible.

Par exemple, prenez un paramètre typé avec le trait `FnOnce`. Cela signifie que la closure *peut* capturer ses variables par référence `&T`, référence mutable `&mut T`, ou valeur `T` mais le compilateur reste encore le seul juge quant au régime à adopter, en fonction du contexte.

C'est pourquoi si un transfert (`move`) est possible alors n'importe quel type d'emprunts devrait être possible, notez que l'inverse n'est pas vrai. Si le paramètre est typé `Fn` alors les captures par référence mutable `&mut T` ou par valeur `T` ne sont pas permises.

Dans l'exemple suivant, essayez de modifier le type de capture (i.e. `Fn`, `FnMut` et `FnOnce`) pour voir ce qu'il se passe :

```rust,editable
// Une fonction qui prend une closure en paramètre et appelle cette dernière.
fn apply<F>(f: F) where
    // La closure ne prend rien et ne renvoie rien.
    F: FnOnce() {
    // ^ TODO: Essayez de remplacer ce trait par `Fn` ou `FnMut`.

    f();
}

// Une fonction qui prend une closure en paramètre et renvoie un entier
// de type `i32`.
fn apply_to_3<F>(f: F) -> i32 where
    // La closure prend en paramètre un `i32` et renvoie 
    // un `i32`.
    F: Fn(i32) -> i32 {

    f(3)
}

fn main() {
    use std::mem;

    let greeting = "hello";
    // Un type qui ne peut pas être copié.
    // `to_owned` crée une ressource dont 
    // l'assignation `farewell` sera responsable, à partir d'une ressource empruntée.
    let mut farewell = "goodbye".to_owned();

    // Capture deux variables: `greeting` par référence et 
    // `farewell` par valeur.
    let diary = || {
        // `greeting` est capturé par référence: requiert `Fn`.
        println!("I said {}.", greeting);

        // Le fait de modifier `farewell` rend obligatoire 
        // la capture par référence mutable, le compilateur choisira 
        // donc `FnMut`.
        farewell.push_str("!!!");
        println!("Then I screamed {}.", farewell);
        println!("Now I can sleep. zzzzz");

        // Appeler manuellement la fonction `drop` nécessite 
        // désormais de capturer par valeur `farewell`, le compilateur 
        // choisira alors `FnOnce`.
        mem::drop(farewell);
    };

    // On appelle la fonction qui prend en paramètre la closure.
    apply(diary);

    // `double` satisfait les conditions du trait soumis à `apply_to_3`.
    let double = |x| 2 * x;

    println!("3 doubled: {}", apply_to_3(double));
}

```

## Voir aussi

La fonction [std::mem::drop][drop] et les traits [Fn][Fn], [FnMut][FnMut] et [FnOnce][FnOnce].

[drop]: http://doc.rust-lang.org/std/mem/fn.drop.html
[Fn]: http://doc.rust-lang.org/std/ops/trait.Fn.html
[FnMut]: http://doc.rust-lang.org/std/ops/trait.FnMut.html
[FnOnce]: http://doc.rust-lang.org/std/ops/trait.FnOnce.html
