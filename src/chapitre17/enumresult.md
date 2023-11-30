# L'énumération `Result`

Nous avons vu que l'enum `Option` peut être utilisée en tant que valeur de retour depuis les fonctions pouvant échouer, où `None` peut être renvoyé pour indiquer un échec. Il est parfois important d'expliquer *pourquoi* une opération a échoué. Pour ce faire, nous pouvons utiliser `Result`.

`Result<T, E>` possède deux variantes:

1. `Ok(valeur)` qui signale que l'opération s'est correctement déroulée et enveloppe la `valeur` renvoyée par l'opération (`valeur` est de type `T`);
2. `Err(pourquoi)` qui signale que l'opération a échoué et enveloppe le `pourquoi`, qui (espérons-le) nous renseigne sur la cause de l'échec (`pourquoi` est de type `E`).

```rust,editable
mod checked {
    // Les "erreurs" mathématiques que nous voulons gérer.
    #[derive(Debug)]
    pub enum MathError {
        DivisionByZero,
        NonPositiveLogarithm,
        NegativeSquareRoot,
    }

    pub type MathResult = Result<f64, MathError>;

    pub fn div(x: f64, y: f64) -> MathResult {
        if y == 0.0 {
            // Cette opération échouerait, nous wrappons l'erreur dans une instance 
            // `Err` à la place.
            Err(MathError::DivisionByZero)
        } else {
            // Cette opération est valide, nous renvoyons le résultat wrappé dans `Ok`.
            Ok(x / y)
        }
    }

    pub fn sqrt(x: f64) -> MathResult {
        if x < 0.0 {
            Err(MathError::NegativeSquareRoot)
        } else {
            Ok(x.sqrt())
        }
    }

    pub fn ln(x: f64) -> MathResult {
        if x <= 0.0 {
            Err(MathError::NonPositiveLogarithm)
        } else {
            Ok(x.ln())
        }
    }
}

// `op(x, y)` === `sqrt(ln(x / y))`
fn op(x: f64, y: f64) -> f64 {
    // Ceci est une pyramide de match à trois niveaux !
    match checked::div(x, y) {
        Err(why) => panic!("{:?}", why),
        Ok(ratio) => match checked::ln(ratio) {
            Err(why) => panic!("{:?}", why),
            Ok(ln) => match checked::sqrt(ln) {
                Err(why) => panic!("{:?}", why),
                Ok(sqrt) => sqrt,
            },
        },
    }
}

fn main() {
    // Cette opération va-t-elle échouer ?
    println!("{}", op(1.0, 10.0));
}

```
