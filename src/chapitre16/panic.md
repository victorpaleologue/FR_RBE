# La macro `panic`

Le plus simple mécanisme de gestion d'erreur que nous allons voir est `panic`. Il affiche un message d'erreur, lance la tâche et généralement met fin au programme. Ici, nous appelons explicitement `panic` dans notre condition:

```rust,editable
fn give_princess(gift: &str) {
    // Les princesses détestent les serpents, donc nous devons tout arrêter si elles n'acceptent pas !
    if gift == "snake" { panic!("AAAaaaaa!!!!"); }

    println!("I love {}s!!!!!", gift);
}

fn main() {
    give_princess("teddy bear");
    give_princess("snake");
}

```
