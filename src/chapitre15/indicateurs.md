# Les indicateurs

Les arguments d'une macro sont préfixés par un `$` et sont typés par le biais d'un indicateur:

```rust,editable
macro_rules! create_function {
    // Cette macro prend un argument possédant l'indicateur `ident` 
    // et créé une fonction nommée `$func_name`.
    // L'indicateur `ident` est utilisé pour les identificateur de variables/fonctions.
    ($func_name:ident) => (
        fn $func_name() {
            // La macro `stringify!` convertit un `ident` en chaîne de caractères.
            println!("You called {:?}()",
                     stringify!($func_name))
        }
    )
}

// On créé les fonctions `foo` et `bar` avec la macro ci-dessus.
create_function!(foo);
create_function!(bar);

macro_rules! print_result {
    // Cette macro prend une expression de type `expr` et 
    // affiche sa représentation sous forme de chaîne de caractères 
    // ainsi que son résultat.
    ($expression:expr) => (
        // `stringify!` va convertir l'expression *telle qu'elle est* dans une chaîne 
        // de caractères.
        println!("{:?} = {:?}",
                 stringify!($expression),
                 $expression)
    )
}

fn main() {
    foo();
    bar();

    print_result!(1u32 + 1);

    // Rappelez-vous que les blocs sont également des expressions !
    print_result!({
        let x = 1u32;

        x * x + 2 * x - 1
    });
}

```

Voici une liste exhaustive des indicateurs existants:

* `block`;
* `expr`, pour les expressions;
* `ident`, pour les identificateurs de variables et fonctions;
* `item`;
* `pat` (pattern);
* `path`;
* `stmt` (déclaration);
* `token` (token tree);
* `ty` (type).
