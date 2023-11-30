# Les constantes

Rust possède deux types de constantes qui peuvent être déclarées dans n'importe quel contexte global.

Chacun dispose d'un mot-clé :

* `const`: Une valeur immuable (état par défaut de toute variable);

* `static`: Une variable pouvant être accédée en lecture et (accessoirement) en écriture possédant la « lifetime » `‘static`.

Exception pour les `"chaînes de caractères"` littérales qui peuvent être directement assignées à une variable statique sans modification de votre part, car leur type `&'static str` dispose déjà de la lifetime `‘static`. Tous les autres types de référence doivent être explicitement annotés pour étendre leur durée de vie.

```rust,editable
// Les variables globales sont déclarées en dehors de tous contextes.
static LANGUAGE: &'static str = "Rust";
const  THRESHOLD: i32 = 10;

fn is_big(n: i32) -> bool {
    // Accès à la constante dans une fonction.
    n > THRESHOLD
}

fn main() {
    let n = 16;

    // Accès à la constante dans le fil d'exécution principal.
    println!("This is {}", LANGUAGE);
    println!("The threshold is {}", THRESHOLD);
    println!("{} is {}", n, if is_big(n) { "big" } else { "small" });

    // Erreur! Vous ne pouvez pas modifier une constante.
    // THRESHOLD = 5;
    // FIXME ^ Commentez cette ligne pour voir disparaître
    // le message d'erreur.
}

```

## Voir aussi

La RFC des mot-clés [const et static][const], [la lifetime `'static`][lifetime].

[const]: https://github.com/rust-lang/rfcs/blob/master/text/0246-const-vs-static.md
[lifetime]: ../chapitre13/static.html
