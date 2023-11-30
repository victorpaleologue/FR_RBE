# Les expressions

Un programme écrit en Rust est (principalement) composé d'une série de déclarations :

```rust,editable
fn main() {
    // déclaration
    // déclaration
    // déclaration
}

```

Il y a plusieurs sortes de déclarations en Rust. Les deux plus communes sont les assignations et les expressions suivies par un point-virgule « ; » :

```rust,editable
fn main() {
    // assignation
    let x = 5;

    // expression;
    x;
    x + 1;
    15;
}

```

Les blocs sont également des expressions, donc ils peuvent être utilisés comme `r-value` dans les assignations. La dernière expression dans le bloc sera assignée à la `l-value`. Notez toutefois que si la dernière expression du bloc se termine par un point-virgule « ; », la valeur de renvoi sera `()`.

```rust,editable
fn main() {
    let x = 5u32;

    let y = {
        let x_squared = x * x;
        let x_cube = x_squared * x;

        // Cette expression sera assignée à `y`.
        x_cube + x_squared + x
    };

    let z = {
        // Le point-virgule supprime cette expression et `()` est assigné 
        // à `z`.
        2 * x;
    };

    println!("x is {:?}", x);
    println!("y is {:?}", y);
    println!("z is {:?}", z);
}

```
