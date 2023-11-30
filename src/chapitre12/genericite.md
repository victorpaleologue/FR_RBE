# La généricité

Comme son nom l'indique, cette section abordera les types et fonctionnalités génériques. La généricité peut être très utile pour réduire les répétitions au sein du code dans de nombreux cas, mais vous demandera, en échange, d'apporter quelques précisions supplémentaires à propos de la syntaxe. Notez également que rendre une ressource générique signifie que n'importe quelle ressource sera traitée de la même manière, il est nécessaire de savoir quels types de ressources peuvent être réellement traités, dans les cas où il est nécessaire de le spécifier.

La généricité est principalement utilisée pour rendre générique un, ou plusieurs, paramètre passé à une fonction. Par convention, un paramètre générique doit avoir un identificateur respectant la convention de nommage CamelCase et être déclaré entre un chevron ouvrant (`<`) et un chevron fermant(`>`) : `<Aaa, Bbb, ...>`, qui est souvent représenté par le paramètre `<T>.` En déclarant un paramètre générique de type `<T>`, on accepte de recevoir un, ou plusieurs, paramètre de ce type. Tout paramètre déclaré comme générique est générique, tout le reste est concret (non-générique).

Par exemple, voici une fonction générique nommée `foo` qui prend un paramètre de type `T` (de n'importe quel type, donc) :

```rust,ignore
fn foo<T>(p: T) { ... }
```

```rust,editable
// A est un type concret.
struct A;

// Lorsque nous déclarons `Single`, la première occurrence de `A` n'est 
// pas précédée du type générique `<A>`. Le type `Single` et `A` sont donc 
// concrets.
struct Single(A);
//            ^ Voici la première occurrence du type `A`.

// En revanche, ici, `<T>` précède la première occurrence `T`, donc le type 
// `SingleGen` est générique. Puisque le type `T` est générique, cela pourrait être 
// "n'importe quoi", y compris le type concret `A` déclaré au début du fichier.
struct SingleGen<T>(T);

fn main() {
    // `Single` est un type concret et prend explicitement un paramètre 
    // de type `A`.
    let _s = Single(A);

    // On créé une variable nommée `_char` de type `SingleGen<char>`
    // et on lui assigne la valeur `SingleGen('a')`.
    // Le type requis du paramètre passé pour cette instance de `SingleGen` 
    // est spécifié, mais il peut être omis, exemple ---
    let _char: SingleGen<char> = SingleGen('a');

    // --->
    let _t    = SingleGen(A); // On passe une instance 
                              // du type `A` définit en haut.
    let _i32  = SingleGen(6); // On passe un entier de type `i32`.
    let _char = SingleGen('a'); // On passe un `char`.
}

```

## Voir aussi

[Les structures][struct]

[struct]: ../chapitre3/struct.html
