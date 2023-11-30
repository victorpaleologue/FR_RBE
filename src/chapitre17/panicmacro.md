# La macro `panic!`

La macro `panic!` peut être utilisée pour générer un plantage et dérouler la pile. Pendant le déroulement de la pile, l'exécution prendra soin de libérer toutes les ressources *possédées* par le fil d'exécution en appelant le destructeur de chaque objet.

Puisque nous interagissons avec nos programmes en n'utilisant qu'un seul fil d'exécution, `panic!` renverra un message d'erreur puis mettra un terme à l'exécution.

```rust,editable
// Ré-implémentation de la division d'entiers (/).
fn division(dividend: i32, divisor: i32) -> i32 {
    if divisor == 0 {
        // La division par zéro fait planter le thread courant.
        panic!("division by zero");
    } else {
        dividend / divisor
    }
}


fn main() {
    // Entier alloué dans le tas.
    let _x = Box::new(0i32);

    // Cette opération va déclencher la procédure d'abandon.
    division(3, 0);

    println!("This point won't be reached!");

    // `_x` devrait être détruit à ce niveau.
}

```

Vérifions que la macro `panic!` ne cause aucune fuite mémoire.

```text
$ rustc panic.rs && valgrind ./panic
==4401== Memcheck, a memory error detector
==4401== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==4401== Using Valgrind-3.10.0.SVN and LibVEX; rerun with -h for copyright info
==4401== Command: ./panic
==4401== 
thread '<main>' panicked at 'division by zero', panic.rs:5
==4401== 
==4401== HEAP SUMMARY:
==4401==     in use at exit: 0 bytes in 0 blocks
==4401==   total heap usage: 18 allocs, 18 frees, 1,648 bytes allocated
==4401== 
==4401== All heap blocks were freed -- no leaks are possible
==4401== 
==4401== For counts of detected and suppressed errors, rerun with: -v
==4401== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
```
