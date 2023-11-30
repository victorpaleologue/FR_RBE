# La clause `where`

Une restriction peut également être explicitée par la clause `where`. Cette dernière se trouvera alors avant l'accolade ouvrante (`{`) plutôt qu'à la déclaration du type(e.g. `<A: Display, B: Debug, ...>`). Avec `where`, vous pouvez également ajouter arbitrairement d'autres types en plus de spécifier les traits à implémenter pour les types génériques.

`where` peut être utile dans plusieurs cas :


* Lorsque vous ajoutez des restrictions aux types génériques, facilitant la lecture :

```rust,ignore
impl <A: TraitB + TraitC, D: TraitE + TraitF> MyTrait<A, D> for YourType {}

// Les restrictions sont explicitées 
// par la condition `where`.
impl <A, D> MyTrait<A, D> for YourType where
    A: TraitB + TraitC,
    D: TraitE + TraitF {}
```

* Lorsque d'autres types sont ajoutés aux restrictions :

```rust,editable
use std::fmt::{Debug, Formatter, Result};

trait PrintInOption {
    fn print_in_option(self);
}

// Parce que nous pourrions modifier la restriction sans spécifier le 
// conteneur `T: Debug` ou adopter une autre approche,
// il est nécessaire d'utiliser la condition `where`: 
impl<T> PrintInOption for T where
    Option<T>: Debug{
    // Nous spécifions la restriction de type `Option<T>: Debug` parce que 
    // c'est ce que nous souhaitons afficher. Faire autrement pourrait nous 
    // induire en erreur quant au type de restriction à spécifier.
    fn print_in_option(self) {
        println!("{:?}", Some(self)); 
    }
}

fn main() {
    let vec = vec![1, 2, 3];
    vec.print_in_option();
}

```

## Voir aussi

[RFC pour la condition/clause `where`][rfc], [les structures][struct], [les traits][traits].

[rfc]: https://github.com/rust-lang/rfcs/blob/master/text/0135-where.md
[struct]: ../chapitre3/struct.html
[traits]: ../chapitre14/traits.html
