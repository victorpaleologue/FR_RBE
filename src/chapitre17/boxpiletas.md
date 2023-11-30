# Les `Box`, la pile et le tas

En Rust, toutes les valeurs sont allouées dans la pile, par défaut. Les valeurs peuvent être *boxées* (i.e. allouées dans le tas) en créant une instance de `Box<T>`. Une "box" est un pointeur intelligent sur une ressource de type `T` allouée dans le tas. Lorsqu'une box sort du contexte, son destructeur est appelé, l'objet à charge est détruit et la mémoire du tas libérée.

Les valeurs "boxées" peuvent être déréférencées en utilisant l'opérateur `*`; Ceci supprime un [niveau d'indirection][indirection].

```rust,editable
use std::mem;

#[derive(Clone, Copy)]
struct Point {
    x: f64,
    y: f64,
}

#[allow(dead_code)]
struct Rectangle {
    p1: Point,
    p2: Point,
}

fn origin() -> Point {
    Point { x: 0.0, y: 0.0 }
}

fn boxed_origin() -> Box<Point> {
    // Alloue cette instance de `Point` dans le tas et renvoie un pointeur 
    // sur cette dernière.
    Box::new(Point { x: 0.0, y: 0.0 })
}

fn main() {
    // (Ici le typage est superflu)
    // Variables allouées dans la pile.
    let point: Point = origin();
    let rectangle: Rectangle = Rectangle {
        p1: origin(),
        p2: Point { x: 3.0, y: 4.0 }
    };

    // Rectangle alloué dans le tas.
    let boxed_rectangle: Box<Rectangle> = Box::new(Rectangle {
        p1: origin(),
        p2: origin()
    });

    // Le résultat des fonctions peut être boxé également.
    let boxed_point: Box<Point> = Box::new(origin());

    // Double indirection
    let box_in_a_box: Box<Box<Point>> = Box::new(boxed_origin());

    println!("Point occupies {} bytes in the stack",
             mem::size_of_val(&point));
    println!("Rectangle occupies {} bytes in the stack",
             mem::size_of_val(&rectangle));

    // La taille du pointeur est égale à la taille de la Box.
    println!("Boxed point occupies {} bytes in the stack",
             mem::size_of_val(&boxed_point));
    println!("Boxed rectangle occupies {} bytes in the stack",
             mem::size_of_val(&boxed_rectangle));
    println!("Boxed box occupies {} bytes in the stack",
             mem::size_of_val(&box_in_a_box));

    // La ressource contenue dans `boxed_point` est copiée dans 
    // `unboxed_point`.
    let unboxed_point: Point = *boxed_point;
    println!("Unboxed point occupies {} bytes in the stack",
             mem::size_of_val(&unboxed_point));
}

```

[indirection]: https://stackoverflow.com/questions/18003544/what-does-level-of-indirection-mean-in-david-wheelers-aphorism/18003704#18003704
