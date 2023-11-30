# La boucle for et les invervalles

L'ensemble `for in` peut être utilisé pour itérer à l'aide d'une instance `Iterator`. L'une des manières les plus simples pour créer un itérateur est d'utiliser la notation d'intervalle (« range notation ») `a..b`. Soit un intervalle `[a;b[` (comprend toutes les valeurs entre `a` (inclut) et `b` (exclut)).

Écrivons les règles de *FizzBuzz* en utilisant la boucle `for` au lieu de `while`.

```rust,editable
fn main() {
    // `n` prendra pour valeur: 1, 2, ..., 100  au fil des itérations. 
    for n in 1..101 {
        if n % 15 == 0 {
            println!("fizzbuzz");
        } else if n % 3 == 0 {
            println!("fizz");
        } else if n % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", n);
        }
    }
}
```

## Voir aussi

[Les itérateurs][iterators].

[iterators]: ../chapitre14/iterators.html
