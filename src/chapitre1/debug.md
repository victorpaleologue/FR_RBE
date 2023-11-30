# Debug

Tous les types qui utilisent le formatage des traits du module `std::fmt` doivent en posséder une implémentation pour être affichés.

Les implémentations ne sont fournies automatiquement que pour les types supportés par la bibliothèque standard. Les autres devront l'implémenter « manuellement ».

Pour le trait `fmt::Debug`, rien de plus simple. Tous les types peuvent hériter de son implémentation (i.e. la créer automatiquement, sans intervention de votre part). Ce n'est, en revanche, pas le cas pour le second trait : `fmt::Display`.

```rust,ignore
// Cette structure ne peut être affichée par `fmt::Debug`, 
// ni par `fmt::Display`.
struct UnPrintable(i32);

// L'attribut `derive` créé automatiquement l'implémentation requise 
// pour permettre à cette structure d'être affichée avec `fmt::Debug`.
#[derive(Debug)]
struct DebugPrintable(i32);
```

Également, tous les types de la bibliothèque standard peuvent être automatiquement affichés avec le marqueur `{:?}` :

```rust,editable
// On fait hériter l'implémentation de `fmt::Debug` pour `Structure`.
// `Structure` est une structure qui contient un simple entier de type `i32`.
#[derive(Debug)]
struct Structure(i32);

// On créé une structure nommée `Deep`, que l'on rend également affichable,
// contenant un champ de type `Structure`,
#[derive(Debug)]
struct Deep(Structure);

fn main() {
    // L'affichage avec le marqueur `{:?}` est similaire à `{}`,
    // pour des types standards comme les entiers et les chaînes de caractères.
    println!("{:?} mois dans une année.", 12);
    println!("{1:?} {0:?} est le nom de {actor:?}.",
             "Slater",
             "Christian",
             actor="l'acteur");

    // `Structure` peut être affichée !
    println!("{:?} peut désormais être affichée!", Structure(3));

    // Le problème avec `derive` est que vous n'avez aucun contrôle quant au résultat
    // affiché. Comment faire si je souhaite seulement afficher `7` ?
    println!("{:?} peut désormais être affichée!", Deep(Structure(7)));
}
```

Finalement, `fmt::Debug` permet de rendre un type personnalisé affichable en sacrifiant quelque peu « l'élégance » du résultat. Pour soigner cela, il faudra implémenter soit-même les services du traits `fmt::Display`.

## Voir aussi

[Les attributs][attributes],  [derive][derive], [std::fmt][fmt], [les structures][struct].

[attributes]: https://doc.rust-lang.org/reference.html#attributes
[derive]: ../chapitre14/derive.html
[fmt]: http://doc.rust-lang.org/std/fmt/
[struct]: ../chapitre1/struct.html
