# Le RAII

En Rust, les variables ne stockent pas seulement leurs données dans la pile : Elles sont responsables de leurs ressources (e.g. le conteneur `Box<T>` possède, alloue de la mémoire dans le tas). Rust imposant l'approche du RAII, lorsqu'un objet sort du contexte, son destructeur est appelé et les ressources, possédées par l'objet, sont libérées.

Ce fonctionnement prévient les problèmes de fuites mémoire et nous dispense donc de gérer manuellement la mémoire. Voici un exemple :

```rust,editable
// Dans le fichier raii.rs
fn create_box() {
    // Allocation d'un entier dans le tas.
    let _box1 = Box::new(3i32);

    // `_box1` est détruit ici, et la mémoire est libérée.
}

fn main() {
    // Allocation d'un entier dans le tas.
    let _box2 = Box::new(5i32);

    // Contexte imbriqué:
    {
        // Allocation d'un entier dans le tas.
        let _box3 = Box::new(4i32);

        // `_box3` est détruit ici, et la mémoire est libérée.
    }

    // On créé ici un grand nombre de "box" juste pour l'exemple.
    // Il n'y a pas besoin de libérer manuellement la mémoire !
    for _ in 0u32..1_000 {
        create_box();
    }

    // `_box2` est détruit ici, et la mémoire est libérée.
}

```

Bien entendu, vous pouvez vérifier par vous-même si des fuites sont présentes en utilisant [valgrind][valgrind] :

```bash
$ rustc raii.rs && valgrind ./raii
==26873== Memcheck, a memory error detector
==26873== Copyright (C) 2002-2013, and GNU GPL'd, by Julian Seward et al.
==26873== Using Valgrind-3.9.0 and LibVEX; rerun with -h for copyright info
==26873== Command: ./raii
==26873==
==26873==
==26873== HEAP SUMMARY:
==26873==     in use at exit: 0 bytes in 0 blocks
==26873==   total heap usage: 1,013 allocs, 1,013 frees, 8,696 bytes allocated
==26873==
==26873== All heap blocks were freed -- no leaks are possible
==26873==
==26873== For counts of detected and suppressed errors, rerun with: -v
==26873== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 2 from 2)
```

## Voir aussi

[Box][box].

[valgrind]: http://valgrind.org/info/
[box]: ../chapitre17/boxpiletas.html
