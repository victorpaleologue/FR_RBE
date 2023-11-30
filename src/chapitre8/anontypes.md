# Les types anonymes

Les closures capturent succinctement les variables se trouvant dans les contextes qui les ont engendré. Cela a-t-il des conséquences ? Certainement. Nous remarquons qu'une fonction prête à recevoir une closure doit posséder un paramètre [générique](../chapitre12/genericite.html) pour définir le « régime » de capture que la closure adoptera :

```rust,editable
// `F` doit être générique.
fn apply<F>(f: F)
where
    F: FnOnce(),
{
    f();
}
# fn main() {}

```

Quand une closure est définie, le compilateur crée implicitement une *structure anonyme* pour stocker les variables capturées par la closure. Cette structure implémentera également l'un des traits rencontrés précédemment : `Fn`, `FnMut` ou `FnOnce`. Ce type anonyme est assigné à la variable stockée jusqu'à ce que la closure soit appelée.

Puisque le type créé implicitement est inconnu, son utilisation dans le corps d'une fonction nécessitera un paramètre générique. Cependant, un paramètre `<T>`  dont le trait n'est pas précisé pourrait toujours être ambiguë et rejeté par le compilateur. Il est donc nécessaire de préciser quels services (i.e. `Fn`, `FnMut` ou `FnOnce`) il implémentera.

```rust,editable
// `F` doit implémenter `Fn` pour une closure qui ne prend aucun 
// argument et ne renvoie rien - exactement ce qui est nécessaire 
// pour `print`.
fn apply<F>(f: F) where
    F: Fn() {
    f();
}

fn main() {
    let x = 7;

    // Capture la variable `x` dans une structure anonyme 
    // et implémente `Fn` pour cette dernière. On stocke dans `print`.
    let print = || println!("{}", x);

    apply(print);
}

```

## Voir aussi

[Une analyse complète des closures][analyse], [Fn][Fn], [FnMut][FnMut] et [FnOnce][FnOnce].

[analyse]: http://huonw.github.io/blog/2015/05/finding-closure-in-rust/
[Fn]: http://doc.rust-lang.org/std/ops/trait.Fn.html
[FnMut]: http://doc.rust-lang.org/std/ops/trait.FnMut.html
[FnOnce]: http://doc.rust-lang.org/std/ops/trait.FnOnce.html
