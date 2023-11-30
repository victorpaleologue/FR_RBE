# Affichage formaté

L'affichage est pris en charge par une série de macros déclarées dans le module `std::fmt` qui inclut :


* `format!`: Construit la chaîne de caractères du texte à afficher;
* `print!`: Fait exactement la même chose que `format!`, mais le texte est affiché dans la console;
* `println!`: Fait exactement la même chose que `print!`, mais un retour à la ligne est ajouté.

Toutes formatent le texte de la même manière.

**Note**: La validité du formatage (i.e. Si la chaîne de caractères que vous soumettez peut être formatée comme vous le désirez) est vérifiée au moment de la compilation.

```rust,editable
fn main(){
    // En général, le marqueur '{}' sera automatiquement remplacé par 
    // n'importe quel argument. Il sera transformé en chaîne de caractères.
    println!("{} jours", 31);
    
    // Sans suffixe, 31 est de type i32. Vous pouvez changer le type de 31 avec
    // un suffixe. (e.g. 31i64)
    
    // Différents modèles peuvent être utilisés. 
    // Les marqueurs de position peuvent être utilisés.
    println!("{0}, voici {1}. {1}, voici {0}", "Alice", "Bob");
    
    // Les marqueurs peuvent également être
    // nommés
    println!("{sujet} {verbe} {objet}", 
    objet="le chien paresseux",
    sujet="Rapide, le renard",
    verbe="saute par-dessus");
    
    // Un formatage spécial peut être spécifié après un ':'.
    println!("{} personne sur {:b} sait lire le binaire, l'autre moité non.", 1, 2);
    
    // Vous pouvez aligner vers la droite votre texte en spécifiant 
    // la largeur (en espace) entre le côté gauche de la console 
    // et votre chaîne. Cet exemple affichera: "     1", un "1" après 5 espaces.

    println!("{number:>width$}", number=1, width=6);
    
    // Vous pouvez également remplacer les white spaces par des '0'.
    // Affiche: "000001"
    
    println!("{number:>0width$}", number=1, width=6);
    
    // Le nombre d'arguments utilisé est vérifié par le compilateur.
    // println!("Mon nom est {0}, {1} {0}", "Bond");
    // FIXME ^ Ajoutez l'argument manquant: "James".
    
    // On créé une structure nommé 'Structure' contenant un entier de type 'i32'.
    #[allow(dead_code)]
    struct Structure(i32);
    
    // Cependant, les types complexes tels que les structures demandent
    // une gestion de l'affichage plus complexe. Cela ne fonctionnera pas.
    // println!("Cette structure '{}' ne sera pas affichée...", Structure(3));
    // FIXME ^ Commentez/Décommentez cette ligne pour voir le message d'erreur.
}
```

`std::fmt` contient plusieurs traits qui structurent l'affichage du texte. Les deux plus « importants » sont listés ci-dessous :


1. [fmt::Debug][debug] : Utilise le marqueur `{:?}`. Applique un formatage dédié au débogage.
2. [fmt::Display][display] : Utilise le marqueur `{}`. Formate le texte de manière plus élégante, plus « user friendly ».

Dans cet exemple, `fmt::Display` était utilisé parce que la bibliothèque standard fournit les implémentations pour ces types. Pour afficher du texte à partir de types complexes/personnalisés, d'autres étapes sont requises.

## Activité

Réglez les deux problèmes dans le code ci-dessus (cf. FIXME) pour qu'il s'exécute sans erreurs.

Ajoutez une macro `println!` qui affiche : « Pi est, à peu près, égal à 3,142 » en contrôlant le nombre affiché de chiffres après la virgule. Dans le cadre de l'exercice, vous utiliserez `let pi = 3.141592` comme estimation de Pi (**Note**: Vous pourriez avoir besoin de consulter la documentation du module [std::fmt][fmt] pour configurer le nombre de décimaux à afficher).

## Voir aussi

[std::fmt][fmt], [les macros][macros], [les structures][struct], [les traits][traits].

[debug]: https://doc.rust-lang.org/std/fmt/trait.Debug.html
[display]: https://doc.rust-lang.org/std/fmt/trait.Display.html
[fmt]: https://doc.rust-lang.org/std/fmt/index.html
[macros]: ../chapitre15/systememacro.html
[struct]: ../chapitre3/struct.html
[traits]: ../chapitre14/traits.html
