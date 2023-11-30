# Les restrictions

Tout comme les types génériques, les lifetimes (elles-mêmes génériques) utilisent les restrictions. Ici, le caractère `:` a une signification quelque peu différente, mais `+` possède la même fonction. La déclaration se lit comme suit :


1. `T: ‘a` : Toutes les références dans le type `T` doivent, au moins, survivre à la lifetime `‘a` ;
2. `T: Trait + ‘a` : Le type `T` doit implémenter le trait `Trait` et toutes les références doivent survivre à la lifetime `‘a`.

L'exemple ci-dessous illustre les explications précédentes :

```rust,editable
use std::fmt::Debug; // On importe le trait `Debug`.
// Trait avec lequel nous allons filtrer les entrées 
// des fonctions génériques.

#[derive(Debug)]
struct Ref<'a, T: 'a>(&'a T);
// `Ref` contient la référence d'un type générique `T` qui possède 
// une lifetime inconnue nommée `'a`. Toutes les références contenues par 
// le type `T` sont contraintes à survivre à la lifetime `'a`. De plus, 
// la durée de vie de `Ref` ne peut pas excéder la lifetime `'a`.

// Une fonction générique qui affiche le résultat de l'utilisation 
// du trait `Debug`.
fn print<T>(t: T) where
    T: Debug {
    println!("`print`: t is {:?}", t);
}

// Ici, nous avons une référence de type `T` en entrée où 
// `T` implémente le trait `Debug` et toutes les références 
// contenues par le type `T` survivent à la lifetime `'a`. La lifetime 
// `'a` doit survivre à l'appel de la fonction.
fn print_ref<'a, T>(t: &'a T) where
    T: Debug + 'a {
    println!("`print_ref`: t is {:?}", t);
}

fn main() {
    let x = 7;
    let ref_x = Ref(&x);

    print_ref(&ref_x);
    print(ref_x);
}

```

## Voir aussi

[La généricité][genericite], [les restrictions][bounds] et [les restrictions multiples][mult_bounds].

[genericite]: ../chapitre12/genericite.html
[bounds]: ../chapitre12/restrictions.html
[mult_bounds]: ../chapitre12/restrictionsmultiples.html
