# Le problème

Un `trait` qui possède des types génériques en entrée doit respecter certaines règles : Les utilisateurs du trait doivent spécifier tous les types de données génériques supportés par le conteneur.

Dans l'exemple ci-dessous, le `trait` `Contains` permet l'utilisation des types génériques `A` et `B`. Le `trait` est alors implémenté pour le type `Container` en spécifiant le type `i32` pour les deux types génériques (i.e. `A` et `B`). Ils peuvent donc être soumis à la fonction `fn difference()`.

Puisque le type `Contains` est générique, nous sommes obligés de déclarer tous les types génériques supportés par `Contains` pour la fonction `difference()`. En pratique, nous opterions pour une approche nous permettant d'inférer les types génériques supportés par `Contains` à partir de l'entrée `C`. C'est ce que nous verrons dans la section suivante, car les types associés autorisent cette approche.

```rust,editable
struct Container(i32, i32);

// Nous déclarons un trait qui vérifie si deux items sont contenus 
// par le conteneur.
// Le conteneur pourra également fournir la première ou dernière 
// valeur.
trait Contains<A, B> {
    fn contains(&self, &A, &B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;  
}

impl Contains<i32, i32> for Container {
    // Renvoie `true` si les nombres stockés sont égaux.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }

    // On récupère la première valeur.
    fn first(&self) -> i32 { self.0 }

    // On récupère la dernière valeur.
    fn last(&self) -> i32 { self.1 }
}

// `C` contient `A` et `B`. Les déclarer une nouvelle fois dans les paramètres 
// génériques de la fonction est fastidieux.
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("Does container contain {} and {}: {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("First number: {}", container.first());
    println!("Last number: {}", container.last());

    println!("The difference is: {}", difference(&container));
}

```

## Voir aussi

[Les structures][struct].

[struct]: ../chapitre3/struct.html
