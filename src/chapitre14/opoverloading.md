# La surcharge des opérateurs

Avec Rust, nombre d'opérateurs peuvent être surchargés via les traits. En d'autres termes, des opérateurs peuvent être utilisés pour accomplir différentes tâches en fonction des arguments passés en entrée. Cette manipulation est possible parce que les opérateurs sont des sucres syntaxes visant à masquer l'appel des méthodes liées à ces derniers. Par exemple, l'opérateur `+` dans l'expression `a + b` appelle la méthode `add` (`a.add(b)`). La méthode `add` appartient au trait `Add`, d'où l'utilisation de l'opérateur `+` par tous les types implémentant le trait.

Vous pouvez retrouver la liste des traits surchargeant des opérateurs [ici][operators].

```rust,editable
use std::ops;

struct Foo;
struct Bar;

#[derive(Debug)]
struct FooBar;

#[derive(Debug)]
struct BarFoo;

// Le trait `std::ops::Add` est utilisé pour permettre la surcharge de `+`.
// Ici, nous spécifions `Add<Bar>` - cette implémentation sera appelée si l'opérande de droite est 
// de type `Bar`.
// Le bloc ci-dessous implémente l'opération: `Foo + Bar = FooBar`.
impl ops::Add<Bar> for Foo {
    type Output = FooBar;

    fn add(self, _rhs: Bar) -> FooBar {
        println!("> Foo.add(Bar) was called");

        FooBar
    }
}

// En inversant les types, nous nous retrouvons à implémenter une addition non-commutative.
// Ici, nous spécifions `Add<Foo>` - cette implémentation sera appelée si l'opérande de droite 
// est de type `Foo`.
// Le bloc ci-dessous implémente l'opération: `Bar + Foo = BarFoo`.
impl ops::Add<Foo> for Bar {
    type Output = BarFoo;

    fn add(self, _rhs: Foo) -> BarFoo {
        println!("> Bar.add(Foo) was called");

        BarFoo
    }
}

fn main() {
    println!("Foo + Bar = {:?}", Foo + Bar);
    println!("Bar + Foo = {:?}", Bar + Foo);
}

```

## Voir aussi

[Add][add_trait], [index de la syntaxe][index].

[opterators]: https://doc.rust-lang.org/core/ops/#traits
[add_trait]: https://doc.rust-lang.org/core/ops/trait.Add.html
[index]: https://doc.rust-lang.org/book/first-edition/syntax-index.html
