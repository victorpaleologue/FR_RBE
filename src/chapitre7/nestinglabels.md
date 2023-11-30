# L'imbrication et les labels

Il est possible de sortir (i.e. `break`) ou de relancer (i.e. `continue`) l'itération d'une boucle à partir d'une autre boucle interne à cette dernière. Pour ce faire, les boucles concernées doivent être annotées avec un `‘label` et il devra être passé aux instructions `break` et/ou `continue`.

```rust,editable
#![allow(unreachable_code)] // permet de faire taire les avertissements 
// relatifs au code mort.

fn main() {
    'externe: loop {
        println!("Entré dans la boucle annotée 'externe.");

        'interne: loop {
            println!("Entré dans la boucle annotée 'interne.");

            // Cette instruction nous ferait simplement 
            // sortir de la boucle 'interne.
            // break;
            
            // On sort de la boucle 'externe 
            // à partir de la boucle 'interne.
            break 'externe;
        }

        println!("Cette ligne ne sera jamais exécutée.");
    }

    println!("Sorti de la boucle annotée 'externe.");
}

```