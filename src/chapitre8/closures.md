# Les closures

Les closures en Rust, également appelées « lambdas », sont des fonctions qui peuvent capturer l'environnement qui les entoure. Par exemple, voici une closure qui capture la variable `x` :

```rust,ignore
|val| val + x
```


La syntaxe ainsi que les capacités des closures les rendent adéquates aux déclarations et utilisations à la volée. Appeler une closure se fait de la même manière qu'une fonction classique. En revanche, les types reçus en entrée (i.e. les types des paramètres passés) et le type de renvoi peuvent être [inférés][inference] et les identificateurs des paramètres *doivent* être spécifiés.

D'autres caractéristiques spécifiques aux closures :

* L'utilisation du couple `||` plutôt que de `()` pour entourer les paramètres;
* La délimitation `{}` du corps de la closure optionnelle pour une seule expression (sinon obligatoire);
* La capacité à capturer des variables appartenant au contexte dans lequel la closure est imbriquée.

```rust,editable
fn main() {
    // Incrémentation avec les closures et fonctions.
    fn  function            (i: i32) -> i32 { i + 1 }

    // Les closures sont anonymes, ici nous assignons leurs références.
    // Les closures sont typées de la même manière qu'une fonction classique
    // mais le typage est optionnel. Chaque version (raccourcie et non-raccourcie)
    // est assignée à un identificateur approprié.
    let closure_annotated = |i: i32| -> i32 { i + 1 };
    let closure_inferred  = |i     |          i + 1  ;

    let i = 1;
    // Appelle la fonction et les closures.
    println!("function: {}", function(i));
    println!("closure_annotated: {}", closure_annotated(i));
    println!("closure_inferred: {}", closure_inferred(i));

    // Une closure qui ne prend aucun argument et renvoie un 
    // entier de type `i32`.
    // Le type de renvoi est inféré.
    let one = || 1;
    println!("closure returning one: {}", one());

}

```

[inference]: https://fr.wikipedia.org/wiki/Inférence_de_types
