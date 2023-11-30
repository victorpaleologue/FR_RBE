# L'attribut `cfg`

La compilation conditionnelle est possible grâce à deux opérateurs:


1. L'attribut cfg: `#[cfg(…)]`;
2. La macro `cfg!`: `cfg!(…)` en tant qu'expression booléenne.

Tous deux possèdent la même syntaxe :

```rust,editable
// Cette fonction ne sera compilée que sur des distributions Linux.
#[cfg(target_os = "linux")]
fn are_you_on_linux() {
    println!("You are running linux!")
}

// Et cette fonction sera compilée seulement sur des plateformes qui ne sont 
// *pas* des distributions Linux.
#[cfg(not(target_os = "linux"))]
fn are_you_on_linux() {
    println!("You are *not* running linux!")
}

fn main() {
    are_you_on_linux();

    println!("Are you sure?");
    if cfg!(target_os = "linux") {
        println!("Yes. It's definitely linux!");
    } else {
        println!("Yes. It's definitely *not* linux!");
    }
}

```

## Voir aussi

[La référence de l'attribut cfg][cfg], [std::cfg!][cfg_macro] et [les macros][macros].

[cfg]: https://doc.rust-lang.org/reference/attributes.html#conditional-compilation
[cfg_macro]: https://doc.rust-lang.org/std/macro.cfg.html
[macros]: ../chapitre15/systememacro.html
