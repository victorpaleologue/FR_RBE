# L'inférence des types

Le moteur dédié à l'inférence des types est très intelligent. Il fait bien plus que d'inférer le type d'une `r-value` à l'initialisation. Il se charge également d'analyser l'utilisation de la variable dans la suite du programme pour inférer son type définitif. Voici un exemple plus avancé dédié à l'inférence :

```rust,editable
fn main() {
    // Dû à l'annotation(suffixe), le compilateur sait que `elem` possède le type 
    // u8.
    let elem = 5u8;

    // Crée un vecteur vide (un tableau dont la taille n'est pas définie).
    let mut vec = Vec::new();
    // À ce niveau, le compilateur ne connaît pas encore le type exact de `vec`,
    // il sait simplement que c'est un vecteur de quelque chose (`Vec<_>`).

    // On ajoute `elem` dans le vecteur.
    vec.push(elem);
    // Tada! Maintenant le compilateur sait que `vec` est un vecteur 
    // d'entiers non-signés typés `u8` (`Vec<u8>`).
    // TODO ^ Essayez de commenter la ligne où se trouve `vec.push(elem)`.

    println!("{:?}", vec);
}

```

Aucun typage explicite n'était nécessaire, le compilateur est heureux et le programmeur aussi !