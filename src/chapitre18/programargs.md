# Les arguments du programme

Les arguments passés en ligne de commande peuvent être récupérés en utilisant `std::env::args` qui renvoie un itérateur fournissant une `String` pour chaque argument:

```rust,editable
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    // Le premier argument est le chemin à partir duquel le programme 
    // a été appelé.
    println!("My path is {}.", args[0]);

    // Le reste des arguments sont ceux passés en ligne de commande au programme.
    // On appelle le programme comme ceci:
    //  $ ./args arg1 arg2
    println!("I got {:?} arguments: {:?}.", args.len() - 1, &args[1..]);
}

```

```bash
$ ./args 1 2 3
My path is ./args.
I got 3 arguments: ["1", "2", "3"].
```
