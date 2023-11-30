# La macro `try!`

Chaîner les résultats en utilisant match peut être très chaotique; heureusement, la macro `try!` peut être utilisée pour soigner l'écriture. La macro `try!` étend une expression de match où la branche `Err(err)` étend un retour prématuré (`return Err(err)`) et la branche `Ok(ok)` étend une expression `ok` et fournit la ressource.

```rust,editable
mod checked {
    #[derive(Debug)]
    enum MathError {
        DivisionByZero,
        NegativeLogarithm,
        NegativeSquareRoot,
    }

    type MathResult = Result<f64, MathError>;

    fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            Err(MathError::DivisionByZero)
        } else {
            Ok(x / y)
        }
    }

    fn sqrt(x: f64) -> MathResult {
        if x < 0.0 {
            Err(MathError::NegativeSquareRoot)
        } else {
            Ok(x.sqrt())
        }
    }

    fn ln(x: f64) -> MathResult {
        if x < 0.0 {
            Err(MathError::NegativeLogarithm)
        } else {
            Ok(x.ln())
        }
    }

    // Fonction intermédiaire.
    fn op_(x: f64, y: f64) -> MathResult {
        // Si la fonction `div` échoue, alors `DivisionByZero` sera renvoyée.
        let ratio = try!(div(x, y));

        // Si `ln` échoue, alors `NegativeLogarithm` sera renvoyée.
        let ln = try!(ln(ratio));

        sqrt(ln)
    }

    pub fn op(x: f64, y: f64) {
        match op_(x, y) {
            Err(why) => panic!(match why {
                MathError::NegativeLogarithm
                    => "logarithm of negative number",
                MathError::DivisionByZero
                    => "division by zero",
                MathError::NegativeSquareRoot
                    => "square root of negative number",
            }),
            Ok(value) => println!("{}", value),
        }
    }
}

fn main() {
    checked::op(1.0, 10.0);
}

```

N'hésitez pas à consulter la [documentation][doc], de nombreuses méthodes sont disponibles pour créer et gérer les `Result`.

[doc]: https://doc.rust-lang.org/std/result/index.html
