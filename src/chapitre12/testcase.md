# Exemple d'utilisation : Petite précision

Nous allons créer une méthode chargée de calculer dans deux unités de mesure différentes ([le pied][pied] et [le millimètre][mm]) et nous implémenterons le `trait` `Add` avec un type générique fantôme. Voici l'implémentation du `trait` `Add` :

```rust,ignore
// Cette implémentation devrait imposer: `Self + RHS = Output`
// où `Self` est la valeur par défaut de `RHS` si elle n'est pas spécifiée 
// dans l'implémentation.

pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` doit être de type `T<U>` pour que `T<U> + T<U> = T<U>`.
impl<U> Add for T<U> {
    type Output = T<U>;
    ...
}
```

Voici l'implémentation complète :

```rust,editable
use std::ops::Add;
use std::marker::PhantomData;

/// On créé des énumérations vides pour déclarer le type des 
// unités de mesures.
#[derive(Debug, Clone, Copy)]
enum Inch {}
#[derive(Debug, Clone, Copy)]
enum Mm {}

/// `Length` est une structure prenant un type générique fantôme `Unit`,
/// `f64` implémente déjà les traits `Clone` et `Copy`.
#[derive(Debug, Clone, Copy)]
struct Length<Unit>(f64, PhantomData<Unit>);

/// Le trait `Add` définit le comportement de l'opérateur `+`.
impl<Unit> Add for Length<Unit> {
     type Output = Length<Unit>;

    // La méthode add() renvoie une nouvelle instance de la 
    // structure `Length` contenant la somme.
    fn add(self, rhs: Length<Unit>) -> Length<Unit> {
        // L'opérateur `+` appelle l'implémentation 
        // du trait `Add` pour le type `f64`.
        Length(self.0 + rhs.0, PhantomData)
    }
}

fn main() {
    // On initialise `one_foot` pour avoir un type générique fantôme `Inch`.
    // Ce "fantôme" sert de marqueur et classe cette instance dans 
    // l'unité de mesure "Pied".
    let one_foot:  Length<Inch> = Length(12.0, PhantomData);
    // On initialise `one_meter` pour avoir un type générique fantôme `Mm`.
    // Ce "fantôme" sert de marqueur et classe cette instance dans 
    // l'unité de mesure "Millimètre".
    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);

    // L'opérateur `+` appelle la méthode `add()` que nous avons 
    // précédemment implémentée pour `Length<Unit>`.
    // Maintenant que `Length` implémente le trait `Copy`, `add()` ne 
    // prend pas possession (ne consomme pas) `one_foot` et `one_meter` mais 
    // les copie dans `self` et `rhs`.
    let two_feet = one_foot + one_foot;
    let two_meters = one_meter + one_meter;

    // L'addition fonctionne.
    println!("one foot + one_foot = {:?} in", two_feet.0);
    println!("one meter + one_meter = {:?} mm", two_meters.0);

    // Les opérations illogiques échouent comme prévu:
    // Erreur à la compilation: mismatched type.
    // let one_feter = one_foot + one_meter;
}

```

## Voir aussi

[Le système d'emprunts][emprunts], [les restrictions][bounds], [les énumérations][enums], [impl et self][impl_n_self], [la surcharge des opérateurs][overloading], [le pattern `ref`][ref], [les `traits`][traits] et [les tuples][tuples].

[pied]: https://fr.wikipedia.org/wiki/Pied_%28unité%29
[mm]: https://fr.wikipedia.org/wiki/Mètre#Description_des_sous-multiples
[emprunts]: ../chapitre13/borrowing.html
[bounds]: ../chapitre12/restrictions.html
[enums]: ../chapitre3/enum.html
[impl_n_self]: ../chapitre8/methodes.html
[overloading]: ../chapitre14/opoverloading.html
[ref]: ../chapitre13/refpattern.html
[traits]: ../chapitre14/traits.html
[tuples]: ../chapitre3/struct.html
