# Les alias

Le mot-clé `type` peut être utilisé pour donner un nouveau nom à un type existant. Les types doivent respecter la convention de nommage *CamelCase* ou le compilateur vous renverra un avertissement. L'exception à cette règle sont les types primitifs : `usize`, `f32`, etc.

```rust,editable
// `NanoSecond` est le nouveau nom de `u64`.
type NanoSecond = u64;
type Inch = u64;

// Utilisons un attribut pour faire taire les 
// avertissements.
#[allow(non_camel_case_types)]
type u64_t = u64;
// TODO ^ Essayez de supprimer l'attribut.

fn main() {
    // `NanoSecond` = `Inch` = `u64_t` = `u64`.
    let nanoseconds: NanoSecond = 5 as u64_t;
    let inches: Inch = 2 as u64_t;
    
    // Notez que les alias de types ne fournissent aucune sécurité supplémentaire,
    // car ce ne sont pas de nouveaux types (i.e. vous pouvez très bien changer
    // Inch par NanoSecond, vous n'aurez aucune erreur).
    println!("{} nanoseconds + {} inches = {} unit?",
             nanoseconds,
             inches,
             nanoseconds + inches);
}
```

## Voir aussi

[Les attributs][attributes].

[attributes]: ../chapitre11/attributes.html
