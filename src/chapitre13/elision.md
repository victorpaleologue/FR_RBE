# Annotation implicite

En règle générale, décrire explicitement la durée de vie d'une référence n'est pas nécessaire et nous préférerons passer la main au compilateur, qui se chargera de nous épargner l'écriture des annotations et d'améliorer la lisibilité du code. Ce processus d'annotation implicite se nomme [l'élision][elision]. Il s'agit ici d'omettre volontairement les annotations pour que le compilateur le fasse à notre place. L'élision ne peut être appliquée que lorsqu'un pattern de durée de vie est commun, simple à deviner.

Le code source qui suit présente quelques exemples où nous avons volontairement omis les annotations. Pour une description plus exhaustive du concept d'élision, n'hésitez pas à consulter la section [lifetime elision][link_book] du livre.

```rust,editable
// `elided_input` et `annotated_input` ont fondamentalement la même signature, 
// sauf que la lifetime de l'entrée de la fonction `elided_input` a été omise 
// et ajoutée par le compilateur.
fn elided_input(x: &i32) {
    println!("`elided_input`: {}", x)
}

fn annotated_input<'a>(x: &'a i32) {
    println!("`annotated_input`: {}", x)
}

// Même combat, `elided_pass` et `annotated_pass` possèdent la même signature 
// sauf que la lifetime de `x`, pour la fonction `elided_pass`, a été omise 
// et ajoutée par le compilateur. Annotation implicite.
fn elided_pass(x: &i32) -> &i32 { x }

fn annotated_pass<'a>(x: &'a i32) -> &'a i32 { x }

fn main() {
    let x = 3;

    elided_input(&x);
    annotated_input(&x);

    println!("`elided_pass`: {}", elided_pass(&x));
    println!("`annotated_pass`: {}", annotated_pass(&x));
}

```

## Voir aussi

[Le chapitre du livre sur l'élision][link_book].

[elision]: http://www.linternaute.com/dictionnaire/fr/definition/elision/
[link_book]: https://doc.rust-lang.org/book/lifetimes.html#lifetime-elision
