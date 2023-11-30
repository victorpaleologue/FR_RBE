# Les sous-processus

La structure `process::Output` représente la sortie d'un sous-processus terminé et la structure `process::Command` est un constructeur de processus.

```rust,editable
use std::process::Command;

fn main() {
    let output = Command::new("rustc")
        .arg("--version")
        .output().unwrap_or_else(|e| {
            panic!("failed to execute process: {}", e)
    });

    if output.status.success() {
        let s = String::from_utf8_lossy(&output.stdout);

        print!("rustc succeeded and stdout was:\n{}", s);
    } else {
        let s = String::from_utf8_lossy(&output.stderr);

        print!("rustc failed and stderr was:\n{}", s);
    }
}

```

Nous vous encourageons à essayer l'exemple précédent en lançant `rustc` avec un flag incorrect.
