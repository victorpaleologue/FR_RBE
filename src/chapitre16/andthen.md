# Les combinateurs: `and_then`

`map()` a été décrite comme étant un moyen de chaîner les directives pour simplifier les déclarations `match`. Cependant, utiliser `map()` sur une fonction qui renvoie déjà une instance de `Option<T>` risque d'imbriquer le résultat dans une autre instance `Option<Option<T>>`. Chaîner des appels peut alors prêter à confusion. C'est là où un autre combinateur nommé `and_then()`, connu dans d'autres langages sous le nom de flatmap, entre en jeu.

`and_then()` appelle la fonction passée en entrée avec la valeur imbriquée et renvoie le résultat. Si le conteneur `Option` vaut `None`, alors elle renvoie `None` à la place.

Dans l'exemple suivant, `cookable_v2()` renvoie une instance de `Option<Food>`. Utiliser la méthode `map()` au lieu de `and_then()` donnerait une instance imbriquée `Option<Option<Food>>`, qui est un type invalide pour la fonction `eat()`.

```rust,editable
#![allow(dead_code)]

#[derive(Debug)] enum Food { CordonBleu, Steak, Sushi }
#[derive(Debug)] enum Day { Monday, Tuesday, Wednesday }

// Nous n'avons pas les ingrédients pour faire des sushis.
fn have_ingredients(food: Food) -> Option<Food> {
    match food {
        Food::Sushi => None,
        _           => Some(food),
    }
}

// Nous avons la recette de tous les mets sauf celle du Cordon Bleu.
fn have_recipe(food: Food) -> Option<Food> {
    match food {
        Food::CordonBleu => None,
        _                => Some(food),
    }
}


// Pour faire un plat, nous avons besoin de deux ingrédients et d'une recette.
// Nous pouvons représenter la logique avec une chaîne de `match`s:
fn cookable_v1(food: Food) -> Option<Food> {
    match have_ingredients(food) {
        None       => None,
        Some(food) => match have_recipe(food) {
            None       => None,
            Some(food) => Some(food),
        },
    }
}

// On peut rendre plus compacte cette implémentation en utilisant `and_then()`:
fn cookable_v2(food: Food) -> Option<Food> {
    have_ingredients(food).and_then(have_recipe)
}

fn eat(food: Food, day: Day) {
    match cookable_v2(food) {
        Some(food) => println!("Yay! On {:?} we get to eat {:?}.", day, food),
        None       => println!("Oh no. We don't get to eat on {:?}?", day),
    }
}

fn main() {
    let (cordon_bleu, steak, sushi) = (Food::CordonBleu, Food::Steak, Food::Sushi);

    eat(cordon_bleu, Day::Monday);
    eat(steak, Day::Tuesday);
    eat(sushi, Day::Wednesday);
}

```

## Voir aussi

[Les closures][closures], [Option][option] et [Option::and_then()][andthen].

[closures]: ../chapitre8/closures.html
[option]: https://doc.rust-lang.org/std/option/enum.Option.html
[andthen]: https://doc.rust-lang.org/std/option/enum.Option.html#method.and_then
