# La structure `HashMap`

Là où les vecteurs stockent leurs valeurs en utilisant un index entier, les `HashMap`s stockent leurs valeurs en utilisant des clés. Les clés d'une `HashMap` peuvent être des booléens, des chaînes de caractères ou n'importe quel autre type qui implémente les traits `Eq` et `Hash`. Nous y reviendrons dans la section suivante.

Tout comme les vecteurs, les `HashMap` sont redimensionnables mais peuvent également se tronquer elles-mêmes lorsqu'elles atteignent la limite de leur capacité. 
Vous pouvez créer une `HashMap` avec une capacité donnée en utilisant `HashMap::with_capacity(uint)`, ou utiliser `HashMap::new()` pour récupérer une instance avec une capacité initiale par défaut (recommandé).

```rust,editable
use std::collections::HashMap;

fn call(number: &str) -> &str {
    match number {
        "798-1364" => "We're sorry, the call cannot be completed as dialed. 
            Please hang up and try again.",
        "645-7689" => "Hello, this is Mr. Awesome's Pizza. My name is Fred.
            What can I get for you today?",
        _ => "Hi! Who is this again?"
    }
}

fn main() { 
    let mut contacts = HashMap::new();

    contacts.insert("Daniel", "798-1364");
    contacts.insert("Ashley", "645-7689");
    contacts.insert("Katie", "435-8291");
    contacts.insert("Robert", "956-1745");

    // Prend une référence en entrée et renvoie un conteneur `Option<&V>`.
    match contacts.get(&"Daniel") {
        Some(&number) => println!("Calling Daniel: {}", call(number)),
        _ => println!("Don't have Daniel's number."),
    }


    // La méthode `HashMap::insert()` renvoie `None` 
    // si la valeur insérée est nouvelle, sinon `Some(value)`.
    contacts.insert("Daniel", "164-6743");

    match contacts.get(&"Ashley") {
        Some(&number) => println!("Calling Ashley: {}", call(number)),
        _ => println!("Don't have Ashley's number."),
    }

    contacts.remove(&("Ashley")); 

    // La méthode `HashMap::iter()` renvoie un itérateur qui fournit 
    // les paires (&'a key, &'a value) dans un ordre arbitraire.
    for (contact, &number) in contacts.iter() {
        println!("Calling {}: {}", contact, call(number)); 
    }
}

```

Pour plus d"informations à propos du fonctionnement du hashage et des hash maps (parfois appelées hash tables), consultez [la page wikipédia dédiée aux Hash Tables][hashtables].

[hashtables]: https://en.wikipedia.org/wiki/Hash_table
