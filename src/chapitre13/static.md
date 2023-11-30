# La lifetime `'static`

Une ressource annotée du label `‘static` possède la plus longue durée de vie qu'on puisse assigner. La durée de vie de `‘static` est égale à celle du programme lui-même et peut également être raccourcie selon le contexte.

Il y a deux façons d'assigner la lifetime `‘static`, et toutes deux stockeront la ressource directement dans le binaire en lecture seule :

1. Créer une constante avec la déclaration `static`;
2. Créer une chaîne de caractères avec le `"littéral"` en l'annotant du type `&'static str`.

Voici un exemple pour illustrer les deux manières de faire :

```rust,editable
// On créé une constante avec la lifetime `'static` en utilisant 
// le mot-clé `static`.
static NUM: i32 = 18;

// Renvoie une référence de `NUM` où sa lifetime `'static` 
// est obligée de s'aligner avec la durée de vie du paramètre 
// passé à la fonction.
fn coerce_static<'a>(_: &'a i32) -> &'a i32 {
    &NUM
}

fn main() {
    {
        // On créé une chaîne de caractères littérale, primitive 
        // et on l'affiche.
        let static_string = "I'm in read-only memory";
        println!("static_string: {}", static_string);

        // Lorsque `static_string` sortira du contexte, la référence 
        // ne pourra plus être utilisée, mais la ressource restera 
        // présente dans le binaire.
    }

    {
        // On créé un entier à passer à la 
        // fonction `coerce_static`:
        let lifetime_num = 9;

        // On aligne, adapte la durée de vie de `NUM à 
        // celle de `lifetime_num`:
        let coerced_static = coerce_static(&lifetime_num);

        println!("coerced_static: {}", coerced_static);
    }

    println!("NUM: {} stays accessible!", NUM);
}

```

## Voir aussi

[Les constantes](../chapitre3/constantes.html).
