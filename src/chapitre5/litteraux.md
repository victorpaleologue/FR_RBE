# Les littéraux

Les littéraux numériques peuvent être typés en suffixant le littéral avec son type. Par exemple, pour préciser que le littéral `42` devrait posséder le type `i32`, nous écrirons `42i32`.

Le type des littéraux numériques qui ne sont pas suffixés va dépendre du contexte dans lequel ils sont utilisés. S'il n'y a aucune contrainte (i.e. si rien ne force la valeur à être codée sur un nombre de bits bien précis), le compilateur utilisera le type `i32` pour les entiers et `f64` pour les nombres réels.

```rust,editable
fn main() {
    // Ces littéraux sont suffixés, leurs types sont connus à l'initialisation.
    let x = 1u8;
    let y = 2u32;
    let z = 3f32;

    // Ces littéraux ne sont pas suffixés, leurs types dépendent du contexte.
    let i = 1;
    let f = 1.0;

    // La fonction `size_of_val` renvoie la taille d'une variable en octets.
    println!("La taille de `x` en octets: {}", std::mem::size_of_val(&x));
    println!("La taille de `y` en octets: {}", std::mem::size_of_val(&y));
    println!("La taille de `z` en octets: {}", std::mem::size_of_val(&z));
    println!("La taille de `i` en octets: {}", std::mem::size_of_val(&i));
    println!("La taille de `f` en octets: {}", std::mem::size_of_val(&f));
}
```

Certains concepts présentés dans l'exemple ci-dessus n'ont pas encore été abordés. Pour les plus impatients, voici une courte explication :


*  `fun(&foo)` : Cette syntaxe représente le passage d'un paramètre par référence plutôt que par valeur (i.e. `fun(foo)`). Pour plus d'informations, voir [le chapitre du système d'emprunts][borrowing].

 
* `std::mem::size_of_val` est une fonction mais appelée avec son chemin absolu. Le code peut être divisé et organisé en plusieurs briques logiques nommées *modules*. Pour le cas de la fonction `size_of_val`, elle se trouve dans le module `mem`, lui-même se trouvant dans le paquet `std`. Pour plus d'informations voir [les modules][mods] et/ou [les « crates »][crates].

[borrowing]: ../chapitre13/borrowing.html
[mods]: ../chapitre9/module.html
[crates]: ../chapitre10/crate.html
