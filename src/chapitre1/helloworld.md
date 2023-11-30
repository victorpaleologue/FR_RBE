# Hello World

Voici le code source d’un traditionnel « Hello World ».

```rust,editable
// Ceci est un commentaire, et sera ignoré par le compilateur.

// Ceci est la fonction principale
fn main() {
// Toutes les déclarations se trouvant dans le corps de la fonction 
// seront exécutées lorsque le binaire est exécuté.
// Afficher du texte dans la console.
    println!("Hello World!");
}
```

`println!` est une macro qui affiche du texte sur la console.

Un binaire peut être généré en utilisant le compilateur Rust : `rustc`.

```bash
$ rustc hello.rs
```

`rustc` va produire un binaire nommé « hello » qui pourra être exécuté :


```bash
$ ./hello
Hello World!
```

## Activité

Cliquez sur le bouton « Run » en début de section pour visualiser le résultat présenté. Ensuite, ajoutez une nouvelle ligne qui permettra de visualiser le résultat ci-dessous :

```text
Hello World!
I'm a Rustacean!
```
