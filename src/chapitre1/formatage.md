# Formatage

Nous avons vu que le formatage désiré était spécifié par des « chaînes de formatage » :


* `format!("{}", foo) -> "3735928559"` ;
* `format!("0x{:X}", foo) -> "0xDEADBEEF"` ;
* `format!("0o{:o}", foo) -> "0o33653337357"`.

La même variable (`foo`) peut être formatée de différentes manières suivant le type d'argument utilisé dans le marqueur (e.g. `X`, `o`, rien).

Cette fonctionnalité est implémentée à l'aide de traits, et il y en a un pour chaque type d'argument. Le plus commun est, bien entendu, `Display`. Il est chargé de gérer les cas où le type d'argument n'est pas spécifié (i.e. `{}`).

```rust,editable
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // Latitude
    lat: f32,
    // Longitude
    lon: f32,
}

impl Display for City {
    // `f` est un tampon, cette méthode écrit la chaîne de caractères
    // formattée à l'intérieur de ce dernier.
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` est équivalente à `format!`, à l'exception qu'elle écrira
        // la chaîne de caractères formatée dans un tampon (le premier argument).
        write!(f, "{}: {:.3}°{} {:.3}°{}",
               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c)
    }
}

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    for city in [
        City { name: "Dublin", lat: 53.347778, lon: -6.259722 },
        City { name: "Oslo", lat: 59.95, lon: 10.75 },
        City { name: "Vancouver", lat: 49.25, lon: -123.1 },
    ].iter() {
        println!("{}", *city);
    }
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ].iter() {
        // Utilisez le marqueur `{}` une fois que vous aurez implémenté
        // le trait fmt::Display.
        println!("{:?}", *color)
    }
}
```

N'hésitez pas à consulter [la liste complète des traits][fmt_traits] dédiés au formatage ainsi que leurs types d'argument dans la documentation du module [std::fmt][fmt].

## Activité

Implémentez le trait `fmt::Display` pour la structure `Color` dans l'exemple ci-dessus de manière à obtenir un résultat identique à celui-ci:

```text
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000
```

Indices:


* Vous pourriez [avoir besoin d'itérer plusieurs fois][fmt_argtypes] sur vos couleurs;
* Vous pouvez [créer une « compensation »][fmt_width] (remplissant votre chaîne de zéros) d'une largeur `n` avec `:0n`.

## Voir aussi

[std::fmt][fmt]

[fmt_traits]: http://doc.rust-lang.org/std/fmt/#formatting-traits
[fmt]: http://doc.rust-lang.org/std/fmt/
[fmt_argtypes]: http://doc.rust-lang.org/std/fmt/#argument-types
[fmt_width]: http://doc.rust-lang.org/std/fmt/#width
