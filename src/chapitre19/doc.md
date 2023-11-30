# Documentation

Les commentaires de documentation sont très utiles pour d'importants projets nécessitant une documentation. Lorsque vous lancez [Rustdoc][rd], ce sont ces commentaires qui seront compilés dans la documentation. Ils sont préfixés par la séquence `///` et supportent [Markdown][md].

```rust,editable
// #![crate_name = "doc"]

/// Un être humain est représenté ici.
pub struct Person {
    /// Une personne doit avoir un nom.
    name: String,
}

impl Person {
    /// Renvoie une personne avec le nom qu'on lui a donné.
    ///
    /// # Arguments
    ///
    /// * `name` - Une slice qui contient le nom de la personne.
    ///
    /// # Example
    ///
    /// ```
    /// // Vous pouvez écrire du code rust entre les balises
    /// // dans les commentaires.
    /// // Si vous passez --test à Rustdoc, il testera même la source pour vous !
    /// use doc::Person;
    /// let person = Person::new("name");
    /// ```
    pub fn new(name: &str) -> Person {
        Person { name: name.to_string() }
    }

    /// Affiche un salut amical !
    ///
    /// Affiche "Hello, [name]" à l'objet `Person` en question.
    pub fn hello(&self) {
        println!("Hello, {}!", self.name);
    }
}

fn main() {
    let john = Person::new("John");

    john.hello();
}

```

> **Note**: Si vous souhaitez compiler ce programme vous-même, n'oubliez pas de décommenter la ligne `// #![crate_name = "doc"]`.

Pour lancer les tests, vous devez tout d'abord compiler le code en mode bibliothèque puis renseigner la position de la bibliothèque à rustdoc pour qu'il puisse la lier à chaque programme de la documentation:

```bash
rustc doc.rs --crate-type lib
rustdoc --test --extern doc="libdoc.rs"
```

Lorsque vous exécutez la commande `cargo test` sur une crate, Cargo générera et exécutera automatiquement les commandes respectives de rustc et rustdoc.

[rd]: https://doc.rust-lang.org/book/first-edition/documentation.html#about-rustdoc
[md]:  https://en.wikipedia.org/wiki/Markdown
