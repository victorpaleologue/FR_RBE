# Iterator::any

`Iterator::any` est une fonction qui, lorsqu'un itérateur est passé en paramètre, renvoie `true` si au moins un élément satisfait le [prédicat][predicat], autrement `false`. Voici sa signature :

```rust,editable
pub trait Iterator {
    // Le type sur lequel on va itérer.
    type Item;

    // `any` prend en paramètre une référence mutable `&mut self` de
    // l'instance courante qui sera empruntée et modifiée, mais pas consommée
    // (possédée).
    fn any<F>(&mut self, f: F) -> bool
    where
        F: FnMut(Self::Item) -> bool,
    {
        true
    }
}
# fn main() {}

```

```rust,editable
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()`, pour les vecteurs, fournit la référence de chaque 
    // élément `&i32`. 
    println!("2 in vec1: {}", vec1.iter()     .any(|&x| x == 2));
    // `into_iter()`, pour les vecteurs, fournit la valeur de chaque élément `i32`.
    // L'itérateur est consommé.
    println!("2 in vec2: {}", vec2.into_iter().any(| x| x == 2));
    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` fournit la référence de chaque élément du tableau `&i32`.
    println!("2 in array1: {}", array1.iter()     .any(|&x| x == 2));
    // `into_iter()` fournit, exceptionnellement, la référence de chaque élément
    // du tableau `&i32` (le type i32 implémente les traits requis).
    println!("2 in array2: {}", array2.into_iter().any(|&x| x == 2));
}

```

## Voir aussi

[std::iter::Iterator::any][any].

[any]: http://doc.rust-lang.org/std/iter/trait.Iterator.html#method.any
[predicat]: https://en.wikipedia.org/wiki/Predicate_%28mathematical_logic%29
