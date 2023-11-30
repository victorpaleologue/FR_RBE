# La structure `Path`

La structure `Path` représente les chemins de fichiers dans le système de fichiers sous-jacent. Il y a deux variantes de `Path`:

1. `posix::Path`, pour les systèmes UNIX-like;
2. `windows::Path`, pour Windows.

Le prélude exporte la variante de `Path` adaptée à la plateforme.

Une instance de `Path` peut être créée à partir du type `OsStr` et fournit de nombreuses méthodes pour obtenir des informations à propos du fichier/répertoire sur lequel le chemin pointe.

Notez que, en interne, un objet `Path` n'est pas représenté par une chaîne de caractères UTF-8 mais est stocké dans un vecteur d'octets (`Vec<u8>`). En conséquence, la conversion d'un objet `Path` en `&str` n'est pas gratuite et peut échouer (un objet `Option` est renvoyé).

```rust,editable
use std::path::{Path, PathBuf};
use std::ffi;

fn main() {
    // Création d'un objet `Path` à partir d'une `&'static str`.
    let path = Path::new(".");

    // La méthode `display` renvoie une structure présentable.
    let display = path.display();

    // La méthode `join()` fusionne un chemin avec toutes les ressources 
    // possédant une implémentation de la méthode `as_ref()` pour le type `Path` et 
    // renvoie un nouveau chemin avec le séparateur spécifique à l'OS.
    let new_path = path.join("a").join("b");

    // Convertit le chemin en une vue sur une string.
    match new_path.to_str() {
        None => panic!("new path is not a valid UTF-8 sequence"),
        Some(s) => println!("new path is {}", s),
    }
}

```

N'hésitez pas à cosnulter les autres méthodes de `Path` et la structure `Metadata`.

## Voir aussi

[OsStr][doc_osstr] et [Metadata][doc_metadata].

[doc_osstr]: https://doc.rust-lang.org/std/ffi/struct.OsStr.html
[doc_metadata]: https://doc.rust-lang.org/std/fs/struct.Metadata.html
