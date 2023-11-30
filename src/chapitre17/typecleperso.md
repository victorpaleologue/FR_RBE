# Personnaliser les types de clé

N'importe quel type implémentant les traits `Eq` et `Hash` peuvent être une clé dans une `HashMap`. Ce qui inclut:

* Le type `bool` (Bien que peut utile puisqu'il n'y a que deux clés possibles);
* Le type `int`, `uint` et toutes les variantes de ces derniers;
* `String` et `&str` (*note*: Vous pouvez avoir une `HashMap` recevant en entrée des `String` et appeler la méthode `.get()` avec une `&str`).

Notez que `f32` et `f64` n'implémentent pas `Hash`, sûrement parce les erreurs de précision rendrait leur utilisation en tant que clé d'une hashmap poserait des soucis.

Toutes les classes représentant une collection implémentent `Eq` et `Hash` si le type qu'elles contiennent implémentent également ces deux traits. Par exemple, `Vec<T>` implémentera `Hash` si `T` l'implémente.

Vous pouvez facilement implémenter `Eq` et `Hash` pour un nouveau type avec cette seule ligne: `#[derive(PartialEq, Hash)]`.

Le compilateur fera le reste. Si vous souhaitez avoir plus de contrôle sur les détails, vous pouvez implémenter `Eq` et/ou `Hash` vous-même. Ce guide ne couvre pas les implémentations spécifiques de `Hash`.

Pour tester l'utilisation d'une `struct` dans une `HashMap`, créons un simple système d'identification:

```rust,editable
use std::collections::HashMap;

// `Eq` nécessite de dériver `PartialEq` sur le type.
#[derive(PartialEq, Eq, Hash)]
struct Account<'a>{
    username: &'a str,
    password: &'a str,
}

struct AccountInfo<'a>{
    name: &'a str,
    email: &'a str,
}

type Accounts<'a> = HashMap<Account<'a>, AccountInfo<'a>>;

fn try_logon<'a>(accounts: &Accounts<'a>,
        username: &'a str, password: &'a str){
    println!("Username: {}", username);
    println!("Password: {}", password);
    println!("Attempting logon...");

    let logon = Account {
        username: username,
        password: password,
    };

    match accounts.get(&logon) {
        Some(account_info) => {
            println!("Successful logon!");
            println!("Name: {}", account_info.name);
            println!("Email: {}", account_info.email);
        },
        _ => println!("Login failed!"),
    }
}

fn main(){
    let mut accounts: Accounts = HashMap::new();

    let account = Account {
        username: "j.everyman",
        password: "password123",
    };

    let account_info = AccountInfo {
        name: "John Everyman",
        email: "j.everyman@email.com",
    };

    accounts.insert(account, account_info);

    try_logon(&accounts, "j.everyman", "psasword123");

    try_logon(&accounts, "j.everyman", "password123");
}

```
