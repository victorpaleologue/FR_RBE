# Fonctions passées en paramètres

Les closures peuvent être soumises en entrée aux fonctions, mais vous pourriez vous demander si nous pouvons faire de même avec d'autres fonctions. C'est le cas ! Si vous déclarez une fonction qui prend une closure en paramètre alors n'importe quelle fonction implémentant les traits requis peut être passée en paramètre.

```rust,editable
// On déclare une fonction qui prend l'argument générique `F`
// délimité par le trait `Fn` et appelle la fonction (ou closure).
fn call_me<F: Fn()>(f: F) {
    f();
}

// On déclare une fonction qui satisfait la délimitation (hériter de `Fn`).
fn function() {
    println!("I'm a function!");
}

fn main() {
    // On déclare une closure qui satisfait la délimitation (hériter de `Fn`).
    let closure = || println!("I'm a closure!");

    call_me(closure);
    call_me(function);
}

```

## Voir aussi

[Fn][Fn], [FnMut][FnMut] et [FnOnce][FnOnce].

[Fn]: http://doc.rust-lang.org/std/ops/trait.Fn.html
[FnMut]: http://doc.rust-lang.org/std/ops/trait.FnMut.html
[FnOnce]: http://doc.rust-lang.org/std/ops/trait.FnOnce.html
