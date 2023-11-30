# La structure `HashSet`

Voyez une `HashSet` comme une `HashMap` où nous nous soucions uniquement des clés (`HashSet<T>` est, en réalité, simplement un wrapper de `HashMap<T, ()>`).

Vous pourriez vous demander "Quel est le but ? Je pourrais simplement stocker mes clés dans un `Vec`".

La fonctionnalité unique de `HashSet` est qu'elle garantit l'inexistance d'éléments dupliqués. C'est le contrat que n'importe quel ensemble remplit. `HashSet` n'est qu'une implémentation (voir aussi: [BTreeSet][btree_set]).

Si vous ajoutez une valeur déjà présente dans l'instance `HashSet`, (i.e. la nouvelle valeur est égale à l'existante et ont toutes deux le même hash), alors la nouvelle valeur remplacera l'ancienne.

C'est pratique lorsque vous ne souhaitez jamais plus d'une occurrence de quelque chose ou lorsque vous voulez savoir si vous possédez déjà quelque chose. Mais les ensembles peuvent faire bien plus que cela.

Les ensembles ont quatre (4) opérations inhérentes (chacune renvoie un itérateur):

1. `union`:  Récupère tous les éléments dans les deux ensembles;
2. `difference`: Récupère tous les éléments qui sont dans le premier ensemble mais pas dans le second;
3. `intersection`: Récupère uniquement les éléments présents dans les *deux* ensembles;
4. `symmetric_difference`: Récupère tous éléments qui sont dans le premier ou second ensemble mais *pas* les deux.

Essayons tout cela dans l'exemple suivant.

```rust,editable
use std::collections::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec!(1i32, 2, 3).into_iter().collect();
    let mut b: HashSet<i32> = vec!(2i32, 3, 4).into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // `HashSet::insert()` renvoie false si 
    // une valeur était déjà présente.
    // assert!(b.insert(4), "Value 4 is already in set B!");
    // FIXME ^ Commentez/décommentez cette ligne

    b.insert(5);

    // Si le type d'un élément de la collection implémente le trait `Debug`,
    // alors la collection devra, elle aussi, implémenter `Debug`.
    // Elle affiche généralement ses éléments dans le format `[elem1, elem2, ...]`.
    println!("A: {:?}", a);
    println!("B: {:?}", b);

    // Affiche [1, 2, 3, 4, 5] dans un ordre arbitraire.
    println!("Union: {:?}", a.union(&b).collect::<Vec<&i32>>());

    // Ceci devrait afficher [1].
    println!("Difference: {:?}", a.difference(&b).collect::<Vec<&i32>>());

    // Affiche [2, 3, 4] dans un ordre arbitraire.
    println!("Intersection: {:?}", a.intersection(&b).collect::<Vec<&i32>>());

    // Affiche [1, 5].
    println!("Symmetric Difference: {:?}",
             a.symmetric_difference(&b).collect::<Vec<&i32>>());
}

```

Les exemples originaux proviennent de la [documentation][doc].

[btree_set]: https://doc.rust-lang.org/std/collections/struct.BTreeSet.html
[doc]: https://doc.rust-lang.org/std/collections/struct.HashSet.html#method.difference
