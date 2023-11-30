# if let

Pour certains cas, `match` peut être « lourd ». Par exemple :

```rust,editable
// Crée une valeur optionnelle de type `Option<i32>`.
let optional = Some(7);

match optional {
    Some(i) => {
        println!("Ceci est une très longue chaîne de caractères contenant un 
        `{:?}`", i);
        // ^ Deux niveaux d'indentations sont nécessaires alors 
        // que nous aurions pu simplement déstructurer `i`.
    },
    _ => {},
    // ^ Nécessaire parce que `match` est exhaustif. Cette branche vous 
    // paraît-elle utile?
};
```

`if let` est plus adapté à ce genre de cas et permet la création de plusieurs branches en cas d'erreur :

```rust,editable
fn main() {
    // Toutes les variables sont de type `Option<i32>`.
    let number = Some(7);
    let letter: Option<i32> = None;
    let emoticon: Option<i32> = None;

    // L'ensemble `if let` se déroule de cette manière: 
    // `if let` déstructure `number` et assigne sa valeur à `i` et exécute 
    // le bloc (`{}`).
    if let Some(i) = number {
        println!("{:?} a été trouvé!", i);
    }

    // Si vous devez spécifier un cas d'erreur, utilisez un `else`:
    if let Some(i) = letter {
        println!("{:?} a été trouvé!", i);
    } else {
        // Déstructuration ratée. On exécute le `else`.
        println!("Aucun nombre n'a été trouvé. 
        Cherchons une lettre!");
    };

    // Fournit une condition alternative.
    let i_like_letters = false;

    if let Some(i) = emoticon {
        println!("{:?} a été trouvé!", i);
    // Déstructuration ratée. Passe à une condition `else if` pour tester si 
    // la condition alternative est vraie.
    } else if i_like_letters {
        println!("Aucun nombre n'a été trouvé. 
        Cherchons une lettre!");
    } else {
        // La condition évaluée est fausse. Branche par défaut:
        println!("Je n'aime pas les lettres. Cherchons une emoticône :)!");
    };
}
```

## Voir aussi 

[Les énumérations][enums], [l'énumération `Option`][option] et [la RFC de if let][rfc].

[enums]: ../chapitre3/enum.html
[option]: ../chapitre17/enumoption.html
[rfc]: https://github.com/rust-lang/rfcs/pull/160
