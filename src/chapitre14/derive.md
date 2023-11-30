# L'attribut Derive

Le compilateur est capable de fournir de simples implémentations pour cetains traits par le biais de [l'attribut][attribute] `#[derive]`. 
Ces traits peuvent toujours être implémentés manuellement si un traitement plus complexe est attendu.

Voici une liste de traits pouvant être dérivés:

* Les traits de comparaison: [`Eq`][eq], [`PartialEq`][partial_eq], [`Ord`][ord], [`PartialOrd`][partial_ord];
* [`Clone`][clone], pour créer une instance (`T`) à partir d'une référence (`&T`) par copie;
* [`Copy`][copy], pour permettre à un type d'être copié plutôt que transféré;
* [`Hash`][hash], pour générer un hash depuis `&T`;
* [`Debug`][debug], pour formater une valeur en utilisant le formatteur `{:?}`.

```rust,editable
// `Centimeters` est un tuple qui peut être comparé.
#[derive(PartialEq, PartialOrd)]
struct Centimeters(f64);

// `Inches` est un tuple qui peut être affiché.
#[derive(Debug)]
struct Inches(i32);

impl Inches {
    fn to_centimeters(&self) -> Centimeters {
        let &Inches(inches) = self;

        Centimeters(inches as f64 * 2.54)
    }
}

// `Seconds` est un tuple ne possédant aucun attribut.
struct Seconds(i32);

fn main() {
    let _one_second = Seconds(1);

    // Erreur: `Seconds` ne peut pas être affiché; Il n'implémente pas le trait `Debug`.
    // println!("One second looks like: {:?}", _one_second);
    // TODO ^ Essayez de décommenter cette ligne.

    // Erreur: `Seconds` ne peut pas être comparé; Il n'implémente pas le trait `PartialEq`.
    // let _this_is_true = (_one_second == _one_second);
    // TODO ^ Essayez de décommenter cette ligne.

    let foot = Inches(12);

    println!("One foot equals {:?}", foot);

    let meter = Centimeters(100.0);

    let cmp =
        if foot.to_centimeters() < meter {
            "smaller"
        } else {
            "bigger"
        };

    println!("One foot is {} than one meter.", cmp);
}

```

## Voir aussi

[Derive][derive].

[attribute]: ../chapitre11/attributes.html
[eq]: https://doc.rust-lang.org/std/cmp/trait.Eq.html
[partial_eq]: https://doc.rust-lang.org/std/cmp/trait.PartialEq.html
[ord]: https://doc.rust-lang.org/std/cmp/trait.Ord.html
[partial_ord]: https://doc.rust-lang.org/std/cmp/trait.PartialOrd.html
[clone]: https://doc.rust-lang.org/std/clone/trait.Clone.html
[copy]: https://doc.rust-lang.org/core/marker/trait.Copy.html
[hash]: https://doc.rust-lang.org/std/hash/trait.Hash.html
[debug]: https://doc.rust-lang.org/std/fmt/trait.Debug.html
[derive]: https://doc.rust-lang.org/reference/attributes.html#derive
